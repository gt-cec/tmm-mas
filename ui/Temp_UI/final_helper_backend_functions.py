# operation_functions.py

import numpy as np
import pandas as pd

import ollama

import re

def extract_robot_data(data):
    if "simulator time" not in data or "robots" not in data:
        print("❌ Invalid data format!")
        return None

    simulator_time = data["simulator time"]
    dfs = {}

    for robot_id, robot_info in data["robots"].items():
        x_val = robot_info["x"]
        y_val = robot_info["y"]
        mission_time = robot_info["mission_time"]

        formatted_pos = f"({x_val}, {y_val})"
        pos_match = re.findall(r"-?\d+", formatted_pos)
        formatted_position = tuple(map(int, pos_match)) if pos_match else (None, None)

        dfs[robot_id] = [
            {
                "index": 0,
                "formatted_pos": formatted_position,
                "robot_time": simulator_time,
                "mission_time": mission_time
            }
        ]

    return dfs


# import re

# def extract_robot_data(data):
#     """
#     Extracts (x[0], y[1]), simulator time, and mission time for all robots.

#     :param data: Raw JSON data.
#     :return: Dictionary with data formatted like previous dfs.
#     """
#     if "simulator time" not in data or "robots" not in data:
#         print("❌ Invalid data format!")
#         return None

#     simulator_time = data["simulator time"]
#     dfs = {}

#     # Process each robot
#     for robot_id, robot_info in data["robots"].items():
#         x_val = robot_info["x"][0] if len(robot_info["x"]) > 0 else None
#         y_val = robot_info["y"][1] if len(robot_info["y"]) > 1 else None
#         mission_time = robot_info["mission_time"]

#         # Format position correctly using regex extraction
#         formatted_pos = f"({x_val}, {y_val})"
#         pos_match = re.findall(r"-?\d+", formatted_pos)
#         formatted_position = tuple(map(int, pos_match)) if pos_match else (None, None)

#         # Store in a list of dicts (like rows in a DataFrame)
#         dfs[robot_id] = [
#             {
#                 "index": 0,  # Can be incremented over time if needed
#                 "formatted_pos": formatted_position,  # Now correctly formatted as (x, y)
#                 "robot_time": simulator_time,
#                 "mission_time": mission_time
#             }
#         ]

#     return dfs



def abstract_plan(robot_data):
    abstracted_plan = []
    plan = robot_data.get("plan", [])
    mission_time = robot_data.get("mission_time", 0)
    replan_flag = robot_data.get("replan_flag", False)

    if plan:
        final_goal = plan[-1]
        abstracted_plan.append(f"Go to ({final_goal[0]}, {final_goal[1]})")

        if len(plan) > 1:
            direction = get_direction(plan[0], plan[1])
            abstracted_plan.append(f"Direction: {direction}")

        if replan_flag:
            abstracted_plan.append("Replanning occurred")
        abstracted_plan.append(f"Mission time: {mission_time}")

    return abstracted_plan

def get_direction(current_pos, next_pos):
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


# def abstract_plan(robot_data):
#     """
#     Abstract the plan information from the robot data.
#     """
#     abstracted_plan = []
#     plan = robot_data.get("plan", [])
#     immediate_goal = robot_data.get("immediate_goal", [])
#     mission_time = robot_data.get("mission_time", 0)
#     replan_flag = robot_data.get("replan_flag", False)

#     if plan:
#         # Get the final goal position from the plan
#         final_goal = plan[-1]
#         abstracted_plan.append(f"Go to ({final_goal[0]}, {final_goal[1]})")

#         # Add direction information
#         if len(plan) > 1:
#             current_pos = plan[0]
#             next_pos = plan[1]
#             direction = get_direction(current_pos, next_pos)
#             abstracted_plan.append(f"Direction: {direction}")

#         if replan_flag:
#             abstracted_plan.append("Replanning occurred")
#         abstracted_plan.append(f"Mission time: {mission_time}")

#     return abstracted_plan

# def get_direction(current_pos, next_pos):
#     """
#     Determine the direction based on current and next positions.
#     """
#     dx = next_pos[0] - current_pos[0]
#     dy = next_pos[1] - current_pos[1]

