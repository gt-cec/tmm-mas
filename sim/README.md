# LTL-D* Isaac Sim Visualization
This repository contains the files required to visualize the drone simulation example for the LTL-D* algorithm.
Link to paper: https://doi.org/10.48550/arXiv.2404.01219 (Citation to be added)

The simulation was written for Isaac Sim 2023.1.1 and has been lightly tested in Isaac Sim 4.2.0. Bugs may exist if used in Isaac Sim 4.2.0.

## Usage
Place all files in the same directory and run as an Isaac Sim standalone example. In the code file paths should be changed in the `User Inputs` section. Please make sure that a quadcopter USD exists at the path `/World/quadx` with this name scheme inside the environment USD as this is how this simple example finds the quadcopter in the world to move. An XForm named `trace` most also exist in the USD at the path `/World/trace` if trace is enabled. Trace can be enabled/disabled in the `User Inputs` section as well. If Isaac Sim is having trouble finding any of the files, they may need to be changed from relative file paths to exact file paths. 

Difficult terrain (or bumps) need to be added directly in the code in the form of ordered pairs `(y,x)`. All coordinates represent the center point of squares in a grid world. Bumps designate locations where the drone must go to a higher elevation to overcome obstacles and only three vertical points are defined: the starting position on the ground, the standard cruising height, and the increased elevation to avoid bumps.

Only simple PID control is implemented at this moment and a path plan should be provided to the quadcopter. For an example of what path plan coordinates should look like, reference `grid.csv` and `coords_final.csv`. While the drone motion is somewhat simulated, this example is primarily for visualization of the proposed algorithm. For the algorithm used to generate the path plan found in `coords_final.csv`, please contact Jiming Ren (jren313@gatech.edu)

The environment USD file referenced in this example is too large to be uploaded to GitHub and can be found at the following link: [Environment USDs]([https://gtvault-my.sharepoint.com/:u:/g/personal/hmiller43_gatech_edu/Ed6wUSYb7UVHnxqCYqqqpQUBMMfWg0RtWXO7g1M0Osqr3g?e=ya8spc](https://gtvault-my.sharepoint.com/:f:/g/personal/hmiller43_gatech_edu/EiXSVUZyHghKi__9jqqyTwMBl0gtiv0T9s5Oy3fTkMTuDQ?e=eYURR2))

### Controls
The following keyboard inputs can be used once the simulation window has been fully loaded:
* P - Start/Stop the sim
* R - Reset the sim (It is recommended to stop the sim before resetting)
* X - Close the sim

## Contact
For any questions or comments, please contact  Haris Miller (harismiller@gatech.edu).
