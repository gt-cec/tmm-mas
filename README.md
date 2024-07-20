## Team Mental Models for Multi-Agent Systems

This project looks at how an autonomous multi-agent system can intelligently decide when to inform a human operator of changes to the mission plan. The objective is for the system to identify when the robot's plan outcomes have substantially changed from what the robot believes the human thinks the outcomes will be, and appropriately update the user.

As a toy problem, we consider a grid world where a single robot agent must navigate from one corner of the grid to the other. As the robot moves, obstacles regularly spawn and force the robot to replan, which changes its estimated mission time. If the mission time changes enough, the robot updates the human controller of the new time. This demonstration shows a simulation rollout and the resulting "mental models".

In future work, we plan to extend this system to more complex multi-agent domains.

### Running the code

A simplified demonstration of the capabilities use `rollout_simulation.py` and `plot_sim_results.py`.

To generate a simulation rollout:

`$ python rollout_simulation.py`

The results of the rollout will be saved to `robot_data_1.csv`, and an MP4 video of the rollout will be saved to `robot_animation.mp4`. To generate a plot of the mental models, run:

`$ python plot_sim_results.py`

The resulting plot shows the robot's estimate of the mission time at each simulation timestep, and the estimated human mental model due to the robot updating the human when the two models sufficiently diverge.

### UI Interface

I made a template UI interface in the `ui/` folder, which can be used as a baseline upon which to create a visualization for the simulator.

To run the example:

1. Start the server.

```
cd ui
python server.py
```

2. Open the webpage in your browser, you will see an empty blue rectangle.

`http://localhost:5000`

3. In another terminal, send the image.

```
cd ui
python send_image.py
```

4. Check the webpage, you will see the CEC logo. The `send_image.py` script sent the image to the server, which emitted it to the webpage. In practice, you can use a script like `send_image.py` to pull from the simulator and send to the server, or you can use the server script to pull from the simulator. 