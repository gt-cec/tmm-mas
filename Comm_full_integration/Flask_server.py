
# # flask_server.py
# from flask import Flask, request, jsonify
# from operation_functions import (
#     generate_rmm_array_for_row, 
#     dynamic_deviation_threshold_multi_logic, 
#     bayesian_probabilistic_update_general,
#     select_hmm_array, generate_hmm_arrays
# )
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # Global variable to hold the last mission time
# last_mission_time = 37  # Start with the initial value
# input_file_path = 'robot_data_10 1.csv'
# hmm_arrays = generate_hmm_arrays(input_file_path)



# @app.route('/process', methods=['POST'])
# def process():
#     global last_mission_time  # Use the global variable

#     # Get data from the JSON body
#     data_string = request.json.get('data')
#     dynamic_threshold = request.json.get('dynamic_threshold')  # Get slider position
    
#     print("Received data string:", data_string)
#     print("Received slider position:", dynamic_threshold)

#     # Define thresholds based on slider input
#     # low_dynamic_threshold_mission_time = 40 
#     # medium_dynamic_threshold_mission_time = 60 
#     # high_dynamic_threshold_mission_time = 70 
    
#     low_dynamic_threshold_mission_time = 10 # 11 stars # dataset low threshold high sensitivity 3
#     medium_dynamic_threshold_mission_time = 15 # 8 stars # dataset medium 2
#     high_dynamic_threshold_mission_time = 20 # 6 stars # dataset high threshold low sensitivity 1

    
#     if dynamic_threshold == 'low':
#         dynamic_threshold_mission_time = low_dynamic_threshold_mission_time
#     elif dynamic_threshold == 'medium':
#         dynamic_threshold_mission_time = medium_dynamic_threshold_mission_time
#     elif dynamic_threshold == 'high':
#         dynamic_threshold_mission_time = high_dynamic_threshold_mission_time

#     # Continue with processing
#     numbers = [float(num.strip().strip("'")) if '.' in num else int(num.strip().strip("'")) 
#                for num in data_string[1:-1].split(',')]
#     timestep = numbers[0] - 1
#     first_state = numbers[1]
#     second_state = numbers[2]
#     time_elapsed = numbers[3]
#     steps_remaining = numbers[4]
    
    
#     hmm_array_data=select_hmm_array(hmm_arrays, timestep)
    
#     hmm_array = [ hmm_array_data[0], hmm_array_data[1],  hmm_array_data[2], round(hmm_array_data[3], 2), last_mission_time]     
    
#     # Initialize hmm_array with the last_mission_time instead of 37
#     rmm_array = [timestep, first_state, second_state, round(time_elapsed, 2), steps_remaining]
    
    
#     # shmm_row = ((first_state, second_state), time_elapsed, timestep + steps_remaining)
#     # rmm_array = generate_rmm_array_for_row(shmm_row, timestep)
    
    
#     print("HMM Array:", hmm_array)
#     print("RMM Array:", rmm_array)

#     uncertainty_factor_pos = 0.05
#     uncertainty_factor_time = 0.01

#     # Use the dynamic threshold from the slider input
#     update_logic_functions = [bayesian_probabilistic_update_general]

#     updated_hmm_array, message = dynamic_deviation_threshold_multi_logic(
#         [hmm_array], [rmm_array], update_logic_functions, uncertainty_factor_pos, uncertainty_factor_time,
#         dynamic_threshold_mission_time=dynamic_threshold_mission_time
#     )

#     # Update the last mission time with the updated value from updated_hmm_array
#     last_mission_time = updated_hmm_array[0][4]

#     print("Updated HMM Array:", updated_hmm_array)
#     print("Message:", message)
#     return jsonify(result=message, rmm_array=rmm_array)

#     # return jsonify(result=message)

# if __name__ == '__main__':
#     app.run(port=5000)
    
    
    
    
    
    
# # flask_server.py
# from flask import Flask, request, jsonify
# from operation_functions import (
#     generate_rmm_array_for_row, 
#     dynamic_deviation_threshold_multi_logic, 
#     bayesian_probabilistic_update_general,
#     select_hmm_array, generate_hmm_arrays
# )
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # Global variable to hold the last mission time
# last_mission_time = 37  # Start with the initial value
# input_file_path = 'robot_data_10 1.csv'
# hmm_arrays = generate_hmm_arrays(input_file_path)



# @app.route('/process', methods=['POST'])
# def process():
#     global last_mission_time  # Use the global variable

#     # Get data from the JSON body
#     data_string = request.json.get('data')
#     dynamic_threshold = request.json.get('dynamic_threshold')  # Get slider position
    
#     print("Received data string:", data_string)
#     print("Received slider position:", dynamic_threshold)

