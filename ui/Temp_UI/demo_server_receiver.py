
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from multirobot_operation_functions import (
    generate_hmm_arrays, 
    select_hmm_row,
    hmm_array_reformat,
    create_rmm_array,
    dynamic_deviation_threshold_multi_logic,
    bayesian_probabilistic_update_general,
    extract_robot_data,
    check_robot_data
)
import pandas as pd
import random
import time
import json
import numpy as np
import copy

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow CORS for UI connections

# Global variables
last_mission_times = {
    "quad1": 76, 
    "quad2": 80, 
    "quad3": 72
}

index_value = 0  # Keeps track of timestep across multiple requests
previous_robot_states = {
    "robots": {
        "1": {
            "currentLocationPlan": [],
            "currentAbstractedPlan": []
        },
        "2": {
            "currentLocationPlan": [],
            "currentAbstractedPlan": []
        },
        "3": {
            "currentLocationPlan": [],
            "currentAbstractedPlan": []
        }
    }
}
current_robot_states = {
    "initial": True,
    "timestamp": time.time(),
    "robots": {
        "1": {
            "robot_id": "quad1",
            "currentLocationPlan": [],
            "currentAbstractedPlan": [],
            "previousAbstractedPlan": []
        },
        "2": {
            "robot_id": "quad2",
            "currentLocationPlan": [],
            "currentAbstractedPlan": [],
            "previousAbstractedPlan": []
        },
        "3": {
            "robot_id": "quad3",
            "currentLocationPlan": [],
            "currentAbstractedPlan": [],
            "previousAbstractedPlan": []
        }
    },
    "objectives": [
        {"name": "A", "x": 2, "y": 3},
        {"name": "B", "x": 7, "y": 9},
        {"name": "C", "x": 9, "y": 2}
    ]
}
initial_data = True
first_json_received = False
is_playing = False  # Play/Stop control

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/receive_data", methods=["POST"])
def receive_data():
    global initial_data, current_robot_states, previous_robot_states, first_json_received, index_value, processed_hmm_arrays

    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    JSON_data = data[0]
    check_robot_data(JSON_data, expected_robots=["quad1", "quad2", "quad3"])

    if not first_json_received:
        first_json_received = True
        processed_hmm_arrays = generate_hmm_arrays(JSON_data)
        print("✅ generate_hmm_arrays called for the first JSON.")

    if "robots" not in JSON_data:
        return jsonify({"error": "Missing 'robots' key in JSON data."}), 400

    dfs = extract_robot_data(JSON_data)
    active_robots = {robot_id: len(dfs[robot_id]) > 0 for robot_id in dfs}

    tasks = {
        "Go to": ["objective A", "objective B", "objective C", "base"],
        "Acquire": ["package #1", "package #2", "package #3"],
        "Drop": ["package #1", "package #2", "package #3"]
    }

    print("\n🚀 Processing the Received JSON data")
    current_index = index_value
    index_value += 1
    
    # Deep copy the current state to previous state
    previous_robot_states = copy.deepcopy(current_robot_states)
    
    robot_states = {}
    plan_coordinates = []
    plans = []
    
    for robot_id, robot_data in JSON_data["robots"].items():
        # Skip if no data for this robot
        if robot_id not in dfs or len(dfs[robot_id]) == 0:
            continue
            
        row = dfs[robot_id][0]
        formatted_position = row["formatted_pos"]
        result = [
            current_index,
            formatted_position[0],
            formatted_position[1],
            row["interval"],
            row["mission_time"]
        ]
        
        robot_number = robot_id.replace("quad", "")
        robot_state = process(robot_id, result, tasks, plan_coordinates, plans, JSON_data, robot_number)
        print(result[1], result[2])
        robot_states[robot_number] = robot_state

    if robot_states:
        # Update current_robot_states with new data
        updated_robot_states = {
            "initial": initial_data,
            "timestamp": time.time(),
            "robots": robot_states,
            "objectives": [
                {"name": "A", "x": 2, "y": 3},
                {"name": "B", "x": 7, "y": 9},
                {"name": "C", "x": 9, "y": 2}
            ]
        }
        current_robot_states = updated_robot_states
        
        # Emit the updated state to all connected clients
        print("Emitting updated state to clients")
        socketio.emit("message", current_robot_states)
        initial_data = False

    return jsonify({"message": "All data received successfully!"}), 200

@socketio.on("message")
def handle_play_stop(state):
    global is_playing
    is_playing = state
    print(f"🔄 Play/Stop received: {is_playing}")
    socketio.emit("message", is_playing)

@socketio.on("connect")
def handle_connect():
    print("Client connected")
    # Send the current state to the newly connected client
    socketio.emit("message", current_robot_states)