#     if dx > 0:
#         return "East"
#     elif dx < 0:
#         return "West"
#     elif dy > 0:
#         return "North"
#     elif dy < 0:
#         return "South"
#     else:
#         return "Stationary"


# def generate_hmm_arrays(data):
#     """
#     Processes robot data from JSON and generates HMM arrays.

#     :param data: Raw JSON data.
#     :return: Dictionary containing processed data as generated_hmm_arrays.
#     """
#     if "simulator time" not in data or "robots" not in data:
#         print("❌ Invalid data format!")
#         return None

#     simulator_time = data["simulator time"]
#     generated_hmm_arrays = {}

#     # Process each robot
#     for robot_id, robot_info in data["robots"].items():
#         positions = robot_info["plan"]  # Use 'plan' as the positions

#         # Create processed data with formatted structure
#         generated_hmm_arrays[robot_id] = [
#             {
#                 "formatted_pos": f"({pos})", 
#                 "robot_time": simulator_time, 
#                 "mission_time": robot_info["mission_time"]
#             }
#             for pos in positions
#         ]

#     return generated_hmm_arrays



#time value redefined based on sim estimation.
def generate_hmm_arrays(data):
    """
    Processes robot data from JSON and generates HMM arrays with cumulative time intervals.

    :param data: Raw JSON data.
    :return: Dictionary containing processed data as generated_hmm_arrays.
    """
    if "simulator time" not in data or "robots" not in data:
        print("❌ Invalid data format!")
        return None

    total_time = 150.03103494644165
    generated_hmm_arrays = {}

    # Process each robot
    for robot_id, robot_info in data["robots"].items():
        positions = robot_info["plan"]
        num_positions = len(positions) if positions else 1  # Avoid division by zero
        time_step = total_time / num_positions  # Compute time difference between each position
        
        cumulative_time = 0  # Start from 0 and accumulate
        generated_hmm_arrays[robot_id] = []

        for pos in positions:
            cumulative_time += time_step  # Increment time by step size

            generated_hmm_arrays[robot_id].append({
                "formatted_pos": f"({pos[0]}, {pos[1]})", 
                "robot_time": round(cumulative_time, 4),  # Store rounded cumulative time
                "mission_time": robot_info["mission_time"]
            })

    return generated_hmm_arrays



def select_hmm_row(processed_data, robot_id, row_index):
    """
    Selects a specific row from processed robot data using the robot ID.

    :param processed_data: Dict containing processed robot data.
    :param robot_id: String robot ID (e.g., "quad1", "quad2").
    :param row_index: Index of the row to select.
    :return: The selected row dictionary or None if out of bounds or robot not found.
    """
    if robot_id not in processed_data:
        print(f"❌ Robot {robot_id} not found!")
        return None

    robot_data = processed_data[robot_id]

    # Check if the row_index is within the bounds of the data
    if row_index < 0 or row_index >= len(robot_data):
        print(f"❌ Row index {row_index} out of range for {robot_id}.")
        print(f"Robot data length: {len(robot_data)}")
        return None

    return robot_data[row_index]
    # return robot_data



def hmm_array_reformat(row_data):
    """
    Extracts and formats 'formatted_pos', 'robot_time', and 'mission_time' into an HMM array.

    :param row_data: The dictionary row containing robot data.
    :return: List containing formatted values for HMM processing.
    """
    if not row_data:
        print("❌ Invalid row data provided!")
        return None

    # Extract numbers from formatted_pos (convert from string to tuple)
    pos_match = re.findall(r"-?\d+", row_data["formatted_pos"])  
    formatted_position = tuple(map(int, pos_match)) if pos_match else (None, None)

    # Store in list
    hmm_array = [formatted_position, row_data["robot_time"], row_data["mission_time"]]

    return hmm_array





# def create_rmm_array(data, robot_id):
#     """
#     Extracts (x[0], y[1]), simulator time, and mission time for a given robot.

#     :param data: Raw JSON data.
#     :param robot_id: String ID of the robot (e.g., 'quad1', 'quad2', etc.).
#     :return: List containing [(x[0], y[1]), simulator_time, mission_time] as RMM array.
#     """
#     if "simulator time" not in data or "robots" not in data:
#         print("❌ Invalid data format!")
#         return None

