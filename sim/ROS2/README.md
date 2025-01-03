# ROS Communication
Communication between the LTL-D* planner and the Isaac Sim simulation ocurrs via ROS2. The planner has been tested on both Foxy Fitzroy and Humble Hawksbill and the simulation has only been tested on Humble Hawksbill. Note that Isaac Sim support for ROS2 Foxy is deprecated and may not work with this simulation, however this has not been tested. 

The `interfaces_hmm_sim` package is associated with the Isaac Sim simulation while the packages found in the `ltl_planner` directory are associated with the LTL-D* planner.

## Dependencies
For the dependencies for the LTL-D* planner, see the README in the `ltl_planner` directory. While not listed as a dependency, `pygame` may need to be installed for the LTL-D* planner to work. Use `pip install pygame` to resolve this. 

The `interfaces_hmm_sim` package does not have any additional dependencies.

## Workspace Setup
To run all of the code a ROS2 workspace needs to be setup. This can either be a normal ROS2 workspaces or one of the ROS workspace provided by Isaac Sim on their [GitHub](https://github.com/isaac-sim/IsaacSim-ros_workspaces). If the Isaac Sim simulation is not needed or the Isaac Sim ROS2 bridge is being run via Fast DDS instead of via a ROS2 workspace, it is better to just use a normal ROS2 workspace. The instructions to setup a ROS2 workspace can be found [here for Humble](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) and [here for Foxy](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html). While it shouldn't cause issues, it is recommended to place the files in this folder into the ROS2 workspace `src` directory separately from the rest of the simulation code if you are running it with Isaac Sim.

Once the files have been placed into your `src` folder open a terminal run the following to build the packages to build the packages.
```
cd <workspace_folder>
colcon build
source install/local_setup.bash
```
You can also add the following to your `.bashrc` or other shell config file so that the workspace does not need to be sourced in each new terminal manually:
```
source ~/<workspace_folder>/install/local_setup.bash
```

Your final workspace directory will look something like this after building the project:
```
workspace_folder/
    build/
    install/
    log/
    src/
      interfaces_hmm_sim/
      lmco/
            ltl_automaton_msgs/
            ltl_automaton_planner/
```

## File Paths
Some paths in the LTL-D* planner packages have been hardcoded for now and need to be changed. I have listed files and the line numbers here:
* `multiagent-sim/ROS2/ltl_planner/ltl_automaton_planner/launch/ltl_planner_isaac_launch.py`, line 18
* `multiagent-sim/ROS2/ltl_planner/ltl_automaton_planner/ltl_automaton_planner/benchmark_node.py`, line 65
* `multiagent-sim/ROS2/ltl_planner/ltl_automaton_planner/ltl_automaton_planner/benchmark_node.py`, 516
* `multiagent-sim/ROS2/ltl_planner/ltl_automaton_planner/ltl_automaton_planner/nodes/benchmark_node.py`, line 64
* `multiagent-sim/ROS2/ltl_planner/ltl_automaton_planner/ltl_automaton_planner/nodes/benchmark_node.py`, line 414
* `multiagent-sim/ROS2/ltl_planner/ltl_automaton_planner/ltl_automaton_planner/nodes/simulation_node.py`, line 61

Make sure to rebuild with `colcon build` and source `local_install.bash` if these changes are made after already building the packages.

## Launching Files
To launch the LTL-D* planner open a terminal and run the following:
```
ros2 launch ltl_automaton_planner ltl_planner_isaac_launch.py
```

The 'interfaces_hmm_sim' package is associated with the Isaac Sim simulation and does not have a separate launch file. 
