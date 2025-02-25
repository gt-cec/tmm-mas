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

app = Flask(__name__)
socketio = SocketIO(app)

# Global variables
# set mission time based on JSON, check it out, some 75-82
# last_mission_times = {1: 76, 2: 80, 3: 72}
last_mission_times = {
    "quad1": 76, 
    "quad2": 80, 
    "quad3": 72
}

index_value = 0  # Keeps track of timestep across multiple requests

previous_robot_states = {}
current_robot_states = {
    "robots": {
        str(robot_num): {
            "currentLocationPlan": [],
            "currentAbstractedPlan": []
        } for robot_num in range(1, 4)
    }
}
print("current_robot_states",current_robot_states)
initial_data = True

# Flag to ensure `generate_hmm_arrays` is only called for the first JSON received
first_json_received = False

index_value = 0
# List of expected robots (robot names)



@app.route("/receive_data", methods=["POST"])


@socketio.on("message")
def receive_data():
    global initial_data, current_robot_states
    global first_json_received  # Use the global flag
    global  index_value  # Track timestep globall
    global processed_hmm_arrays

    try:
        # Get the JSON data from the incoming request
        data = request.json
        # print(data)
        # print(len(data))
        JSON_data=data[0]
        # print("JSON_data",JSON_data)
        if not data:
            raise ValueError("No JSON data received")

        # Log the full incoming data for debugging (optional)
        # print("Received JSON Data:")
        # print(json.dumps(data, indent=4))

        # Check if 'robots' key is present
        if not isinstance(data, list):
            raise ValueError("Data should be a list of JSONs.")



        check_robot_data(JSON_data, expected_robots = ['quad1', 'quad2', 'quad3'])


        # Only call `generate_hmm_arrays` for the first JSON
        if not first_json_received:
            first_json_received = True
            # first_json = data
            # Call the generate_hmm_arrays function for the first JSON data
            processed_hmm_arrays=generate_hmm_arrays(JSON_data)
            print("✅ generate_hmm_arrays called for the first JSON.")
            # print(processed_hmm_arrays)

        
        # Process and print robot data for all robots
        if "robots" not in JSON_data:
            raise ValueError("Missing 'robots' key in JSON data.")



        dfs = extract_robot_data(JSON_data)
        print("dfs:", dfs)

        # Track active robots
        active_robots = {robot_id: len(dfs[robot_id]) > 0 for robot_id in dfs}
        print("Active Robots:", active_robots)


        tasks = {
            "Go to": ["objective A", "objective B", "objective C", "base"],
            "Acquire": ["package #1", "package #2", "package #3"],
            "Drop": ["package #1", "package #2", "package #3"]
        }
        plan_coordinates = []
        plans = []

        print(f"\n🚀 Processing the Received JSON data")

        current_index = index_value
        index_value+=1



        robot_states = {}

        for robot_id, robot_data in JSON_data["robots"].items():
            

            row = dfs[robot_id][0]  
            print("row:", row)                      # Convert the row to the expected format


            formatted_position = row["formatted_pos"]  # This is already a tuple (x, y)
            result = [
                current_index,  # timestep increment
                formatted_position[0],  # x-coordinate
                formatted_position[1],  # y-coordinate
                row["interval"],  # Time interval
                row["mission_time"]  # Mission time
            ]
            print("result:", result)



            robot_state = process(robot_id, result, tasks, plan_coordinates, plans,JSON_data)
            print("robot_state",robot_state)



            robot_number = int(robot_id.replace("quad", ""))
            robot_states[(robot_number)] = robot_state

    # Print HMM, RMM, and message details
            print(f"HMM Array for Robot {robot_id}: {robot_state['rmm_array']}")
            print(f"RMM Array for Robot {robot_id}: {robot_state['rmm_array']}")
            # print(f"Message for Robot {robot_id}: {robot_state['message']}")
            print("robot_states", robot_states)



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




            # # print(f"🔍 Checking robot_id: {robot_id}, row_index: {current_index}")
            # # print(f"🔍 Available robots: {list(processed_hmm_arrays.keys())}")
            # # if robot_id in processed_hmm_arrays:
            # #     print(f"🔍 {robot_id} has {len(processed_hmm_arrays[robot_id])} rows")



            # # print(f"🔍 Checking robot_id: {robot_id}, row_index: {current_index}")

            # hmm_array_data_preformat  =  select_hmm_row(processed_hmm_arrays,str(robot_id), int(current_index))
            # # print(f"HMM Array for Robot {robot_id}: {hmm_array_data_preformat}")

            # hmm_array_data = hmm_array_reformat(hmm_array_data_preformat)
            # # print(f"HMM Array for Robot {robot_id}: {hmm_array_data }")



            # # Create the hmm_array with the necessary values
            # hmm_array = [
            #     int(current_index),  # First value: the current index (converted to int)
            #     float(hmm_array_data[0][0]),  # Second value: hmm_array_data[1] (converted to float)
            #     float(hmm_array_data[0][1]),  # Third value: hmm_array_data[2] (converted to float)
            #     round(float(hmm_array_data[1]), 4),  # Fourth value: rounding hmm_array_data[3] (converted to float)
            #     int(last_mission_times[str(robot_id)])  # Fifth value: mission time for the robot ID
            # ]

            # # # Print the relevant values
            # # print(f"Current index: {int(current_index)}")
            # # print(f"hmm_array_data[1]: {float(hmm_array_data[0][0])}")
            # # print(f"hmm_array_data[2]: {float(hmm_array_data[0][1])}")
            # # print(f"Rounded hmm_array_data[3]: {round(float(hmm_array_data[2]), 4)}")
            # # print(f"last_mission_times for {robot_id}: {int(last_mission_times[str(robot_id)])}")

            # # Print the final hmm_array
            # print(f"HMM Array for Robot {robot_id}: {hmm_array}")




            # rmm_array_create = create_rmm_array(JSON_data, str(robot_id))
            # print(f"RMM Array for Robot prior to reformat {robot_id}: {rmm_array_create}")

            # # shmm_row = ((x, y), time_elapsed, timestep + steps_remaining)
            # # rmm_process = generate_rmm_array_for_row(shmm_row, timestep)

            # # Create the rmm_array with the necessary values
            # rmm_array = [
            #     int(current_index),  # First value: the current index (converted to int)
            #     float(rmm_array_create[0][0]),  # Second value: hmm_array_data[1] (converted to float)
            #     float(rmm_array_create[0][1]),  # Third value: hmm_array_data[2] (converted to float)
            #     round(float(rmm_array_create[1]), 4),  # Fourth value: rounding hmm_array_data[3] (converted to float)
            #     int(rmm_array_create[2])
            # ]
            # print(f"RMM Array for Robot {robot_id}: {rmm_array}")


            # hmm_array = [
            #     float(current_index),
            #     float(hmm_array_data[1]),
            #     float(hmm_array_data[2]),
            #     round(float(hmm_array_data[3]), 2),
            #     int(last_mission_times[robot_id])
            # ]
            
            # hmm_array = [
            #     int(current_index),
            #     float(hmm_array_data[1]),
            #     float(hmm_array_data[2]),
            #     round(float(hmm_array_data[3]), 2),
            #     int(last_mission_times[str(robot_id)])
            # ]
                    
            # # print(f"Current index: {int(current_index)}")
            # # print(f"hmm_array_data[1]: {float(hmm_array_data[0][1])}")
            # # print(f"hmm_array_data[2]: {float(hmm_array_data[0][2])}")
            # # print(f"Rounded hmm_array_data[3]: {float(hmm_array_data[2] )}")
            # # print(f"last_mission_times for {robot_id}: {int(last_mission_times[str(robot_id)])}")
            

            # print(f"Current index: {int(current_index)}")

            # print(f"hmm_array_data[1]: {float(hmm_array_data[0][0])}")
            # print(f"hmm_array_data[2]: {float(hmm_array_data[0][1])}")


            # print(f"Rounded hmm_array_data[3]: {round(float(hmm_array_data[2]), 4)}")
            # print(f"last_mission_times for {robot_id}: {int(last_mission_times[str(robot_id)])}")
            



            # print(f"HMM Array for Robot {robot_id}: {int(last_mission_times[str(robot_id)])}")



    #         robot_state = process(robot_id, result, tasks, plan_coordinates, plans)

    #         robot_states[str(robot_id)] = robot_state


    # # Print HMM, RMM, and message details
    #         print(f"HMM Array for Robot {robot_id}: {robot_state['hm m_array']}")
    #         print(f"RMM Array for Robot {robot_id}: {robot_state['rmm_array']}")
    #         print(f"Message for Robot {robot_id}: {robot_state['message']}")







