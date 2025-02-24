


from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from multirobot_operation_functions import (
    generate_rmm_array_for_row, 
    dynamic_deviation_threshold_multi_logic, 
    bayesian_probabilistic_update_general,
    select_hmm_array, 
    generate_hmm_arrays
)
import pandas as pd
import random
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Global variables
# set mission time based on JSON, check it out, some 75-82
last_mission_times = {1: 51, 2: 49, 3: 47}
input_file_paths = {
    1: 'formatted_robot1.csv',
    2: 'formatted_robot2.csv',
    3: 'formatted_robot3.csv'
}

hmm_arrays = {robot_id: generate_hmm_arrays(input_file_paths[robot_id]) for robot_id in range(1, 4)}
previous_robot_states = {}
current_robot_states = {
    "robots": {
        str(robot_id): {
            "currentLocationPlan": [],
            "currentAbstractedPlan": []
        } for robot_id in range(1, 4)
    }
}
initial_data = True


@socketio.on("message")
def play_recorded(data):
    global initial_data, current_robot_states
    print("Received message to start processing:", data)
    if data:
        dfs = {robot_id: pd.read_csv(input_file_paths[robot_id], header=None) for robot_id in range(1, 4)}
        # print(dfs)
        active_robots = {robot_id: True for robot_id in dfs}  # Tracking active robots

        i = 0  
        while any(active_robots.values()):  # Continue as long as any robot is active
            tasks = {
                "Go to": ["objective A", "objective B", "objective C", "base"],
                "Acquire": ["package #1", "package #2", "package #3"],
                "Drop": ["package #1", "package #2", "package #3"]
            }
            plan_coordinates = []
            plans = []



#change code below

            robot_states = {}

            for robot_id in range(1, 4):
                if active_robots[robot_id]:  # Only processing active robots
                    if i < len(dfs[robot_id]):  # Checking if the more data rows exist
                        print(f"Processing timestep {i + 1} for Robot {robot_id}...")
                        row = dfs[robot_id].iloc[i]
                        print("row",row)                    
                        result = [i + 1, eval(row[0])[0], eval(row[0])[1], float(row[1]), int(row[2])]
                        print("result",result)

                        robot_state = process(robot_id, result, tasks, plan_coordinates, plans)
                        robot_states[str(robot_id)] = robot_state




#change code above










                        # Print HMM, RMM, and message details
                        print(f"HMM Array for Robot {robot_id}: {robot_state['rmm_array']}")
                        print(f"RMM Array for Robot {robot_id}: {robot_state['rmm_array']}")
                        print(f"Message for Robot {robot_id}: {robot_state['message']}")
                    else:
                        # Mark this robot as inactive
                        active_robots[robot_id] = False
                        print(f"Robot {robot_id} has finished processing all rows.")

            if robot_states:
                previous_robot_states = current_robot_states
                current_robot_states = {
                    "initial": initial_data,
                    "timestamp": time.time(),
                    "robots": robot_states,
                    "objectives": [
                        {"name": "A", "x": 2, "y": 3},
                        {"name": "B", "x": 7, "y": 9},
                        {"name": "C", "x": 9, "y": 2}
                    ]
                }

                # Emit the updated state to the client
                socketio.emit("message", current_robot_states)
                initial_data = False

            socketio.sleep(2)  # Simulate processing delay
            i += 1  # Increment the row index for all robots



#change code below


def process(robot_id, data, tasks, plan_coordinates, plans):
    global last_mission_times

    timestep, x, y, time_elapsed, steps_remaining = data
    hmm_array_data = select_hmm_array(hmm_arrays[robot_id], timestep)

    hmm_array = [
        float(hmm_array_data[0]),
        float(hmm_array_data[1]),
        float(hmm_array_data[2]),
        round(float(hmm_array_data[3]), 2),
        int(last_mission_times[robot_id])
    ]

    shmm_row = ((x, y), time_elapsed, timestep + steps_remaining)
    rmm_process = generate_rmm_array_for_row(shmm_row, timestep)
    rmm_array = [
        float(rmm_process[0]),
        float(rmm_process[1]),
        float(rmm_process[2]),
        round(float(rmm_process[3]), 2),
        int(rmm_process[4])
    ]

    update_logic_functions = [bayesian_probabilistic_update_general]
    uncertainty_factor_pos = 0.05
    uncertainty_factor_time = 0.01

    updated_hmm_array, message = dynamic_deviation_threshold_multi_logic(
        [hmm_array], [rmm_array], update_logic_functions, uncertainty_factor_pos, uncertainty_factor_time,
        dynamic_threshold_mission_time=10, robot_number=robot_id
    )

    last_mission_times[robot_id] = updated_hmm_array[0][4]



#change code above







    # Generate plans
    x = random.randint(3, 7)
    y = random.randint(3, 7)
    plan = [[x, y]]
    last_loc = [x, y]
    for _ in range(steps_remaining):
        new_loc = [last_loc[0] + random.randint(-1, 1), last_loc[1] + random.randint(-1, 1)]
        last_loc = new_loc
        plan.append(new_loc)
    plan_coordinates.append(plan)

    robotPlanAbstract = []
    for _ in range(random.randint(0, 5)):
        task = random.choice(list(tasks.keys()))
        obj = random.choice(tasks[task])
        robotPlanAbstract.append(f"{task} {obj}")
    plans.append(robotPlanAbstract)

    return {
        "rmm_array": rmm_array,
        "x": plan[0][0],
        "y": plan[0][1],
        "robotPath": [[1, 0], [0, 0], [plan[0][0], plan[0][1]]],
        "completedPlan": ["Go to objective A", "Pick up package #1"],
        "currentLocationPlan": plan,
        "previousLocationPlan": current_robot_states["robots"][str(robot_id)]["currentLocationPlan"],
        "initialPlan": [[2, 4], [3, 4], [3, 5], [4, 5]],
        "currentAbstractedPlan": robotPlanAbstract,
        "previousAbstractedPlan": current_robot_states["robots"][str(robot_id)]["currentAbstractedPlan"],
        "message": message
    }







@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=8080)
