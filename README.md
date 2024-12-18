## Team Mental Models for Multi-Agent Systems

This project looks at how an autonomous multi-agent system can intelligently decide when to inform a human operator of changes to the mission plan. The objective is for the system to identify when the robot's plan outcomes have substantially changed from what the robot believes the human thinks the outcomes will be, and appropriately update the user.

As a toy problem, we consider a grid world where a single robot agent must navigate from one corner of the grid to the other. As the robot moves, obstacles regularly spawn and force the robot to replan, which changes its estimated mission time. If the mission time changes enough, the robot updates the human controller of the new time. This demonstration shows a simulation rollout and the resulting "mental models".

In future work, we plan to extend this system to more complex multi-agent domains.

### Proof of Concept Demo

We have a quick-and-dirty proof-of-concept that ignores the UI and simulator to generate an agent navigating through a grid world and identifying which points the user is communicated to. The scripts used for this are `rollout_simulation.py` and `plot_sim_results.py`.

To generate a simulation rollout:

`$ python rollout_simulation.py`

The results of the rollout will be saved to `robot_data_1.csv`, and an MP4 video of the rollout will be saved to `robot_animation.mp4`. To generate a plot of the mental models, run:

`$ python plot_sim_results.py`

The resulting plot shows the robot's estimate of the mission time at each simulation timestep, and the estimated human mental model due to the robot updating the human when the two models sufficiently diverge.

### UI Interface

We use Python and the Flask-SocketIO webserver to organize plan information from robots in an IsaacSim simulator and stream it to a web-based UI.

(As of Dec 18 2024) The simulator / replanner and webserver have not been integrated yet. The webserver includes a demo generator (random plans that are mostly nonsensical) for testing.

1. Start the server.

```
cd ui
python server.py
```

2. Open the webpage in your browser, you will see the user interface and a map image centered.

`http://localhost:8080`

3. (Demo plans) Click the "Play" button to start the demo plan, the script generates a plan and waits a few seconds before sending each step. Change this sleep time in `server.py->play_recorded()`.

### To Do

There are a few things needed:

1. Integration of replanner with IsaacSim.

2. Integration of replanner or IsaacSim with the webserver.

3. Improving the UI, both visually and by useful functionality.