#     if robot_id not in data["robots"]:
#         print(f"❌ Robot {robot_id} not found!")
#         return None

#     robot_info = data["robots"][robot_id]
#     simulator_time = data["simulator time"]

#     # Extract first values of x and y
#     # x_val = robot_info["x"][0] if len(robot_info["x"]) > 0 else None
#     # y_val = robot_info["y"][1] if len(robot_info["y"]) > 1 else None
#     # x_val = robot_info["x"][0] if len(robot_info["x"]) > 0 else None
#     # y_val = robot_info["y"][1] if len(robot_info["y"]) > 1 else None
#     x_val = robot_info["x"]
#     y_val = robot_info["y"]
#     mission_time = robot_info["mission_time"]

#     # Create RMM array
#     rmm_array = [(x_val, y_val), simulator_time, mission_time]

#     return rmm_array


def create_rmm_array(data, robot_id):
    """
    Extracts (x[0], y[1]), simulator time, and mission time for a given robot.

    :param data: Raw JSON data.
    :param robot_id: String ID of the robot (e.g., 'quad1', 'quad2', etc.).
    :return: List containing [(x[0], y[1]), simulator_time, mission_time] as RMM array.
    """
    if "simulator time" not in data or "robots" not in data:
        print("❌ Invalid data format!")
        return None

    if robot_id not in data["robots"]:
        print(f"❌ Robot {robot_id} not found!")
        return None

    robot_info = data["robots"][robot_id]
    simulator_time = data["simulator time"]

    # Extract first values of x and y
    x_val = robot_info["x"]
    y_val = robot_info["y"]

    # Extract mission_time and ensure it's not negative
    mission_time = robot_info["mission_time"]
    if mission_time < 0:
        mission_time = 0
        print(f"⚠️ Mission time for Robot {robot_id} was negative. Set to 0.")

    # Create RMM array
    rmm_array = [(x_val, y_val), simulator_time, mission_time]

    return rmm_array




# Function to check robot data for each new JSON batch
def check_robot_data(JSON_data, expected_robots):
    # Initialize a list to track missing robots
    missing_robots = []

    # Check if any robot data is missing or has completed its task
    for robot in expected_robots:
        if robot not in JSON_data['robots']:
            missing_robots.append(robot)
        elif 'mission_time' in JSON_data['robots'][robot] and JSON_data['robots'][robot]['mission_time'] <= 0:
            # raise ValueError(f"{robot} has completed its task.")
            print(f"{robot} has completed its task.")

    # If there are missing robots, raise an error
    if missing_robots:
        # raise ValueError(f"Missing robot data for: {', '.join(missing_robots)}")
        print(f"Missing robot data for: {', '.join(missing_robots)}")

    # If no missing robots and no completed tasks, proceed with the code
    else:
        print("All robots are present and have not completed their tasks.")


def calculate_l1_norm(array1, array2):
    # norm = np.abs(np.array(array2) - np.array(array1))
    norm = (np.array(array2) - np.array(array1))
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


def generate_communication_message(deviation, threshold, hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time, robot_number):
    messages = []
    if abs(deviation) > threshold:
        robot_number = robot_number  # Assuming robot number 1 for example
        X = hmm_time
        Y = rmm_time
        A = (hmm_pos1, hmm_pos2)
        B = (rmm_pos1, rmm_pos2)
        delay_message = generate_delay_message(robot_number, X, Y, A, B)
        # print(delay_message)
        messages.append(delay_message)  # Append formatted delay message to messages list
        # print(messages)
    return messages



# def generate_message_with_ollama(model, prompt):
#     """
#     Generate message using Ollama with specified model
#     """
#     try:
#         response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
#         return response['message']['content']
#     except Exception as e:
#         return f"Error with {model}: {str(e)}"




# def generate_communication_message_ollama(deviation, threshold, hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time, robot_number,JSON_data):
#     messages = []
#     if abs(deviation) > threshold:
#         robot_number = robot_number  # Assuming robot number 1 for example
#         X = hmm_time
#         Y = rmm_time
#         A = (hmm_pos1, hmm_pos2)
#         B = (rmm_pos1, rmm_pos2)
#         delay_message = generate_delay_message(robot_number, X, Y, A, B)
#         # print(delay_message)
#         messages.append(delay_message)  # Append formatted delay message to messages list
#         # print(messages)
#     return messages



