import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/maverick/LMCO/tmm-mas/sim/ROS2/install/ltl_automaton_planner'
