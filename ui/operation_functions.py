# operation_functions.py

import numpy as np
import pandas as pd

def generate_rmm_array_for_row(shmm_row, index):
    position_values = shmm_row[0]
    time_value = shmm_row[1]
    mission_time_value = shmm_row[2]

    position_noise = np.random.normal(0, 1)
    time_noise = np.random.normal(0, 3)

    position_value1 = int(np.round(np.abs(position_values[0] + position_noise)))
    position_value2 = int(np.round(np.abs(position_values[1] + np.random.normal(0, 0.1))))
    time_taken = round((np.abs(time_value + time_noise)), 2)
    mission_tim = int(mission_time_value)

    position_value1 = np.clip(position_value1, 0, 5)
    position_value2 = np.clip(position_value2, 0, 3)

    rmm_array = [index, position_value1, position_value2, time_taken, mission_tim]
    return rmm_array


def generate_hmm_arrays(input_file_path):
    # Read the input CSV file
    df = pd.read_csv(input_file_path, header=None)

    # Initialize lists to store the parsed data
    index = []
    position_x = []
    position_y = []
    time_taken = []
    steps_remaining = []

    # Parse the data
    for i, row in df.iterrows():
        pos = eval(row[0])  # Evaluate the position tuple (x, y)
        index.append(i + 1)  # Create index starting from 1
        position_x.append(pos[0])
        position_y.append(pos[1])
        time_taken.append(float(row[1]))
        steps_remaining.append(int(row[2]))

    # Create a DataFrame with the parsed data and rename it to SHMM
    SHMM = pd.DataFrame({
        'Index': index,
        'Position X': position_x,
        'Position Y': position_y,
        'Time Taken': time_taken,
        'Steps Remaining': steps_remaining
    })

    # Prepare SHMM data for RMM generation
    shmm_data = []
    for i, row in SHMM.iterrows():
        first_state = row['Position X']
        second_state = row['Position Y']
        time_elapsed = row['Time Taken']
        steps_remaining = row['Steps Remaining']
        mission_time = i + steps_remaining
        shmm_data.append(((first_state, second_state), time_elapsed, mission_time))

    # Prepare hmm_arrays in the desired format
    HMM_arrays = [[i, pose[0][0], pose[0][1], round(pose[1], 2), pose[2]] for i, pose in enumerate(shmm_data)]
    
    return HMM_arrays

def select_hmm_array(hmm_arrays, timestep):
    """
    Select a row of data from HMM_arrays based on the given timestep.

    Parameters:
    hmm_arrays (list): The HMM arrays generated from the input CSV file.
    timestep (int): The index value (1-based) for which to retrieve the corresponding row.

    Returns:
    list: The corresponding row of data from the HMM arrays, or None if not found.
    """
    # Adjust for 0-based index in Python
    index = timestep - 1
    
    # Check if the index is valid
    if 0 <= index < len(hmm_arrays):
        return hmm_arrays[index]
    else:
        return None  # Return None if the index is out of bounds

def calculate_l1_norm(array1, array2):
    norm = np.abs(np.array(array2) - np.array(array1))
    return norm

def bayesian_probabilistic_update_general(original_value, deviation, threshold, uncertainty_factor):
    expected_value = original_value + deviation
    updated_value = expected_value if abs(deviation) > threshold else original_value
    return updated_value