# def generate_communication_message_ollama(deviation, threshold, hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time, robot_number, JSON_data):
#     messages = []
#     if abs(deviation) > threshold:
#         # Calculate position differences
#         pos_diff_x = rmm_pos1 - hmm_pos1
#         pos_diff_y = rmm_pos2 - hmm_pos2

#         # Determine movement direction
#         if pos_diff_x > 0:
#             direction = "East"
#         elif pos_diff_x < 0:
#             direction = "West"
#         elif pos_diff_y > 0:
#             direction = "North"
#         elif pos_diff_y < 0:
#             direction = "South"
#         else:
#             direction = "Stationary"

#         # Determine delay status
#         if rmm_time > hmm_time:
#             time_status = f"{rmm_time - hmm_time} seconds behind the expected time"
#         else:
#             time_status = f"{hmm_time - rmm_time} seconds ahead of schedule"

#         # Check replan flag
#         replan_flag = JSON_data.get('replan_flag', False)
#         replan_message = " It has undergone replanning and has a new plan." if replan_flag else ""

#         # Prepare prompt for LLM
#         prompt = f"Robot {robot_number} is {time_status}; it has moved {direction}.{replan_message}"

#         # Generate message using Ollama
#         try:
#             response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
#             llm_message = response['message']['content'].strip()
#         except Exception as e:
#             llm_message = f"Error generating message: {str(e)}"

#         messages.append(llm_message)
#     return messages




# def generate_delay_message_ollama(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos):
#     """
#     Generate a delay message using the Ollama model.
#     """
#     time_deviation = rmm_time - hmm_time
#     pos_deviation_x = rmm_pos[0] - hmm_pos[0]
#     pos_deviation_y = rmm_pos[1] - hmm_pos[1]

#     direction = ""
#     if pos_deviation_y > 0:
#         direction += "North"
#     elif pos_deviation_y < 0:
#         direction += "South"
#     if pos_deviation_x > 0:
#         direction += "East"
#     elif pos_deviation_x < 0:
#         direction += "West"

#     time_status = "ahead" if time_deviation < 0 else "behind"
#     time_diff = abs(time_deviation)

#     prompt = f"""
# You are an AI assistant generating short mission status updates.
# Analyze the mission data and return a concise, **2-3 line** report focusing only on key deviations:

# Robot {robot_number} is {time_diff} seconds {time_status} the expected time; it has moved {direction}.
# """
#     try:
#         response = ollama.chat(model='zephyr', messages=[{'role': 'user', 'content': prompt}])
#         return response['message']['content'].strip()
#     except Exception as e:
#         return f"Error generating message: {str(e)}"


# import ollama

# def generate_delay_message_ollama(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag):
#     """
#     Generate a delay message in a strict format without using Ollama.
#     """
#     time_deviation = rmm_time - hmm_time
#     pos_deviation_x = rmm_pos[0] - hmm_pos[0]
#     pos_deviation_y = rmm_pos[1] - hmm_pos[1]

#     direction = ""
#     if pos_deviation_y > 0:
#         direction += "North"
#     elif pos_deviation_y < 0:
#         direction += "South"
#     if pos_deviation_x > 0:
#         direction += "East"
#     elif pos_deviation_x < 0:
#         direction += "West"

#     time_status = "ahead" if time_deviation < 0 else "behind"
#     time_diff = abs(time_deviation)

#     # Construct the message in the desired format
#     message = f"Robot {robot_number} is {time_diff} seconds {time_status} the expected time; it has moved {direction}."
#     if replan_flag:
#         message += " It has undergone replanning and has a new plan."

#     return message

import ollama
#works fine


# def generate_delay_message_ollama(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag=False):
#     """
#     Generate a delay message with consistent formatting for robot status communication
#     using Mistral through Ollama.
    
#     Parameters:
#     - robot_number: The identifier for the robot
#     - hmm_time: Expected/planned time
#     - rmm_time: Actual time
#     - hmm_pos: Expected/planned position as tuple (x, y)
#     - rmm_pos: Actual position as tuple (x, y)
#     - replan_flag: Boolean indicating if replanning occurred
    
