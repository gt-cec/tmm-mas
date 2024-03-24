import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  # Import FuncAnimation

import csv
import numpy as np

# matplotlib global parameters
matplotlib.rcParams["font.sans-serif"] = "Roboto"
matplotlib.rcParams["font.size"] = 25

# Function to calculate KL Divergence
def calculate_kl_divergence(array1, array2):
    # Ensure non-zero values to prevent log(0)
    array1 = np.maximum(array1, np.finfo(float).eps)
    array2 = np.maximum(array2, np.finfo(float).eps)

    # Calculate KL Divergence
    kl_divergence = np.sum(array1 * np.log(array1 / array2))

    return kl_divergence


# Function to calculate evaluation metrics
def evaluate_update(original_hmm, updated_hmm):
    # Calculate metrics
    mission_time_index = 4
    mae_time = np.abs(original_hmm[:, mission_time_index] - updated_hmm[:, mission_time_index]).mean()
    rmse_time = np.sqrt(((original_hmm[:, mission_time_index] - updated_hmm[:, mission_time_index]) ** 2).mean())
    # correlation_time = np.corrcoef(original_hmm[:, mission_time_index], updated_hmm[:, mission_time_index])[0, 1]  # broke for some reason
    # kl_divergence_time = calculate_kl_divergence(original_hmm[:, mission_time_index], updated_hmm[:, mission_time_index])
    percentage_updated_time = np.mean(original_hmm[:, mission_time_index] != updated_hmm[:, mission_time_index])
    rmae_time = mae_time / np.mean(np.abs(original_hmm[:, mission_time_index]))

    # Display metrics
    print("\nMetrics:")
    print(f"MAE_Time: {mae_time}")
    print(f"RMSE_Time: {rmse_time}")
    # print(f"Correlation_Time: {correlation_time}")
    # print(f"KL_Divergence_Time: {kl_divergence_time}")
    print(f"Percentage_Updated_Time: {percentage_updated_time}")
    print(f"RMAE_Time: {rmae_time}")

    return {
        'MAE_Time': mae_time,
        'RMSE_Time': rmse_time,
        # 'Correlation_Time': correlation_time,
        # 'KL_Divergence_Time': kl_divergence_time,
        'Percentage_Updated_Time': percentage_updated_time,
        'RMAE_Time': rmae_time,
    }


def plot_hmm_arrays(original_hmm, updated_hmm, rmm_arrays, update_points=[]):
    mission_time_index = 4

    # Extract time values from rmm_arrays
    rmm_time_values = [pose[mission_time_index] for pose in rmm_arrays]

    # Plot the HMM arrays and RMM time values
    plt.figure(figsize=(8, 6))
    # original_line, = plt.plot(original_hmm[:, 4], label='Original HMM Time', linestyle='--', marker='o')
    plt.plot(updated_hmm[:, mission_time_index], label='Human MM Time', linewidth=3, markersize=10, linestyle='--')
    plt.plot(rmm_time_values, label='Robot MM Time', linestyle='-', linewidth=3)
    plt.scatter(x=[p[0] for p in update_points], y=[p[1] for p in update_points], s=500, zorder=3, marker="*", color="purple", label="Robot Updates Human")

    # Add labels and legend
    plt.title('Change in Human and Robot Mental Models Over Simulation Rollout')
    plt.xlabel('Simulation Time Step')
    plt.xlim([0, 50])
    plt.ylabel('Overall Mission Time [time steps]')
    plt.ylim([0, 80])

    legend = plt.legend(loc="lower right")
    legend.get_frame().set_linewidth(0)  # Remove legend border
    legend.get_frame().set_facecolor('none')  # Remove legend background color

    plt.gca().spines["top"].set_visible(False)  # remove spines
    plt.gca().spines["right"].set_visible(False)
    plt.show()