#           #uncomment stuff below for testing.
            # print(f"\n🚀 JSON Data Received")
            # # for robot_id, robot_data in JSON_data["robots"].items():



            # print(f"\n🚀 Data Received (Robot ID: {robot_id}):")
            # print(f"📅 Simulation Time: {JSON_data.get('simulator time', 'N/A')}s")
            # print(f"📍 Current Position: (x: {robot_data['x'][0]}, y: {robot_data['y'][1]})")
            # print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")


            socketio.sleep(2)  # Simulate processing delay


        # return jsonify({"message": "All data received successfully!"}), 200

    # except Exception as e:
    #     # Return the error in JSON format if something goes wrong
    #     print(f"❌ Error: {e}")
    #     return jsonify({"message": "Failed to process data", "error": str(e)}), 500






        # if robot_states:
        #     previous_robot_states = current_robot_states
        #     current_robot_states = {
        #         "initial": initial_data,
        #         "timestamp": time.time(),
        #         "robots": robot_states,
        #         "objectives": [
        #             {"name": "A", "x": 2, "y": 3},
        #             {"name": "B", "x": 7, "y": 9},
        #             {"name": "C", "x": 9, "y": 2}
        #         ]
        #     }

        #     # Emit the updated state to the client
        #     socketio.emit("message", current_robot_states)
        #     initial_data = False

        # socketio.sleep(2)  # Simulate processing delay









