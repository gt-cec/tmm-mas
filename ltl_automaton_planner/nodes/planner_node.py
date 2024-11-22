#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt

from ltl_automaton_planner.ltl_tools.ts import TSModel
from ltl_automaton_planner.ltl_tools.ltl_planner import LTLPlanner

#import matplotlib.pyplot as plt
import networkx as nx
from ltl_automaton_planner.ltl_automaton_utilities import state_models_from_ts, import_ts_from_file, handle_ts_state_msg, extract_numbers

# Import LTL automaton message definitions
from ltl_automaton_msgs.msg import TransitionSystemState, LTLPlan, LTLState, LTLStateArray
from ltl_automaton_msgs.srv import * #TaskPlanning, TaskPlanningResponse, TaskReplanningAdd, TaskReplanningDelete, TaskReplanningRelabel, TaskReplanningAddResponse, TaskReplanningDeleteResponse

import time

def show_automaton(automaton_graph):
    pos=nx.spring_layout(automaton_graph)
    nx.draw(automaton_graph, pos)
    nx.draw_networkx_labels(automaton_graph, pos)
    edge_labels = nx.get_edge_attributes(automaton_graph, 'guard')
    nx.draw_networkx_edge_labels(automaton_graph, pos, edge_labels = edge_labels)
    plt.show()
    return