#     Returns:
#     - Formatted status message
#     """
#     # Calculate time difference in seconds
#     time_diff = round(rmm_time - hmm_time, 2)
    
#     # Determine time status
#     if time_diff > 0:
#         time_status = "behind"
#     else:
#         time_status = "ahead of"
#         time_diff = abs(time_diff)  # Make positive for message
    
#     # Determine movement direction
#     x_diff = rmm_pos[0] - hmm_pos[0]
#     y_diff = rmm_pos[1] - hmm_pos[1]
    
#     # Create a prompt for Mistral with all the information needed to generate the message
#     prompt = f"""
#     You are a robot status reporting system.
    
#     Robot number: {robot_number}
#     Time difference: {time_diff} seconds
#     Time status: {time_status} the expected time
#     Position difference: x={x_diff}, y={y_diff}
    
#     Based on the position difference, determine the direction (north, northeast, east, southeast, 
#     south, southwest, west, or northwest) and create a message in exactly this format:
#     "Robot [number] is [time_diff] seconds [time_status] the expected time; it has moved [direction]."
    
#     Only respond with the exact message format, no additional explanation.
#     """
    
#     # Call Mistral through Ollama
#     response = ollama.chat(model='mistral', messages=[
#         {
#             'role': 'user',
#             'content': prompt
#         }
#     ])
    
#     # Extract the generated message
#     message = response['message']['content'].strip()
    
#     return message


import ollama

# def generate_delay_message_ollama(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag=False):
#     """
#     Generate a delay message with consistent formatting for robot status communication
#     using Mistral through Ollama.
    
#     Parameters:
#     - robot_number: The identifier for the robot
#     - hmm_time: Expected/planned time
#     - rmm_time: Actual time
#     - hmm_pos: Expected/planned position as tuple (x, y)
#     - rmm_pos: Actual position as tuple (x, y)
#     - replan_flag: Boolean indicating if replanning occurred

#     Returns:
#     - Formatted status message via Mistral
#     """
#     # Calculate raw time difference and round
#     raw_diff = rmm_time - hmm_time
#     time_diff = abs(round(raw_diff))
#     report_time = time_diff > 5
#     time_status = "behind" if raw_diff > 0 else "ahead of"

#     # Calculate position difference
#     x_diff = rmm_pos[0] - hmm_pos[0]
#     y_diff = rmm_pos[1] - hmm_pos[1]

#     # Determine compass abbreviation
#     vert = "N" if y_diff > 0 else "S" if y_diff < 0 else ""
#     hor = "E" if x_diff > 0 else "W" if x_diff < 0 else ""
#     direction = vert + hor

#     # Build prompt for Ollama / Mistral
#     prompt = f"""
# You are a robot status reporting system.

# Robot number: {robot_number}
# Rounded time difference (s): {time_diff}
# Report time? {report_time}
# Time status: {time_status}
# Position difference: x={x_diff}, y={y_diff}
# Direction abbreviation: {direction}

# Follow these rules exactly:
# 1. If both x and y differences are zero, output exactly:
#    Robot {robot_number} is stationary.
# 2. Otherwise:
#    - Use the provided compass abbreviation for movement.
#    - If Report time? is True, include "is {time_diff} seconds {time_status} the expected time;" else omit time.
#    - When including time, format:
#      Robot {robot_number} is {time_diff} seconds {time_status} the expected time; it has moved {direction}.
#    - When omitting time, format:
#      Robot {robot_number} has moved {direction}.
# 3. Do not include any additional text or formatting.
# """

#     # Invoke Mistral via Ollama
#     response = ollama.chat(
#         model='mistral',
#         messages=[{'role': 'user', 'content': prompt}]
#     )
#     # Extract and return the generated message
#     return response['message']['content'].strip()


#ollama



# def generate_delay_message_ollama(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag=False):
#     """
#     Generate a delay message with consistent formatting for robot status communication
#     using Mistral through Ollama.
    