def process(robot_id, data, tasks, plan_coordinates, plans, JSON_data):
    global last_mission_times

    # print("robot_id",robot_id)
    current_index, x, y, time_elapsed, steps_remaining = data
    # print("timestep",timestep)
    # print("processed_hmm_arrays", processed_hmm_arrays)

    # # Debugging: Check processed_hmm_arrays structure
    # if robot_id not in processed_hmm_arrays:
    #     print(f"❌ {robot_id} not found in processed_hmm_arrays")
    # else:
    #     print(f"Processing robot {robot_id} at timestep {timestep}")




    # print(f"🔍 Checking robot_id: {robot_id}, row_index: {current_index}")
    # print(f"🔍 Available robots: {list(processed_hmm_arrays.keys())}")
    # if robot_id in processed_hmm_arrays:
    #     print(f"🔍 {robot_id} has {len(processed_hmm_arrays[robot_id])} rows")



    # print(f"🔍 Checking robot_id: {robot_id}, row_index: {current_index}")

    hmm_array_data_preformat  =  select_hmm_row(processed_hmm_arrays,str(robot_id), int(current_index))
    # print(f"HMM Array for Robot {robot_id}: {hmm_array_data_preformat}")

    hmm_array_data = hmm_array_reformat(hmm_array_data_preformat)
    # print(f"HMM Array for Robot {robot_id}: {hmm_array_data }")



    # Create the hmm_array with the necessary values
    hmm_array = [
        int(current_index),  # First value: the current index (converted to int)
        float(hmm_array_data[0][0]),  # Second value: hmm_array_data[1] (converted to float)
        float(hmm_array_data[0][1]),  # Third value: hmm_array_data[2] (converted to float)
        round(float(hmm_array_data[1]), 4),  # Fourth value: rounding hmm_array_data[3] (converted to float)
        int(last_mission_times[str(robot_id)])  # Fifth value: mission time for the robot ID
    ]

    # # Print the relevant values
    # print(f"Current index: {int(current_index)}")
    # print(f"hmm_array_data[1]: {float(hmm_array_data[0][0])}")
    # print(f"hmm_array_data[2]: {float(hmm_array_data[0][1])}")
    # print(f"Rounded hmm_array_data[3]: {round(float(hmm_array_data[2]), 4)}")
    # print(f"last_mission_times for {robot_id}: {int(last_mission_times[str(robot_id)])}")

    # Print the final hmm_array
    # print(f"HMM Array for Robot {robot_id}: {hmm_array}")




    rmm_array_create = create_rmm_array(JSON_data, str(robot_id))
    # print(f"RMM Array for Robot prior to reformat {robot_id}: {rmm_array_create}")

    # shmm_row = ((x, y), time_elapsed, timestep + steps_remaining)
    # rmm_process = generate_rmm_array_for_row(shmm_row, timestep)

    # Create the rmm_array with the necessary values
    rmm_array = [
        int(current_index),  # First value: the current index (converted to int)
        float(rmm_array_create[0][0]),  # Second value: hmm_array_data[1] (converted to float)
        float(rmm_array_create[0][1]),  # Third value: hmm_array_data[2] (converted to float)
        round(float(rmm_array_create[1]), 4),  # Fourth value: rounding hmm_array_data[3] (converted to float)
        int(rmm_array_create[2])
    ]
    # print(f"RMM Array for Robot {robot_id}: {rmm_array}")



    update_logic_functions = [bayesian_probabilistic_update_general]
    uncertainty_factor_pos = 0.05
    uncertainty_factor_time = 0.01

    updated_hmm_array, message = dynamic_deviation_threshold_multi_logic(
        [hmm_array], [rmm_array], update_logic_functions, uncertainty_factor_pos, uncertainty_factor_time,
        dynamic_threshold_mission_time=10, robot_id=robot_id)

    print("updated_hmm_array",updated_hmm_array)
    print(f"Message for Robot {robot_id}: {message}")



    last_mission_times[str(robot_id)] = updated_hmm_array[0][4]


    robot_number = int(robot_id.replace("quad", ""))



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
        "previousLocationPlan": current_robot_states["robots"][str(robot_number)]["currentLocationPlan"],
        "initialPlan": [[2, 4], [3, 4], [3, 5], [4, 5]],
        "currentAbstractedPlan": robotPlanAbstract,
        "previousAbstractedPlan": current_robot_states["robots"][str(robot_number)]["currentAbstractedPlan"],
        "message": message
    }







@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5211)















