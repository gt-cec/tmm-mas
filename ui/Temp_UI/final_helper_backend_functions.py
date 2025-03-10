# operation_functions.py

import numpy as np
import pandas as pd




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
    # x_val = robot_info["x"][0] if len(robot_info["x"]) > 0 else None
    # y_val = robot_info["y"][1] if len(robot_info["y"]) > 1 else None
    # x_val = robot_info["x"][0] if len(robot_info["x"]) > 0 else None
    # y_val = robot_info["y"][1] if len(robot_info["y"]) > 1 else None
    x_val = robot_info["x"]
    y_val = robot_info["y"]
    mission_time = robot_info["mission_time"]

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


def dynamic_deviation_threshold_multi_logic(hmm_arrays, rmm_arrays, update_logic_functions, uncertainty_factor_pos,
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




    # Generate communication message
    message = generate_communication_message(mission_time_deviation_value, dynamic_threshold_mission_time,
                                              hmm_pos1, hmm_pos2, rmm_pos1, rmm_pos2, hmm_time, rmm_time, robot_number)
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