#     Parameters:
#     - robot_number: The identifier for the robot
#     - hmm_time: Expected/planned time
#     - rmm_time: Actual time
#     - hmm_pos: Expected/planned position as tuple (x, y)
#     - rmm_pos: Actual position as tuple (x, y)
#     - replan_flag: Boolean indicating if replanning occurred

#     Returns:
#     - Formatted status message via Mistral
#     """
#     # Calculate raw time difference and round
#     raw_diff = rmm_time - hmm_time
#     time_diff = abs(round(raw_diff))
#     report_time = time_diff > 5
#     time_status = "behind" if raw_diff > 0 else "ahead of"

#     # Calculate position difference
#     x_diff = rmm_pos[0] - hmm_pos[0]
#     y_diff = rmm_pos[1] - hmm_pos[1]

#     # Check for stationary
#     if x_diff == 0 and y_diff == 0:
#         # Directly handle stationary case via Ollama
#         prompt = f"Robot {robot_number} is stationary."
#         return prompt

#     # Determine direction: cardinal words or diagonal abbreviations
#     if x_diff != 0 and y_diff != 0:
#         # Diagonal: NE, NW, SE, SW
#         if y_diff > 0 and x_diff > 0:
#             direction = "NE"
#         elif y_diff > 0 and x_diff < 0:
#             direction = "NW"
#         elif y_diff < 0 and x_diff > 0:
#             direction = "SE"
#         else:
#             direction = "SW"
#     else:
#         # Cardinal: north, south, east, west
#         if y_diff != 0:
#             direction = "north" if y_diff > 0 else "south"
#         else:
#             direction = "east" if x_diff > 0 else "west"

#     # Build prompt for Ollama / Mistral
#     prompt = f"""
# You are a robot status reporting system.

# Robot number: {robot_number}
# Rounded time difference (s): {time_diff}
# Report time? {report_time}
# Time status: {time_status}
# Position difference: x={x_diff}, y={y_diff}
# Direction: {direction}

# Follow these rules exactly:
# 1. Use the provided direction for movement.
# 2. If Report time? is True, include the phrase:
#    is {time_diff} seconds {time_status};
#    otherwise omit any time mention.
# 3. When including time, the full output must be exactly:
#    Robot {robot_number} is {time_diff} seconds {time_status}; it has moved {direction}.
# 4. When omitting time, the full output must be exactly:
#    Robot {robot_number} has moved {direction}.
# 5. Do not output any additional text or formatting.
# """

#     # Invoke Mistral via Ollama
#     response = ollama.chat(
#         model='mistral',
#         messages=[{'role': 'user', 'content': prompt}]
#     )
#     # Extract and return the generated message
#     return response['message']['content'].strip()





# import ollama

# system_prompt = """
# You are a robot status reporting system.

# Based on the provided data, output exactly one line in one of these formats:

# 1. Robot {robot_number} is stationary.
# 2. Robot {robot_number} is {time_diff} seconds {time_status}; it has moved {direction}.
# 3. Robot {robot_number} has moved {direction}.

# No other text or formatting.
# """

# def generate_delay_message_ollama(
#     robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag=False,
#     model_name='mistral'
# ):
#     """
#     Generate a delay message via Ollama using streamlined prompts for speed.

#     Parameters:
#     - robot_number: identifier for the robot
#     - hmm_time: expected/planned time
#     - rmm_time: actual time
#     - hmm_pos: expected position tuple (x, y)
#     - rmm_pos: actual position tuple (x, y)
#     - replan_flag: boolean flag (unused in messaging)
#     - model_name: Ollama model to call

#     Returns:
#     - Single-line status message per system instructions
#     """
#     # Compute raw time difference and round
#     raw_diff = rmm_time - hmm_time
#     time_diff = abs(round(raw_diff))
#     report_time = time_diff > 5
#     time_status = 'behind' if raw_diff > 0 else 'ahead of'

#     # Compute position difference
#     x_diff = rmm_pos[0] - hmm_pos[0]
#     y_diff = rmm_pos[1] - hmm_pos[1]

#     # Handle stationary case manually
#     if x_diff == 0 and y_diff == 0:
#         return f"Robot {robot_number} is stationary."