#     # Define thresholds based on slider input
#     # low_dynamic_threshold_mission_time = 40 
#     # medium_dynamic_threshold_mission_time = 60 
#     # high_dynamic_threshold_mission_time = 70 
    
#     low_dynamic_threshold_mission_time = 10 # 11 stars # dataset low threshold high sensitivity 3
#     medium_dynamic_threshold_mission_time = 15 # 8 stars # dataset medium 2
#     high_dynamic_threshold_mission_time = 20 # 6 stars # dataset high threshold low sensitivity 1

    
#     if dynamic_threshold == 'low':
#         dynamic_threshold_mission_time = low_dynamic_threshold_mission_time
#     elif dynamic_threshold == 'medium':
#         dynamic_threshold_mission_time = medium_dynamic_threshold_mission_time
#     elif dynamic_threshold == 'high':
#         dynamic_threshold_mission_time = high_dynamic_threshold_mission_time

#     # Continue with processing
#     numbers = [float(num.strip().strip("'")) if '.' in num else int(num.strip().strip("'")) 
#                for num in data_string[1:-1].split(',')]
#     timestep = numbers[0] 
#     first_state = numbers[1]
#     second_state = numbers[2]
#     time_elapsed = numbers[3]
#     steps_remaining = numbers[4]
    
    
#     hmm_array_data=select_hmm_array(hmm_arrays, timestep)
    
#     hmm_array = [ hmm_array_data[0], hmm_array_data[1],  hmm_array_data[2], round(hmm_array_data[3], 2), last_mission_time]     
    
#     # Initialize hmm_array with the last_mission_time instead of 37
#     rmm_array = [timestep -1, first_state, second_state, round(time_elapsed, 2), steps_remaining]
    
    
#     # shmm_row = ((first_state, second_state), time_elapsed, timestep + steps_remaining)
#     # rmm_array = generate_rmm_array_for_row(shmm_row, timestep)
    
    
#     print("HMM Array:", hmm_array)
#     print("RMM Array:", rmm_array)

#     uncertainty_factor_pos = 0.05
#     uncertainty_factor_time = 0.01

#     # Use the dynamic threshold from the slider input
#     update_logic_functions = [bayesian_probabilistic_update_general]

#     updated_hmm_array, message = dynamic_deviation_threshold_multi_logic(
#         [hmm_array], [rmm_array], update_logic_functions, uncertainty_factor_pos, uncertainty_factor_time,
#         dynamic_threshold_mission_time=dynamic_threshold_mission_time
#     )

#     # Update the last mission time with the updated value from updated_hmm_array
#     last_mission_time = updated_hmm_array[0][4]

#     print("Updated HMM Array:", updated_hmm_array)
#     print("Message:", message)
#     return jsonify(result=message, rmm_array= rmm_array, x=first_state, y=second_state)

#     # return jsonify(result=message)

# if __name__ == '__main__':
#     app.run(port=5000)
    
    
from flask import Flask, request, jsonify
from operation_functions import (
    generate_rmm_array_for_row, 
    dynamic_deviation_threshold_multi_logic, 
    bayesian_probabilistic_update_general,
    select_hmm_array, 
    generate_hmm_arrays
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Global variable to hold the last mission time
last_mission_time = 37  # Start with the initial value
input_file_path = 'robot_data_10 1.csv'
hmm_arrays = generate_hmm_arrays(input_file_path)

@app.route('/process', methods=['POST'])
def process():
    global last_mission_time  # Use the global variable

    # Get data from the JSON body
    data_string = request.json.get('data')
    dynamic_threshold = request.json.get('dynamic_threshold')  # Get slider position
    
    print("Received data string:", data_string)
    print("Received slider position:", dynamic_threshold)

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
    numbers = [float(num.strip().strip("'")) if '.' in num else int(num.strip().strip("'")) 
               for num in data_string[1:-1].split(',')]
    timestep = numbers[0] 
    first_state = numbers[1]
    second_state = numbers[2]
    time_elapsed = numbers[3]
    steps_remaining = numbers[4]
    
    hmm_array_data = select_hmm_array(hmm_arrays, timestep)
    hmm_array = [hmm_array_data[0], hmm_array_data[1], hmm_array_data[2], round(hmm_array_data[3], 2), last_mission_time]     
    rmm_array = [timestep - 1, first_state, second_state, round(time_elapsed, 2), steps_remaining]
    
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
    return jsonify(result=message, rmm_array=rmm_array, x=first_state, y=second_state)

@app.route('/reset', methods=['POST'])
def reset():
    global last_mission_time  # Use the global variable
    last_mission_time = 37  # Reset to initial value
    print("Server state has been reset.")
    return jsonify(result="Server state has been reset.")

if __name__ == '__main__':
    app.run(port=5000)
    
    
    
    
    
    
    
    