def generate_rmm_array(shmm_data):
    num_tasks = len(shmm_data)
                                                                                                                                                                                                    
    position_values = [pose[0] for pose in shmm_data]
    time_values = [pose[1] for pose in shmm_data]
    mission_tim_values = [pose[2] for pose in shmm_data]

    # Increase noise standard deviation
    position_noise = np.random.normal(0, 1, num_tasks)  # Adjusted standard deviation
    time_noise = np.random.normal(0, 3, num_tasks)

    rmm_array = []
    prev_time = 0  # Variable to track the previous time value

    for i in range(num_tasks):
        position_value1 = int(np.round(np.abs(position_values[i][0] + position_noise[i])))
        position_value2 = int(np.round(np.abs(position_values[i][1] + np.random.normal(0, 0.1))))
        time_taken = round((np.abs(time_values[i] + time_noise[i])),2)
        mission_tim = int(mission_tim_values[i])

        # Clip position values to be within specified limits
        position_value1 = np.clip(position_value1, 0, 5)
        position_value2 = np.clip(position_value2, 0, 3)

        rmm_array.append([i, position_value1, position_value2, time_taken, mission_tim])

        # Update the previous time value
        prev_time = time_taken + 1  # Increase time for the next iteration

    return rmm_array


# Function to calculate L1 norm between two arrays
def calculate_l1_norm(array1, array2):
    norm = (np.array(array2) - np.array(array1))
    return norm


def bayesian_probabilistic_update_general(original_value, deviation, threshold, uncertainty_factor):
    # Expectation step: compute the expected value of the latent variable
    expected_value = original_value + deviation
    
    # Maximization step: update the parameter using the expected value
    updated_value = expected_value
    
    # Update only if the deviation crosses the threshold
    updated_value = updated_value if abs(deviation) > threshold else original_value
    return updated_value


# Function for dynamic deviation threshold update with different update logics
def dynamic_deviation_threshold_multi_logic(hmm_arrays, rmm_arrays, update_logic_functions, uncertainty_factor_pos, uncertainty_factor_time):
    all_updated_hmm_arrays = []

    print("@@@", len(hmm_arrays))

    for i, update_logic in enumerate(update_logic_functions):
        # Calculate dynamic deviation threshold as the mean deviation across all arrays
        # Jack: I removed this because it is using the entire future time history, which does not reflect what we want (real-time)
        pos_deviation = calculate_l1_norm(hmm_arrays[i][1:3], rmm_arrays[i][1:3])
        time_deviation = calculate_l1_norm([hmm_arrays[i][3]], [rmm_arrays[i][3]])[0]
        mission_tim_deviation = calculate_l1_norm([hmm_arrays[i][4]], [rmm_arrays[i][4]])[0]

        # Bayesian Probabilistic Update for the entire array
        # Calculate dynamic deviation threshold as the mean deviation across all arrays
        dynamic_threshold_pos = max([max(x, 0.01) for x in pos_deviation])
        dynamic_threshold_time = max(time_deviation, 0.1)
        dynamic_threshold_mission_time = 5

        # Bayesian Probabilistic Update for the entire array
        updated_hmm_array = []
        current_hmm_mission_time = rmm_arrays[0][4]
        for i in range(len(hmm_arrays)):
            # pos_deviation = calculate_l1_norm(hmm_arrays[i][1:3], rmm_arrays[i][1:3])
            # time_deviation = calculate_l1_norm([hmm_arrays[i][3]], [rmm_arrays[i][3]])[0]
            updated_pos1 = rmm_arrays[i][1]
            updated_pos2 = rmm_arrays[i][2]    
            mission_time_deviation = calculate_l1_norm([current_hmm_mission_time], [rmm_arrays[i][4]])[0]     
            
            # Bayesian Probabilistic Update for time
            # updated_time = update_logic(hmm_arrays[i][3], time_deviation, dynamic_threshold_time, uncertainty_factor_time)
            updated_mission_time = update_logic(current_hmm_mission_time, mission_time_deviation, dynamic_threshold_mission_time, uncertainty_factor_time)
            current_hmm_mission_time = updated_mission_time
            # print("###", i, current_hmm_mission_time, mission_time_deviation, rmm_arrays[i], len(rmm_arrays), rmm_arrays[i][4])
            updated_hmm_array.append([i, int(round(updated_pos1,0)), int(round(updated_pos2,0)), None, updated_mission_time])

        all_updated_hmm_arrays.append(np.array(updated_hmm_array))

    return all_updated_hmm_arrays