#     # Determine direction: diagonal abbreviations or cardinal words
#     if x_diff != 0 and y_diff != 0:
#         if x_diff > 0 and y_diff > 0:
#             direction = 'NE'
#         elif x_diff < 0 and y_diff > 0:
#             direction = 'NW'
#         elif x_diff > 0 and y_diff < 0:
#             direction = 'SE'
#         else:
#             direction = 'SW'
#     else:
#         if y_diff != 0:
#             direction = 'North' if y_diff > 0 else 'South'
#         else:
#             direction = 'East' if x_diff > 0 else 'West'

#     # Build minimal payload for Ollama
#     user_payload = (
#         f"robot_number={robot_number},"
#         f"time_diff={time_diff},"
#         f"report_time={report_time},"
#         f"time_status={time_status},"
#         f"direction={direction}"
#     )

#     # Invoke Ollama with system + user messages
#     response = ollama.chat(
#         model=model_name,
#         messages=[
#             {'role': 'system', 'content': system_prompt},
#             {'role': 'user', 'content': user_payload}
#         ]
#     )
#     return response['message']['content'].strip()

import ollama

# Preload static instructions to speed up prompt processing
system_prompt = """
You are a robot status reporting system.

Based on the provided data, output exactly one line in one of these formats:

1. Robot {robot_number} is stationary.
2. Robot {robot_number} is {time_diff} seconds {time_status}; it has moved {direction}.
3. Robot {robot_number} has moved {direction}.

No other text or formatting. Do not hallucniate. stick to the given options.
"""

def generate_delay_message_ollama(
    robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag=False,
    model_name='mistral'
):
    """
    Generate a delay message via Ollama using streamlined prompts for speed.

    Parameters:
    - robot_number: identifier for the robot
    - hmm_time: expected/planned time
    - rmm_time: actual time
    - hmm_pos: expected position tuple (x, y)
    - rmm_pos: actual position tuple (x, y)
    - replan_flag: boolean flag (unused in messaging)
    - model_name: Ollama model to call

    Returns:
    - Single-line status message per system instructions
    """
    # Compute raw time difference and round
    raw_diff = rmm_time - hmm_time
    time_diff = abs(round(raw_diff))
    report_time = time_diff > 5
    time_status = 'behind' if raw_diff > 0 else 'ahead'

    # Compute position difference
    x_diff = rmm_pos[0] - hmm_pos[0]
    y_diff = rmm_pos[1] - hmm_pos[1]

    # Handle stationary case manually
    if x_diff == 0 and y_diff == 0:
        return f"Robot {robot_number} is stationary."

    # Determine direction: diagonal abbreviations or cardinal words
    if x_diff != 0 and y_diff != 0:
        if x_diff > 0 and y_diff > 0:
            direction = 'NE'
        elif x_diff < 0 and y_diff > 0:
            direction = 'NW'
        elif x_diff > 0 and y_diff < 0:
            direction = 'SE'
        else:
            direction = 'SW'
    else:
        if y_diff != 0:
            direction = 'north' if y_diff > 0 else 'south'
        else:
            direction = 'east' if x_diff > 0 else 'west'

    # If within threshold, skip time reporting and return movement-only
    if not report_time:
        return f"Robot {robot_number} has moved {direction}."

    # Build minimal payload for Ollama when time needs to be reported
    user_payload = (
        f"robot_number={robot_number},"
        f"time_diff={time_diff},"
        f"report_time={report_time},"
        f"time_status={time_status},"
        f"direction={direction}"
    )

    # Invoke Ollama with system + user messages for time-reporting cases
    response = ollama.chat(
        model=model_name,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_payload}
        ]
    )
    return response['message']['content'].strip()


# if ollama fails/too slow

