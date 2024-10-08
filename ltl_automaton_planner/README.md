# ltl_automaton_planner

## Overview
An LTL (Linear Temporal Logic) planner implementation based on LTL2BA and LTL automata. Takes as input a set of action models to build a transition system, and a LTL formula (with hard and soft components).

A non-deterministic state graph, called product graph, is generated from the product of the Buchi automaton and the action model. This product graph is used to track possible agent state and generate a plan (output word) and action sequence (input word) for the agent.

For more information, please take a look at the [wiki](../../../wiki)

## Config files
- **example_ltl_formula.yaml** Example of LTL formula with both hard and soft task.

- **example_ts.yaml** Example of LTL transition system definition.

## Launch files
- **ltl_planner.launch**: Run the LTL planner node. Need a transition system definition text parameter and a LTL formula parameter.
    - `initial_ts_state_from_agent` If false, get initial TS (Transition System) state from the TS definition text parameter. If true, get initial TS state from agent topic. Default: `true`.

- **ltl_planner_example.launch**: Example of the LTL planner implementation. Run the planner node with an example TS (Transition System) and example LTL formula.
    - `initial_ts_state_from_agent` If false, get initial TS (Transition System) state from the TS definition text parameter. If true, get initial TS state from agent topic. Default: `true`.
    - `agent_name` Agent name. Default: `turtlebot`.

## Nodes
### planner_node.py
Planner node. Build a product graph from a given transition system and LTL formula. Uses the graph to generate a run and an action plan to follow to satisfy the formula. The planner keep track of possible states by receiving TS (Transition System) state from the agent and output action command to the agent.

#### Subscribed Topics
- `ts_state` ([ltl_automaton_msgs/TransitionSystemStateStamped](/ltl_automaton_msgs/msg/TransitionSystemStateStamped.msg))

    Agent TS state topic. The agent TS state is composed of a list of states from the different state models composing the action model. The planner node receives the agent TS state on this topic and update accordingly the next action and the set of possible states.

#### Published Topics
- `next_move_cmd` ([std_msgs/String](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/String.html))

    Next move from the output word (action sequence) to be carried out by the agent in order to satisfy the plan.

- `possible_ltl_states` ([ltl_automaton_msgs/LTLStateArray](/ltl_automaton_msgs/msg/LTLStateArray.msg))
    
    Current possible states of the agent, can be more than one as the system is non-deterministic. LTL states are composed of a TS (Transisition System) state and a Büchi state.

- `prefix_plan` ([ltl_automaton_msgs/LTLPlan](/ltl_automaton_msgs/msg/LTLPlan.msg))

    Prefix plan (also called prefix word), the action sequence to be carried out once by the agent after planning.

- `suffix_plan` ([ltl_automaton_msgs/LTLPlan](/ltl_automaton_msgs/msg/LTLPlan.msg))
    
    Suffix plan (also called suffix word), the action sequence to be carried out repeatively after the prefix plan.
    
#### Services

- `replanning` ([ltl_automaton_msgs/TaskPlanning](/ltl_automaton_msgs/srv/TaskPlanning.srv))
    
    Triggers planning to satisfy the requested hard and soft task.
    
#### LTL formula
For more information on LTL task formulation and syntax, please take a look at the [wiki page](../../../wiki/LTL-Formula)

#### Transition system definition
The final transition system is built from one or more action models. Those action models are also transition systems and their graph product is the final transition system.

As the final transition system, each individual action model transition system is discrete, finite, and can be deterministic or not. The input on each transition is an action that can be carried out by the agent.

More information about the transition system can be found in the corresponding [wiki page](../../../wiki/Transition-System-Definition)

#### Plugins
A plugin system allows for integrating more feature to the planner node (notably used by the Human-In-the-Loop mixed initiative controller). Details on the plugin can be found on the [wiki page](../../../wiki/Planner-Plugin)