if __name__ == "__main__":
    update_logics = [
        bayesian_probabilistic_update_general
    ]

    # Set uncertainty factors for Bayesian probabilistic updates
    uncertainty_factor_pos = 0.05  # You may adjust this factor based on your preferences
    uncertainty_factor_time = 0.01  # You may adjust this factor based on your preferences

    shmm_data = []

    # Read data from CSV file and format it
    with open("robot_data_1.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        timestep = 0
        for row in csv_reader:
            first_state = int(row[1])
            second_state = int(row[2])
            time_elapsed = float(row[3])
            steps_remaining = int(row[4])
            mission_time = timestep + steps_remaining
            shmm_data.append(((first_state, second_state), time_elapsed, mission_time))
            timestep += 1

    # Generate RMM array
    rmm_arrays = generate_rmm_array(shmm_data)

    # Add index position
    shmm_data_with_index = [[i, pose[0][0], pose[0][1], pose[1], pose[2]] for i, pose in enumerate(shmm_data)]

    # Format SHMM array
    hmm_arrays = []
    for arr in shmm_data_with_index:
        hmm_arrays.append([arr[0], arr[1], arr[2], round(arr[3], 2), 39])

    # Print the arrays
    print("SHMM_array:")
    for arr in hmm_arrays:
        print(arr)

    print("\nRMM_array:")
    for arr in rmm_arrays:
        print(arr)


    # Dynamic Deviation Threshold with multiple update logics
    all_updated_arrays = dynamic_deviation_threshold_multi_logic(
        hmm_arrays, rmm_arrays, update_logics, uncertainty_factor_pos, uncertainty_factor_time
    )

    # Calculate metrics and composite score for each update logic
    all_metrics = []
    for i, updated_hmm_array in enumerate(all_updated_arrays):
        index =i+1
        print(f"\nUpdated HMM_array for Update Logic {i + 1} - {update_logics[i].__name__}:")

        # Record the points where the HMM updates
        update_points = []
        last_point = None
        for arr in updated_hmm_array:
            point_of_interest = arr[4]
            if last_point is None or point_of_interest != last_point:
                last_point = point_of_interest
                update_points.append((arr[0], point_of_interest))

        # Evaluate and visualize performance for each update logic
        print(f"\nMetrics for Update Logic {i + 1} - {update_logics[i].__name__}:")
        metrics = evaluate_update(np.array(hmm_arrays), np.array(updated_hmm_array))
        all_metrics.append(metrics)
        plot_hmm_arrays(np.array(hmm_arrays), np.array(updated_hmm_array), rmm_arrays, update_points=update_points)

    # Assign weights based on general understanding (Time-only)
    weights = {
        'MAE_Time': 0.2,
        'RMSE_Time': 0.2,
        'Correlation_Time': 0.2,
        'KL_Divergence_Time': 0.15,
        'Percentage_Updated_Time': 0.15,
        'RMAE_Time': 0.1,
    }

    # Function to calculate the composite score
    def calculate_composite_score(metrics, weights):
        composite_score = 0
        total_weight = sum(weights.values())

        for metric, weight in weights.items():
            if metric in metrics and metrics[metric] is not None:
                composite_score += weight / metrics[metric]

        if total_weight == 0:
            return None

        return len(metrics) / composite_score  # Harmonic mean

    # Display composite scores for each update logic with epsilon adjustment
    for i, metrics in enumerate(all_metrics):
        composite_score = calculate_composite_score(metrics, weights )
        print(f"\nComposite Score for Update Logic {i + 1} - {update_logics[i].__name__}: {composite_score}")
