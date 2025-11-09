





import numpy as np

## --- Helper Functions (Kept Separate as Requested) ---

def calculate_l1_norm(array1, array2):
    """Calculates the simple difference between two scalar arrays."""
    norm = (np.array(array2) - np.array(array1))
    return norm

def bayesian_probabilistic_update(original_value, deviation, threshold):
    """
    Returns the updated value if deviation exceeds threshold, otherwise the original.
    The updated value is calculated as original_value + deviation.
    """
    expected_value = original_value + deviation
    # This conditional logic is the core of the function
    updated_value = expected_value if abs(deviation) > threshold else original_value
    return updated_value


## --- Main Logic Function (Corrected) ---

def dynamic_deviation_threshold_multi_logic(hmm_array, rmm_array, update_logic_functions, 
                                            uncertainty_factor_pos, uncertainty_factor_time, 
                                            dynamic_threshold_mission_time, robot_id):
    """
    Updates HMM with RMM data only if the Bayesian update function changes the mission time.
    """
    communication_triggered = False  # <-- 1. Initialize a flag to track if an update happens
    
    # Start with a copy that we can modify
    updated_hmm_array = hmm_array.copy()
    
    current_hmm_mission_time = hmm_array['mission_time']
    rmm_mission_time = rmm_array['mission_time']




    # 1. Calculate deviation using your separate function
    mission_time_deviation_vector = calculate_l1_norm([current_hmm_mission_time], [rmm_mission_time])
    mission_time_deviation = mission_time_deviation_vector[0]



    # print(f"hmm_array{hmm_array}...")
    # print(f"rmm_array{rmm_array}...")
    
    # print(f"mission_time_deviation_value{mission_time_deviation}...")
    # print(f"dynamic_threshold_mission_time{dynamic_threshold_mission_time}...")
    
    


    
    # 2. Calculate the potential new mission time using your separate Bayesian function
    updated_mission_time = bayesian_probabilistic_update(
        current_hmm_mission_time, 
        mission_time_deviation,
        dynamic_threshold_mission_time
    )
    print(f"updated_mission_time{updated_mission_time}...")

    
    # 3. Check if the Bayesian function decided an update was needed.
    #    An update occurred if the returned value is different from the original value.
    if updated_mission_time != current_hmm_mission_time:
        print(f"✅ Deviation threshold exceeded for {robot_id} at plan_index { rmm_array['plan_index'] }. New Mission time is {updated_mission_time}. Syncing HMM with RMM state.")
        communication_triggered = True     
        # --- This is the key part ---
        # Since the time was updated, now sync ALL other relevant data from the RMM array.
        for key, value in rmm_array.items():
            if key in updated_hmm_array:
                updated_hmm_array[key] = value
                
        # Finally, ensure the mission_time is set to the value calculated by the Bayesian function.
        # (This is slightly redundant if 'mission_time' is in the loop, but makes the intent explicit).
        updated_hmm_array['mission_time'] = updated_mission_time
    else:
        print(f"⚪ Deviation for {robot_id} is within threshold. No update needed.")



    # print(f"updated_hmm_array{updated_hmm_array}...")
    # 4. Return the result
    return updated_hmm_array, communication_triggered