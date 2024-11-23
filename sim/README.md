# LTL-D* Isaac Sim Visualization
This repository contains the files required to visualize the drone simulation example for the LTL-D* algorithm.
Link to paper: https://doi.org/10.48550/arXiv.2404.01219 (Citation to be added)

This simulation was built with Isaac Sim 4.2.0 and ROS2 Humble Hawksbill on Ubuntu 22.04 Jammy Jellyfish.

## Usage
### ROS2 Setup
Isaac Sim uses it's own compiled version of ROS2 Humble through FastDDS. The method for setting up the ROS2 bridge for Isaac Sim can be found here: [ROS2 Bridge Setup](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_ros.html#isaac-sim-app-enable-ros). The `interfaces_hmm_sim` package also needs to be built in a ROS2 workspace. Place this folder in the `src` folder of a ROS2 Workspace and use the command `colcon build --packages-select interfaces_hmm_sim` to build it. Make sure to source both ROS2 Humble and this workspace in any terminal used to run the standalone example.

### Isaac Sim Standalone Example
Place all other files in the same directory and run as an Isaac Sim standalone example. This is done by running the python.sh file for the version of Isaac Sim being used. Assuming Isaac Sim is installed to the default directory on Linux, it is recommended to add the following alias to your .bashrc or other shell environment file to make running standalone environments easier.
```
alias isaac_python='/home/<USER>/.local/share/ov/pkg/isaac-sim-4.2.0/python.sh'
```
Make sure to replace `<USER>` with your own system user or the whole path if Isaac Sim was installed to a different location. From here navigate to the directory where `standalone-multiagent.py` is located and run the following command to run the simulation.
```
isaac_python standalone-multiagent.py
```
If you did not create the above alias, you will instead have to use the full path to the python.sh file to run the example. 

**Note: It can take a while to load the full environment, especially if it is quite large. Unless the terminal says that Isaac Sim has crashed, it is recommended to wait a bit for Isaac Sim to load, even if says that it is not responding. The example environment provided takes ~1 to 5 minutes to load depending on the PC specs used to load it. If it takes longer than 10 minutes to load, there may be a problem with the environment USD file or standalone example code.** 

In the standalone example code, most of what might need to be changed can be found in the `User Inputs` section.
```
##### User Inputs #####

## File Paths

key_path = "./example/grid.csv" #File describing the world grid
coord_path = "./example/coords_final.csv" #File describing the path plan
usd_path = "./Small_Enviornment-Multiagent.usd" #File with the world enfironment

## Isaac Sim Paths

quad_path1 = "/World/quads/quad1" #Path to drone in the environment USD
quad_path2 = "/World/quads/quad2"
quad_path3 = "/World/quads/quad3"
quad_path4 = "/World/quads/quad4"

quad_path_list = [quad_path1, quad_path2, quad_path3, quad_path4]

## Define Bumps

bumps = [(3,1),(4,1),(5,2),(5,3),(2,4),(3,4)] #Difficult terrain points as list of ordered pairs: (y,x)
```

Because of how the standalone example initializes using the python.sh, all file paths should be absolute paths for now. 

Please make sure that a quadcopter USD exists at the path `/World/quadx` with this name scheme inside the environment USD as this is how this simple example finds the quadcopter in the world to move.

Difficult terrain (or bumps) need to be added directly in the code in the form of ordered pairs `(y,x)`. All coordinates represent the center point of squares in a grid world. Bumps designate locations where the drone must go to a higher elevation to overcome obstacles and only three vertical points are defined: the starting position on the ground, the standard cruising height, and the increased elevation to avoid bumps.

Only simple PID control is implemented at this moment and a path plan should be provided to the quadcopter. For an example of what path plan coordinates should look like, reference `grid.csv` and `coords_final.csv`. While the drone motion is somewhat simulated, this example is primarily for visualization of the proposed algorithm. For the algorithm used to generate the path plan found in `coords_final.csv`, please contact Jiming Ren (jren313@gatech.edu)

The environment USD file referenced in this example is too large to be uploaded to GitHub and can be found at the following link: [Environment USDs](https://gtvault-my.sharepoint.com/:f:/g/personal/hmiller43_gatech_edu/EiXSVUZyHghKi__9jqqyTwMBl0gtiv0T9s5Oy3fTkMTuDQ?e=raiM9h)

### Controls
The following keyboard inputs can be used once the simulation window has been fully loaded:
* P - Start/Stop the sim
* X - Close the sim

## Contact
For any questions or comments, please contact  Haris Miller (harismiller@gatech.edu).