# Function to generate delay message based on scenario
def generate_delay_message(robot_number, X, Y, A, B, scenario=None):
    if scenario == "emergency_stop":
        message_template = (
            f"Commander, Robot {robot_number} has encountered an emergency situation "
            f"and has stopped abruptly at position {A}. Further assessment is required.\n"
        )
    elif scenario == "obstacle_detected":
        message_template = (
            f"Commander, Robot {robot_number} has detected an obstacle in its path and is navigating around it. "
            f"Current position: {A}.\n"
        )
    elif scenario == "low_battery":
        message_template = (
            f"Commander, Robot {robot_number}'s battery level is critically low. "
            f"It will pause its mission and return to base for recharging. Current position: {A}.\n"
        )
    elif scenario == "communication_failure":
        message_template = (
            f"Commander, Communication with Robot {robot_number} has been lost. "
            f"Please investigate the issue. Last known position: {A}.\n"
        )
    elif scenario == "sensor_malfunction":
        message_template = (
            f"Commander, Robot {robot_number} has experienced a sensor malfunction, affecting its navigation accuracy. "
            f"Current position: {A}.\n"
        )
    else:
        time_difference = Y - X
        position_difference = (B[0] - A[0], B[1] - A[1])

        message_template = f"Robot {robot_number}'s mission status update:\n"

        # Time-related message
        if time_difference > 0:
            time_message = (
                f"- Time Remaining: Estimated {X} seconds, Actual {Y} seconds\n"
                f"- Coordinates: Estimated {A}, Actual {B}\n"
                f"The robot is currently experiencing a delay of {time_difference} seconds. \n"
            )
        elif time_difference < 0:
            time_message = (
                f"- Estimated Time of Completion: {X} seconds\n"
                f"- Actual Time of Completion: {Y} seconds\n"
                f"- Expected Coordinates: {A}\n"
                f"- Actual Coordinates: {B}\n\n"
                f"The robot is ahead of schedule by {abs(time_difference)} seconds. \n"
            )
        else:
            time_message = (
                f"- Time Remaining: Estimated {X} seconds, Actual {Y} seconds\n"
                f"- Coordinates: Estimated {A}, Actual {B}\n"
                f"The robot is on schedule. \n"
            )

        # Position-related message
        position_message = f"It is now located at position {B}."
        if any(position_difference):
            position_message += f" It has moved {abs(position_difference[0])} units " \
                               f"to the {'right' if position_difference[0] > 0 else 'left'}"
            position_message += f" and {abs(position_difference[1])} units " \
                               f"{'upward' if position_difference[1] > 0 else 'downward'}" \
                               f" from the expected position ({A})."

        message_template += time_message + position_message 

    return message_template


def generate_communication_message(deviation, threshold, hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time):
    messages = []
    if abs(deviation) > threshold:
        robot_number = 1  # Assuming robot number 1 for example
        X = hmm_time
        Y = rmm_time
        A = (hmm_pos1, hmm_pos2)
        B = (rmm_pos1, rmm_pos2)
        delay_message = generate_delay_message(robot_number, X, Y, A, B)
        # print(delay_message)
        messages.append(delay_message)  # Append formatted delay message to messages list
        # print(messages)
    return messages


def dynamic_deviation_threshold_multi_logic(hmm_arrays, rmm_arrays, update_logic_functions, uncertainty_factor_pos,
                                            uncertainty_factor_time, dynamic_threshold_mission_time):
    updated_hmm_array = []
    current_hmm_mission_time = hmm_arrays[0][4]  # Initial mission time from the HMM array

    updated_pos1 = rmm_arrays[0][1]
    updated_pos2 = rmm_arrays[0][2]

    # Calculate mission time deviation
    mission_time_deviation = calculate_l1_norm([current_hmm_mission_time], [rmm_arrays[0][4]])
    mission_time_deviation_value = mission_time_deviation[0]

    hmm_pos1 = hmm_arrays[0][1]
    hmm_pos2 = hmm_arrays[0][2]
    rmm_pos1 = rmm_arrays[0][1]
    rmm_pos2 = rmm_arrays[0][2]
    hmm_time = hmm_arrays[0][3]
    rmm_time = rmm_arrays[0][3]

    # Generate communication message
    message = generate_communication_message(mission_time_deviation_value, dynamic_threshold_mission_time,
                                              hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time)
    formatted_message = "\n".join(message)

    # Update mission time using the first update logic function
    updated_mission_time = update_logic_functions[0](current_hmm_mission_time, mission_time_deviation_value,
                                                      dynamic_threshold_mission_time, uncertainty_factor_time)

    # Update the current_hmm_mission_time with the new updated_mission_time
    current_hmm_mission_time = updated_mission_time

    # Append updated values to updated_hmm_array
    updated_hmm_array.append([0, int(round(updated_pos1, 0)), int(round(updated_pos2, 0)), None, updated_mission_time])

    return updated_hmm_array, formatted_message

def bayesian_probabilistic_update_general(original_value, deviation, threshold, uncertainty_factor):
    expected_value = original_value + deviation
    updated_value = expected_value if abs(deviation) > threshold else original_value
    return updated_value


# operation_functions.py

def print_message(data):
    message = "I love chocolate"
    print(message)
    return message  # Return the message so it can be sent back to the client

# operation_functions.py
import random
import string

def process_data(data):
    # Generate random text
    random_length = random.randint(5, 15)  # Random length between 5 and 15
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=random_length))
    return random_text