def process(robot_id, data, tasks, plan_coordinates, plans, JSON_data, robot_number):
    global last_mission_times
    global current_robot_states
    global previous_robot_states

    current_index, x, y, time_elapsed, steps_remaining = data

    jsonX = x + 1 # add 1 to x, since x = 0 is x at grid line 1 on the map
    jsonY = y + 1 # add 1 to y, since y = 0 is y at grid line 1 on the map

    hmm_array_data_preformat = select_hmm_row(processed_hmm_arrays, str(robot_id), int(current_index))
    hmm_array_data = hmm_array_reformat(hmm_array_data_preformat)

    hmm_array = [
        int(current_index),
        float(hmm_array_data[0][0]),
        float(hmm_array_data[0][1]),
        round(float(hmm_array_data[1]), 4),
        int(last_mission_times[str(robot_id)])
    ]

    rmm_array_create = create_rmm_array(JSON_data, str(robot_id))
    rmm_array = [
        int(current_index),
        float(rmm_array_create[0][0]),
        float(rmm_array_create[0][1]),
        round(float(rmm_array_create[1]), 4),
        int(rmm_array_create[2])
    ]

    update_logic_functions = [bayesian_probabilistic_update_general]
    uncertainty_factor_pos = 0.05
    uncertainty_factor_time = 0.01

    updated_hmm_array, message = dynamic_deviation_threshold_multi_logic(
        [hmm_array], [rmm_array], update_logic_functions, uncertainty_factor_pos, uncertainty_factor_time,
        dynamic_threshold_mission_time=10, robot_id=robot_id)

    print(f"HMM Array for Robot {robot_id}: {hmm_array}")
    print(f"RMM Array for Robot {robot_id}: {rmm_array}")
    print("updated_hmm_array", updated_hmm_array)
    print(f"Message for Robot {robot_id}: {message}")

    last_mission_times[str(robot_id)] = updated_hmm_array[0][4]
    print("last_mission_times", last_mission_times)

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

    # Abstract the plan from the JSON data
    robot_data = JSON_data["robots"][robot_id]
    current_abstracted_plan = abstract_plan(robot_data)
    
    # Get previous plans - make sure we're accessing the correct robot number
    previous_location_plan = []
    previous_abstracted_plan = []
    
    if robot_number in previous_robot_states["robots"]:
        previous_location_plan = previous_robot_states["robots"][robot_number].get("currentLocationPlan", [])
        previous_abstracted_plan = previous_robot_states["robots"][robot_number].get("currentAbstractedPlan", [])
    
    print(f"previous_abstracted_plan for {robot_id}", previous_abstracted_plan)
    print(f"current_abstracted_plan for {robot_id}", current_abstracted_plan)

    # Return the robot state with the correct robot ID
    return {
        "robot_id": robot_id,
        "rmm_array": rmm_array,
        "jsonX": jsonX,
        "jsonY": jsonY,
        "x": plan[0][0],
        "y": plan[0][1],
        "robotPath": [[1, 0], [0, 0], [plan[0][0], plan[0][1]]],
        "completedPlan": ["Go to objective A", "Pick up package #1"],
        "currentLocationPlan": plan,
        "previousLocationPlan": previous_location_plan,
        "initialPlan": [[2, 4], [3, 4], [3, 5], [4, 5]],
        "currentAbstractedPlan": current_abstracted_plan,
        "previousAbstractedPlan": previous_abstracted_plan,
        "message": message
    }

def abstract_plan(robot_data):
    """
    Abstract the plan information from the robot data.
    """
    abstracted_plan = []
    plan = robot_data.get("plan", [])
    immediate_goal = robot_data.get("immediate_goal", [])
    mission_time = robot_data.get("mission_time", 0)
    replan_flag = robot_data.get("replan_flag", False)

    if plan:
        # Get the final goal position from the plan
        final_goal = plan[-1]
        abstracted_plan.append(f"Go to ({final_goal[0]}, {final_goal[1]})")

        # Add direction information
        if len(plan) > 1:
            current_pos = plan[0]
            next_pos = plan[1]
            direction = get_direction(current_pos, next_pos)
            abstracted_plan.append(f"Direction: {direction}")

        if replan_flag:
            abstracted_plan.append("Replanning occurred")
        abstracted_plan.append(f"Mission time: {mission_time}")

    return abstracted_plan

def get_direction(current_pos, next_pos):
    """
    Determine the direction based on current and next positions.
    """
    dx = next_pos[0] - current_pos[0]
    dy = next_pos[1] - current_pos[1]

    if dx > 0:
        return "East"
    elif dx < 0:
        return "West"
    elif dy > 0:
        return "North"
    elif dy < 0:
        return "South"
    else:
        return "Stationary"

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5211)