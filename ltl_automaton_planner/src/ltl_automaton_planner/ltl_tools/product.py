# -*- coding: utf-8 -*-
import rospy
from ltl_automaton_planner.ltl_tools.buchi import check_label_for_buchi_edge
#from discrete_plan import has_path_to_accept

from networkx.classes.digraph import DiGraph
from networkx import find_cycle, NetworkXNoCycle
import time


class ProdAut(DiGraph):
    def __init__(self, ts, buchi, beta=1000):
        DiGraph.__init__(self, ts=ts, buchi=buchi, beta=beta, initial=set(), accept=set(), accept_with_cycle = set(), type='ProdAut')

    # Build product automaton of TS and büchi by exploring every node combination and adding edges when required
    def build_full(self):
        # Iterate over all TS nodes and buchi nodes
        for f_ts_node in self.graph['ts'].nodes():
            # ('c1_r1', 'rescue')
            for f_buchi_node in self.graph['buchi'].nodes():
                # Compose node from current TS and buchi node
                f_prod_node = self.composition(f_ts_node, f_buchi_node)
                # Iterate over all nodes connected to current TS node and büchi node
                for t_ts_node in self.graph['ts'].successors(f_ts_node):
                    for t_buchi_node in self.graph['buchi'].successors(f_buchi_node):
                            # Compose node from connected buchi node and connected TS node, and check if this node
                            # should be connected to previously composed TS/büchi node
                            t_prod_node = self.composition(t_ts_node, t_buchi_node)
                            # Get label from TS node, and weight and action from TS edge
                            label = self.graph['ts'].nodes[f_ts_node]['label']
                            
                            cost = self.graph['ts'][f_ts_node][t_ts_node]['weight'] #action weight
                            action = self.graph['ts'][f_ts_node][t_ts_node]['action']
                            # Check if label is compatible with büchi (black magic for now, need to understand this better)
                            truth, dist = check_label_for_buchi_edge(self.graph['buchi'], label, f_buchi_node, t_buchi_node)
                            total_weight = cost + self.graph['beta']*dist
                            if truth:
                                self.add_edge(f_prod_node, t_prod_node, transition_cost=cost, soft_task_dist=dist, weight=total_weight, action=action)
        print(self.graph['buchi'].graph['accept'])
        # self.build_accept_with_cycle()
       
        # Build initial possible state set from initial state
        self.possible_states = set(self.graph['initial'])

        rospy.loginfo('LTL Planner: full product constructed with %d states and %s transitions' %(len(self.nodes()), len(self.edges())))

    def build_full_relaxed(self):
        # Iterate over all TS nodes and buchi nodes
        for f_ts_node in self.graph['ts'].nodes():
            # ('c1_r1', 'rescue')
            for f_buchi_node in self.graph['buchi'].nodes():
                # Compose node from current TS and buchi node
                f_prod_node = self.composition(f_ts_node, f_buchi_node)
                # Iterate over all nodes connected to current TS node and büchi node
                for t_ts_node in self.graph['ts'].successors(f_ts_node):
                    for t_buchi_node in self.graph['buchi'].successors(f_buchi_node):
                            # Compose node from connected buchi node and connected TS node, and check if this node
                            # should be connected to previously composed TS/büchi node
                            t_prod_node = self.composition(t_ts_node, t_buchi_node)
                            # Get label from TS node, and weight and action from TS edge
                            label = self.graph['ts'].nodes[f_ts_node]['label']
                            cost = self.graph['ts'][f_ts_node][t_ts_node]['weight'] #action weight
                            action = self.graph['ts'][f_ts_node][t_ts_node]['action']
                            # Check if label is compatible with büchi (black magic for now, need to understand this better)
                            truth, dist = check_label_for_buchi_edge(self.graph['buchi'], label, f_buchi_node, t_buchi_node)
                            total_weight = cost + 100000*dist
                            self.add_edge(f_prod_node, t_prod_node, transition_cost=cost, soft_task_dist=dist, weight=total_weight, action=action)

        # self.build_accept_with_cycle()

        # Build initial possible state set from initial state
        self.possible_states = set(self.graph['initial'])

        rospy.loginfo('LTL Planner: full product constructed with %d states and %s transitions' %(len(self.nodes()), len(self.edges())))
    
    # Build required for IRL
    def build_full_margin(self, opt_path):
        opt_edges = None
        if len(opt_path) >= 2:
            opt_edges = zip(opt_path[0::2], opt_path[1::2])
        for f_ts_node in self.graph['ts'].nodes():
            for f_buchi_node in self.graph['buchi'].nodes():
                f_prod_node = self.composition(f_ts_node, f_buchi_node)
                                  
                for t_ts_node in self.graph['ts'].successors(f_ts_node):
                    for t_buchi_node in self.graph['buchi'].successors(f_buchi_node):
                            t_prod_node = self.composition(t_ts_node, t_buchi_node)

                            label = self.graph['ts'].nodes[f_ts_node]['label']
                            cost = self.graph['ts'][f_ts_node][t_ts_node]['weight'] #action weight
                            truth, dist = check_label_for_buchi_edge(self.graph['buchi'], label, f_buchi_node, t_buchi_node)
                            total_weight = cost + self.graph['beta']*dist + 1

                            if not opt_edges == None:
                                if (f_prod_node, t_prod_node) in opt_edges:
                                    k = 1
                                else:
                                    k = 0
                            else:
                                k = 0
                            total_weight -= k
                            if truth:
                                self.add_edge(f_prod_node, t_prod_node, weight=total_weight, transition_cost=cost, soft_task_dist=dist)

        self.build_accept_with_cycle()


    def update_beta(self, beta):
        # update the saved parameter for beta
        self.graph['beta'] = beta
        
        # compute new weight associate to each edge in the ProdAut based on new value of beta
        for (u, v) in self.edges():
            self[u][v]['weight'] = self[u][v]['transition_cost'] + beta*self[u][v]['soft_task_dist']



    def composition(self, ts_node, buchi_node):
        # Compose node from TS and Büchi
        prod_node = (ts_node, buchi_node)
        # If node not already in product graph, add node to graph
        if not self.has_node(prod_node):
            self.add_node(prod_node, ts=ts_node, buchi=buchi_node, marker='unvisited')
            # If TS and Büchi nodes are both initial nodes in their own graph, composed node is initial
            if ((ts_node in self.graph['ts'].graph['initial']) and
                (buchi_node in self.graph['buchi'].graph['initial'])):
                self.graph['initial'].add(prod_node)
            # If Büchi node is an accept state, composed node is an accept state
            if (buchi_node in self.graph['buchi'].graph['accept']):
                # if 'e' in self.graph['ts'].nodes[ts_node]['label']:
                    self.graph['accept'].add(prod_node)
        return prod_node

    def projection(self, prod_node):
        ts_node = self.nodes[prod_node]['ts']
        buchi_node = self.nodes[prod_node]['buchi']
        return ts_node, buchi_node

    #------------------------------
    # Build initial product states
    #------------------------------
    # Initial states of TS and Büchi needs to be
    # defined before calling this function
    def build_initial(self):
        # Reset initial set
        self.graph['initial'] = set()
        # Go through all initial states in TS
        for ts_init in self.graph['ts'].graph['initial']:
            # Go through all initial states in Büchi
            for buchi_init in self.graph['buchi'].graph['initial']:
                # If both TS and Büchi state are initial state, build composed node and add it to the product initial set
                init_prod_node = (ts_init, buchi_init)
                self.graph['initial'].add(init_prod_node)

        # Build initial reachable set from initial state
        self.possible_states = set(self.graph['initial'])

    #-----------------------------
    # Build accept product states
    #-----------------------------
    # TS needs to be built and Büchi accept states
    # defined before calling this function
    def build_accept(self):
        # Reset initial set
        self.graph['accept'] = set()
        # Go through all TS states
        for ts_node in self.graph['ts'].nodes():
            # Go through all accept states in Büchi
            for buchi_accept in self.graph['buchi'].graph['accept']:
                accept_prod_node = (ts_node, buchi_accept)
                # If Büchi state is an accept state, build composed node and add it to the product accept set
                self.graph['accept'].add(accept_prod_node)

    #----------------------------------------
    # Build accept product states with cycle
    #----------------------------------------
    # TS needs to be built and Büchi accept states
    # defined before calling this function
    def build_accept_with_cycle(self):
        # self.graph['ts'].build_full()
        for accept_state in self.graph['accept']:
            try:
                # print('Accepting state in consider is', accept_state)
                find_cycle(self, accept_state, orientation="original")
            except NetworkXNoCycle:
                # print(accept_state, 'fails to find a cycle')
                pass
            else:
                # print(accept_state, 'finds a cycle')
                self.graph['accept_with_cycle'].add(accept_state)

    def accept_predecessors(self, accept_node):
        pre_set = set()
        t_ts_node, t_buchi_node = self.projection(accept_node)
        for f_ts_node, cost in self.graph['ts'].predecessors(t_ts_node):
            for f_buchi_node in self.graph['buchi'].predecessors(t_buchi_node):
                f_prod_node = self.composition(f_ts_node, f_buchi_node)
                label = self.graph['ts'].nodes[f_ts_node]['label']
                truth, dist = check_label_for_buchi_edge(self.graph['buchi'], label, f_buchi_node, t_buchi_node)
                total_weight = cost + self.graph['beta']*dist
                if truth:
                    pre_set.add(f_prod_node)
                    self.add_edge(f_prod_node, accept_node, weight=total_weight)
        return pre_set

    def fly_successors(self, f_prod_node):
        f_ts_node, f_buchi_node = self.projection(f_prod_node)
        # been visited before, and hasn't changed 
        if ((self.nodes[f_prod_node]['marker'] == 'visited') and 
            (self.graph['ts'].graph['region'].nodes[
                self.graph['ts'].nodes[self.nodes[f_prod_node]['ts']]['region']]['status'] == 'confirmed')):
            for t_prod_node in self.successors(f_prod_node):
                yield t_prod_node, self.edge[f_prod_node][t_prod_node]['weight']
        else:
            to_remove = self.out_edges(f_prod_node)
            self.remove_edges_from(to_remove)
            for t_ts_node,cost in self.graph['ts'].fly_successors(f_ts_node):
                for t_buchi_node in self.graph['buchi'].successors(f_buchi_node):
                    t_prod_node = self.composition(t_ts_node, t_buchi_node)
                    label = self.graph['ts'].nodes[f_ts_node]['label']
                    truth, dist = check_label_for_buchi_edge(self.graph['buchi'], label, f_buchi_node, t_buchi_node)
                    total_weight = cost + self.graph['beta']*dist
                    if truth:
                        self.add_edge(f_prod_node, t_prod_node, weight=total_weight)
                        yield t_prod_node, total_weight
            self.nodes[f_prod_node]['marker'] = 'visited'

    #------------------------------------
    # Get possible states from previous
    # possible set and a given TS state 
    #------------------------------------
    def get_possible_states(self, ts_node):
        new_reachable = set()
        # Go through each product state in possible states
        for f_s in self.possible_states:
            # Go through all connected states and if TS states match, add it to the list
            for t_s in self.successors(f_s):
                if t_s[0] == ts_node:
                    new_reachable.add(t_s)
        return new_reachable
