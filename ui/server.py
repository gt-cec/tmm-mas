from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO, emit
from operation_functions import (
    generate_rmm_array_for_row, 
    dynamic_deviation_threshold_multi_logic, 
    bayesian_probabilistic_update_general,
    select_hmm_array, 
    generate_hmm_arrays
)
import random
import pandas as pd

app = Flask(__name__)
socketio = SocketIO(app)

# Global variable to hold the last mission time
last_mission_time = 37  # Start with the initial value
input_file_path = 'robot_data_10 1.csv'
# input_file_path = 'RMM.csv'
hmm_arrays = generate_hmm_arrays(input_file_path)

@socketio.on("message")
def play_recorded(data):
    print("Received message:", data)
    if data == True:
        df = pd.read_csv(input_file_path, header=None)
        # Process and send each row dynamically
        for i, row in df.iterrows():
            # Process each row (transform the data)
            pos = eval(row[0])  # Evaluate the position tuple (x, y)
            index = i + 1  # Create index starting from 1
            position_x = pos[0]
            position_y = pos[1]
            time_taken = float(row[1])
            steps_remaining = int(row[2])
            plan = [[position_x, position_y]]

            last_loc = [position_x, position_y]
            for i in range(steps_remaining):
                new_loc = [last_loc[0] + random.randint(-1, 1), last_loc[1] + random.randint(-1, 1)]
                last_loc = new_loc
                plan.append(new_loc)
            
            # Prepare the processed data as a list of strings
            result = [
                index,
                position_x,
                position_y,
                time_taken,
                steps_remaining,
                plan
            ]
            
            # Send the processed data to the client as a string
            socketio.send(process(result))
            # Add a small delay to allow client to process data
            socketio.sleep(1)  # Wait for 0.5 seconds before sending the next message

        # After sending all rows, stop further communication
        print("Finished sending all data to client")
    return

def process(data):
    global last_mission_time  # Use the global variable

    dynamic_threshold = "low"

    # Define thresholds based on slider input
    low_dynamic_threshold_mission_time = 10 
    medium_dynamic_threshold_mission_time = 15 
    high_dynamic_threshold_mission_time = 20 

    if dynamic_threshold == 'low':
        dynamic_threshold_mission_time = low_dynamic_threshold_mission_time
    elif dynamic_threshold == 'medium':
        dynamic_threshold_mission_time = medium_dynamic_threshold_mission_time
    elif dynamic_threshold == 'high':
        dynamic_threshold_mission_time = high_dynamic_threshold_mission_time

    # Continue with processing
    timestep = data[0] 
    x = data[1]
    y = data[2]
    time_elapsed = data[3]
    steps_remaining = data[4]
    plan = data[5]
    
    hmm_array_data = select_hmm_array(hmm_arrays, timestep)
    hmm_array = [hmm_array_data[0], hmm_array_data[1], hmm_array_data[2], round(hmm_array_data[3], 2), last_mission_time]     
    rmm_array = [timestep - 1, x, y, round(time_elapsed, 2), steps_remaining]
    
    print("HMM Array:", hmm_array)
    print("RMM Array:", rmm_array)

    uncertainty_factor_pos = 0.05
    uncertainty_factor_time = 0.01

    # Use the dynamic threshold from the slider input
    update_logic_functions = [bayesian_probabilistic_update_general]

    updated_hmm_array, message = dynamic_deviation_threshold_multi_logic(
        [hmm_array], [rmm_array], update_logic_functions, uncertainty_factor_pos, uncertainty_factor_time,
        dynamic_threshold_mission_time=dynamic_threshold_mission_time
    )

    # Update the last mission time with the updated value from updated_hmm_array
    last_mission_time = updated_hmm_array[0][4]

    print("Updated HMM Array:", updated_hmm_array)
    print("Message:", message)
    return {
        "result": message,
        "robots": {
            "1": {
                "rmm_array": rmm_array,
                "x": x,
                "y": y,
                "robotPath": [[1,0], [0,0], [y,x]],
                "plan": plan,
                "colorPath": "red",
                "colorPlan": "darkred"
            },
            "2": {
                "rmm_array": rmm_array,
                "x": y,
                "y": x,
                "robotPath": [[0,0], [0,1], [x,y]],
                "plan": plan,
                "colorPath": "blue",
                "colorPlan": "darkblue"
            }
        }
    }

@app.route('/reset', methods=['POST'])
def reset():
    global last_mission_time  # Use the global variable
    last_mission_time = 37  # Reset to initial value
    print("Server state has been reset.")
    return jsonify(result="Server state has been reset.")

# pull the index page
@app.route('/')
def index():
    return render_template('index.html')

# start the server
if __name__ == '__main__':
    socketio.run(app, port=5001)