def generate_delay_message_manual_v2(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag=False):
    """
    Manually generate the same delay message without using Ollama.
    """
    raw_diff = rmm_time - hmm_time
    time_diff = abs(round(raw_diff))
    report_time = time_diff > 5
    time_status = "behind" if raw_diff > 0 else "ahead of"

    x_diff = rmm_pos[0] - hmm_pos[0]
    y_diff = rmm_pos[1] - hmm_pos[1]

    # Stationary check
    if x_diff == 0 and y_diff == 0:
        return f"Robot {robot_number} is stationary."

    # Determine direction
    if x_diff != 0 and y_diff != 0:
        if y_diff > 0 and x_diff > 0:
            direction = "NE"
        elif y_diff > 0 and x_diff < 0:
            direction = "NW"
        elif y_diff < 0 and x_diff > 0:
            direction = "SE"
        else:
            direction = "SW"
    else:
        if y_diff != 0:
            direction = "north" if y_diff > 0 else "south"
        else:
            direction = "east" if x_diff > 0 else "west"

    # Build message manually
    if report_time:
        return (
            f"Robot {robot_number} is {time_diff} seconds {time_status}; "
            f"it has moved {direction}."
        )
    else:
        return f"Robot {robot_number} has moved {direction}."





def generate_delay_message_manual(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos, replan_flag):
    """
    Generate a delay message with consistent formatting for robot status communication.
    
    Parameters:
    - robot_number: The identifier for the robot
    - hmm_time: Expected/planned time
    - rmm_time: Actual time
    - hmm_pos: Expected/planned position as tuple (x, y)
    - rmm_pos: Actual position as tuple (x, y)
    - replan_flag: Boolean indicating if replanning occurred
    
    Returns:
    - Formatted status message
    """
    # Calculate time difference in seconds
    time_diff = round(rmm_time - hmm_time, 2)
    
    # Determine time status
    if time_diff > 0:
        time_status = "behind"
    else:
        time_status = "ahead of"
        time_diff = abs(time_diff)  # Make positive for message
    
    # Determine movement direction
    x_diff = rmm_pos[0] - hmm_pos[0]
    y_diff = rmm_pos[1] - hmm_pos[1]
    
    # Determine direction with full 8-way movement
    if x_diff > 0 and y_diff > 0:
        direction = "northeast"
    elif x_diff > 0 and y_diff < 0:
        direction = "southeast"
    elif x_diff < 0 and y_diff > 0:
        direction = "northwest"
    elif x_diff < 0 and y_diff < 0:
        direction = "southwest"
    elif x_diff > 0:
        direction = "east"
    elif x_diff < 0:
        direction = "west"
    elif y_diff > 0:
        direction = "north"
    else:
        direction = "south"
    
    # Create the base message in the required format
    message = f"Robot {robot_number} is {time_diff} seconds {time_status} the expected time; it has moved {direction}."
    
    return message



def generate_communication_message_ollama(deviation, threshold, hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time, robot_number, JSON_data):
    """
    Generate a communication message using the Ollama model if the deviation exceeds the threshold.
    """
    messages = []
    if abs(deviation) > threshold:
        robot_number = robot_number  # Assuming robot number is passed correctly
        hmm_pos = (hmm_pos1, hmm_pos2)
        rmm_pos = (rmm_pos1, rmm_pos2)
        # print("JSON_data", JSON_data)
        # replan_flag = JSON_data.get('replan_flag')
        replan_flag = JSON_data['robots'][f'robot{robot_number}']['replan_flag']

        # Generate delay message using Ollama
        delay_message = generate_delay_message_ollama(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos,replan_flag)
        # delay_message = generate_delay_message_manual(robot_number, hmm_time, rmm_time, hmm_pos, rmm_pos,replan_flag)


        # Check replan_flag for the specific robot and append replan info if true
        if JSON_data['robots'][f'robot{robot_number}']['replan_flag']:
            delay_message += " It has a new plan/target."

        messages.append(delay_message)  # Append formatted delay message to messages list
    return messages







def dynamic_deviation_threshold_multi_logic(JSON_data, hmm_arrays, rmm_arrays, update_logic_functions, uncertainty_factor_pos,
                                           uncertainty_factor_time, dynamic_threshold_mission_time, robot_id):
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






    robot_number = int(robot_id.replace("robot", ""))
    # print("robot_number",robot_number)




    # # Generate communication message
    # message = generate_communication_message(mission_time_deviation_value, dynamic_threshold_mission_time,
    #                                           hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time, robot_number)
    # formatted_message = "\n".join(message)


    # Generate communication message
    message = generate_communication_message_ollama(mission_time_deviation_value, dynamic_threshold_mission_time,
                                              hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time, robot_number, JSON_data)
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