class MainPlanner(object):
    def __init__(self):
        # init parameters, automaton, etc...
        self.init_params()

        self.build_automaton()

        self.setup_pub_sub()

        time.sleep(1)
        self.publish_plan()
        rate = rospy.Rate(1)
        print("here")
        while not rospy.is_shutdown():
            #self.prefix_plan_pub.publish(self.prefix_plan_msg)
            #self.suffix_plan_pub.publish(self.suffix_plan_msg)
            # self.publish_plan()
            rate.sleep()
       

    def init_params(self):
        #Get parameters from parameter server
        self.agent_name = rospy.get_param('agent_name', "agent")
        self.initial_beta = rospy.get_param('initial_beta', 1000)
        self.gamma = rospy.get_param('gamma', 10)

        # Get LTL hard task and raise error if don't exist
        if (rospy.has_param('hard_task')):
            self.hard_task = rospy.get_param('hard_task')
        else:
            raise ValueError("Cannot initialize LTL planner, no hard_task defined")
        # Get LTL soft task
        self.soft_task = rospy.get_param('soft_task', "")

        # Transition system
        transition_system_textfile = rospy.get_param('transition_system_textfile')
        self.transition_system = import_ts_from_file(transition_system_textfile)
        
        self.algo_type = rospy.get_param('~algo_type', "dstar")
        self.grid_size = rospy.get_param('~N', 10)
        print(self.grid_size)
        self.initial_state_ts_dict = None

    
    def build_automaton(self):
        # Import state models from TS
        state_models = state_models_from_ts(self.transition_system, self.initial_state_ts_dict)
     
        # Here we take the product of each element of state_models to define the full TS
        self.robot_model = TSModel(state_models)
        self.ltl_planner = LTLPlanner(self.robot_model, self.hard_task, self.soft_task, self.initial_beta, self.gamma)
        self.ltl_planner.optimal(algo=self.algo_type, N=self.grid_size)
        # Get first value from set
        self.ltl_planner.curr_ts_state = list(self.ltl_planner.product.graph['ts'].graph['initial'])[0]

        # initialize storage of set of possible runs in product
        self.ltl_planner.posb_runs = set([(n,) for n in self.ltl_planner.product.graph['initial']])

        #show_automaton(self.robot_model)
        #show_automaton(self.ltl_planner.product.graph['buchi'])
        #show_automaton(self.ltl_planner.product)


    def setup_pub_sub(self):
        # Prefix plan publisher
        self.prefix_plan_pub = rospy.Publisher('/prefix_plan', LTLPlan, queue_size = 1)

        # Suffix plan publisher
        self.suffix_plan_pub = rospy.Publisher('/suffix_plan', LTLPlan, queue_size = 1)

        # Initialize task replanning service for ADD
        self.replan_srv_add = rospy.Service('replanning_mod', TaskReplanningModify, self.replanning_modify_callback)
        
        # Initialize task replanning service for DELETE
        self.replan_srv_delete = rospy.Service('replanning_delete', TaskReplanningDelete, self.replanning_delete_callback)
        
        # Initialize task replanning service for RELABEL
        self.replan_srv_relabel = rospy.Service('replanning_relabel', TaskReplanningRelabel, self.replanning_relabel_callback)
        
    #----------------------------------------------
    # Publish prefix and suffix plans from planner
    #----------------------------------------------
    def publish_plan(self):
        # If plan exists
        if not (self.ltl_planner.run == None):
            # Prefix plan
            #-------------
            self.prefix_plan_msg = LTLPlan()
            self.prefix_plan_msg.header.stamp = rospy.Time.now()
            self.prefix_plan_msg.action_sequence = self.ltl_planner.run.pre_plan
            self.prefix_plan_msg.ts_state_sequence = []
            # # Go through all TS state in plan and add it as TransitionSystemState message
            for ts_state in self.ltl_planner.run.line:
                ts_state_msg = TransitionSystemState()
                # ts_state_msg.state_dimension_names = self.ltl_planner.product.graph['ts'].graph['ts_state_format']
                # If TS state is more than 1 dimension (is a tuple)
                if type(ts_state) is tuple:
                    ts_state_msg.states = list(ts_state)
                # Else state is a single string
                else:
                    ts_state_msg.states = [ts_state]
                # Add to plan TS state sequence
                self.prefix_plan_msg.ts_state_sequence.append(ts_state_msg)

            # Publish
            rospy.loginfo("Publish Prefix Plan")
            # print(prefix_plan_msg.action_sequence)
            self.prefix_plan_pub.publish(self.prefix_plan_msg)

            # Suffix plan
            #-------------
            self.suffix_plan_msg = LTLPlan()
            self.suffix_plan_msg.header.stamp = rospy.Time.now()
            self.suffix_plan_msg.action_sequence = self.ltl_planner.run.suf_plan
            self.suffix_plan_msg.ts_state_sequence = []
            # # Go through all TS state in plan and add it as TransitionSystemState message
            for ts_state in self.ltl_planner.run.loop:
                ts_state_msg = TransitionSystemState()
                # ts_state_msg.state_dimension_names = self.ltl_planner.product.graph['ts'].graph['ts_state_format']
                # If TS state is more than 1 dimension (is a tuple)
                if type(ts_state) is tuple:
                    ts_state_msg.states = list(ts_state)
                # Else state is a single string
                else:
                    ts_state_msg.states = [ts_state]

                # Add to plan TS state sequence
                self.suffix_plan_msg.ts_state_sequence.append(ts_state_msg)

            # Publish
            rospy.loginfo("Publish Suffix Plan")
            self.suffix_plan_pub.publish(self.suffix_plan_msg)


    def replanning_modify_callback(self, task_replanning_req):
        if task_replanning_req:
            print("Replanning [modify] Callback")
            update_info = dict()
            update_info["modified"] = set()
            update_info["deleted"] = set()
            update_info["relabel"] = set()
            # TODO: check both delete_from and delete_to have only two elements
            # change position in tuple to ts node of the format ('c0_r5', 'unloaded')
            for node in self.ltl_planner.product.graph['ts'].nodes():
                if tuple(task_replanning_req.mod_from) == extract_numbers(node[0]):
                    for succ_node in self.ltl_planner.product.graph['ts'].successors(node):
                        if tuple(task_replanning_req.mod_to) == extract_numbers(succ_node[0]):
                            update_info["modified"].add((node, succ_node, task_replanning_req.cost))
                if tuple(task_replanning_req.mod_to) == extract_numbers(node[0]):
                    for succ_node in self.ltl_planner.product.graph['ts'].successors(node):
                        if tuple(task_replanning_req.mod_from) == extract_numbers(succ_node[0]):
                            update_info["modified"].add((node, succ_node, task_replanning_req.cost))
            # print(update_info["modified"])
            modified_edges_dict = self.ltl_planner.revise_product(update_info)
            print("finished revise")
            
            success = False
            if self.algo_type == 'dstar' or self.algo_type =="dstar-relaxed":
                if self.ltl_planner.dstar_rewire(task_replanning_req.exec_index, modified_edges_dict, update_info):
                    success = True
            elif self.algo_type == 'local':
                if self.ltl_planner.local_rewire(task_replanning_req.exec_index):
                    success = True
            elif self.algo_type == 'brute-force' or self.algo_type == "relaxed":
                if self.ltl_planner.dijkstra_rewire(task_replanning_req.exec_index):
                    success = True
            
                
            if success:
                # print("new_prefix", self.ltl_planner.prefix)
                # print("new_suffix", self.ltl_planner.suffix)
                res = TaskReplanningModifyResponse()
                res.success = True
                res.new_plan_prefix = LTLPlan()
                res.new_plan_prefix.header.stamp = rospy.Time.now()
                res.new_plan_prefix.action_sequence = self.ltl_planner.run.pre_plan
                # # Go through all TS state in plan and add it as TransitionSystemState message
                for ts_state in self.ltl_planner.run.line:
                    ts_state_msg = TransitionSystemState()
                    # If TS state is more than 1 dimension (is a tuple)
                    if type(ts_state) is tuple:
                        ts_state_msg.states = list(ts_state)
                    # Else state is a single string
                    else:
                        ts_state_msg.states = [ts_state]
                    # Add to plan TS state sequence
                    res.new_plan_prefix.ts_state_sequence.append(ts_state_msg)
                    
                res.new_plan_suffix = LTLPlan()
                res.new_plan_suffix.header.stamp = rospy.Time.now()
                res.new_plan_suffix.action_sequence = self.ltl_planner.run.suf_plan
                # # Go through all TS state in plan and add it as TransitionSystemState message
                for ts_state in self.ltl_planner.run.loop:
                    ts_state_msg = TransitionSystemState()
                    # If TS state is more than 1 dimension (is a tuple)
                    if type(ts_state) is tuple:
                        ts_state_msg.states = list(ts_state)
                    # Else state is a single string
                    else:
                        ts_state_msg.states = [ts_state]
                    # Add to plan TS state sequence
                    res.new_plan_suffix.ts_state_sequence.append(ts_state_msg)
                return res
            
        rospy.logerr("Error!!!")
        
    def replanning_delete_callback(self, task_replanning_req):
        if task_replanning_req:
            print("Replanning [Delete] Callback")
            update_info = dict()
            update_info["modified"] = set()
            update_info["deleted"] = set()
            update_info["relabel"] = set()
            # TODO: check both delete_from and delete_to have only two elements
            # change position in tuple to ts node of the format ('c0_r5', 'unloaded')
            for node in self.ltl_planner.product.graph['ts'].nodes():
                if tuple(task_replanning_req.delete_from) == extract_numbers(node[0]):
                    for succ_node in self.ltl_planner.product.graph['ts'].successors(node):
                        if tuple(task_replanning_req.delete_to) == extract_numbers(succ_node[0]):
                            update_info["deleted"].add((node, succ_node))
                if tuple(task_replanning_req.delete_to) == extract_numbers(node[0]):
                    for succ_node in self.ltl_planner.product.graph['ts'].successors(node):
                        if tuple(task_replanning_req.delete_from) == extract_numbers(succ_node[0]):
                            update_info["deleted"].add((node, succ_node))
            # print(update_info["deleted"])
            modified_edges_dict = self.ltl_planner.revise_product(update_info)
            print("finished revise")
            
            success = False
            if self.algo_type == 'dstar' or self.algo_type =="dstar-relaxed":
                if self.ltl_planner.dstar_rewire(task_replanning_req.exec_index, modified_edges_dict, update_info):
                    success = True
            elif self.algo_type == 'local':
                if self.ltl_planner.local_rewire(task_replanning_req.exec_index):
                    success = True
            elif self.algo_type == 'brute-force' or self.algo_type == "relaxed":
                if self.ltl_planner.dijkstra_rewire(task_replanning_req.exec_index):
                    success = True
                
            if success:
                # print("new_prefix", self.ltl_planner.prefix)
                # print("new_suffix", self.ltl_planner.suffix)
                res = TaskReplanningDeleteResponse()
                res.success = True
                res.new_plan_prefix = LTLPlan()
                res.new_plan_prefix.header.stamp = rospy.Time.now()
                res.new_plan_prefix.action_sequence = self.ltl_planner.run.pre_plan
                # # Go through all TS state in plan and add it as TransitionSystemState message
                for ts_state in self.ltl_planner.run.line:
                    ts_state_msg = TransitionSystemState()
                    # If TS state is more than 1 dimension (is a tuple)
                    if type(ts_state) is tuple:
                        ts_state_msg.states = list(ts_state)
                    # Else state is a single string
                    else:
                        ts_state_msg.states = [ts_state]
                    # Add to plan TS state sequence
                    res.new_plan_prefix.ts_state_sequence.append(ts_state_msg)
                    
                res.new_plan_suffix = LTLPlan()
                res.new_plan_suffix.header.stamp = rospy.Time.now()
                res.new_plan_suffix.action_sequence = self.ltl_planner.run.suf_plan
                # # Go through all TS state in plan and add it as TransitionSystemState message
                for ts_state in self.ltl_planner.run.loop:
                    ts_state_msg = TransitionSystemState()
                    # If TS state is more than 1 dimension (is a tuple)
                    if type(ts_state) is tuple:
                        ts_state_msg.states = list(ts_state)
                    # Else state is a single string
                    else:
                        ts_state_msg.states = [ts_state]
                    # Add to plan TS state sequence
                    res.new_plan_suffix.ts_state_sequence.append(ts_state_msg)
                return res
            
        rospy.logerr("Error!!!")
    
    def replanning_relabel_callback(self):
        pass

    
    # #-------------------------
    # # Publish possible states
    # #-------------------------
    # def publish_possible_states(self):
    #     # Create message
    #     possible_states_msg = LTLStateArray()
    #     # For all possible state, add to the message list
    #     for ltl_state in self.ltl_planner.product.possible_states:
    #         ltl_state_msg = LTLState()
    #         # If TS state is more than 1 dimension (is a tuple)
    #         if type(ltl_state[0]) is tuple:
    #             ltl_state_msg.ts_state.states = list(ltl_state[0])
    #         # Else state is a single string
    #         else:
    #             ltl_state_msg.ts_state.states = [ltl_state[0]]

    #         ltl_state_msg.ts_state.state_dimension_names = self.ltl_planner.product.graph['ts'].graph['ts_state_format']
    #         ltl_state_msg.buchi_state = str(ltl_state[1])
    #         possible_states_msg.ltl_states.append(ltl_state_msg)

    #     # Publish
    #     self.possible_states_pub.publish(possible_states_msg)
#==============================
#             Main
#==============================
if __name__ == '__main__':
    rospy.init_node('ltl_planner', anonymous=False)
    try:
        ltl_planner_node = MainPlanner()
        rospy.spin()
    except ValueError as e:
        rospy.logerr("LTL Planner: "+str(e))
        rospy.logerr("LTL Planner: shutting down...")
