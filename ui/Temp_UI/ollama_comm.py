import numpy as np
import ollama

def calculate_l1_norm(array1, array2):
    return np.array(array2) - np.array(array1)

def prepare_prompt(hmm_array, rmm_array):
    """
    Prepare a short and direct prompt for LLM interpretation
    """
    prompt = f"""
You are an AI assistant generating short mission status updates.
Analyze the mission data and return a concise, **2-3 line** report focusing only on key deviations:

HMM Array (Expected): [index: {hmm_array[0]}, pos_x: {hmm_array[1]}, pos_y: {hmm_array[2]}, time_taken: {hmm_array[3]}, mission_time: {hmm_array[4]}]
RMM Array (Actual):    [index: {rmm_array[0]}, pos_x: {rmm_array[1]}, pos_y: {rmm_array[2]}, time_taken: {rmm_array[3]}, mission_time: {rmm_array[4]}]

Output **only** the deviation details:
- Position difference (X, Y)
- Mission time difference - it is not in seconds. it is timesteps.
- Only time taken is in seconds.
No greetings, no formalities. Just a **direct, concise update but like a human, not like machine**.
"""
    return prompt

def generate_message_with_ollama(model, prompt):
    """
    Generate message using Ollama with specified model
    """
    try:
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error with {model}: {str(e)}"

def process_robot_communication(hmm_array, rmm_array):
    """
    Process robot communication using multiple LLM models
    """
    prompt = prepare_prompt(hmm_array, rmm_array)

    # List of Ollama models
    models = ['mistral', 'llama2', 'zephyr', 'openhermes']

    results = {}

    # Compute deviations
    time_deviation = calculate_l1_norm([hmm_array[4]], [rmm_array[4]])[0]
    pos_deviation_x = rmm_array[1] - hmm_array[1]
    pos_deviation_y = rmm_array[2] - hmm_array[2]

    for model in models:
        message = generate_message_with_ollama(model, prompt)
        results[model] = {
            'message': message.strip(),
            'time_deviation': time_deviation,
            'pos_deviation_x': pos_deviation_x,
            'pos_deviation_y': pos_deviation_y
        }

    return results

def main():
    hmm_array = [13, 2.0, 1.0, 0.0081, 37]
    rmm_array = [13, 3.0, 2.0, 0.0, 58]

    results = process_robot_communication(hmm_array, rmm_array)

    print("Robot Communication Analysis:\n")
    for model, result in results.items():
        print(f"Model: {model}")
        print("-" * 50)
        print(f"Message: {result['message']}")
        # print(f"Time Deviation: {result['time_deviation']} sec")
        # print(f"Position X Deviation: {result['pos_deviation_x']} units")
        # print(f"Position Y Deviation: {result['pos_deviation_y']} units\n")

if __name__ == "__main__":
    main()


# import numpy as np
# import ollama

# def calculate_l1_norm(array1, array2):
#     return np.array(array2) - np.array(array1)

# def prepare_prompt(hmm_array, rmm_array):
#     """
#     Prepare a short and direct prompt for LLM interpretation
#     """
#     prompt = f"""
# You are an AI assistant generating short mission status updates.
# Analyze the mission data and return a concise, **2-3 line** report focusing only on key deviations:

# HMM Array (Expected): [index: {hmm_array[0]}, pos_x: {hmm_array[1]}, pos_y: {hmm_array[2]}, time_taken: {hmm_array[3]}, mission_time: {hmm_array[4]}]
# RMM Array (Actual):    [index: {rmm_array[0]}, pos_x: {rmm_array[1]}, pos_y: {rmm_array[2]}, time_taken: {rmm_array[3]}, mission_time: {rmm_array[4]}]

# Output **only** the deviation details:
# - Position difference (X, Y)
# - Mission time difference - it is not in seconds. it is timesteps.
# - Only time taken is in seconds.
# No greetings, no formalities. Just a **direct, concise update but like a human, not like machine**.
# """
#     return prompt

# def generate_message_with_ollama(model, prompt):
#     """
#     Generate message using Ollama with specified model
#     """
#     try:
#         response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
#         return response['message']['content']
#     except Exception as e:
#         return f"Error with {model}: {str(e)}"

# def process_robot_communication(hmm_array, rmm_array):
#     """
#     Process robot communication using multiple LLM models
#     """
#     prompt = prepare_prompt(hmm_array, rmm_array)

#     # List of Ollama models
#     models = ['mistral', 'llama2', 'zephyr', 'openhermes']

#     results = {}

#     # Compute deviations
#     time_deviation = calculate_l1_norm([hmm_array[4]], [rmm_array[4]])[0]
#     pos_deviation_x = rmm_array[1] - hmm_array[1]
#     pos_deviation_y = rmm_array[2] - hmm_array[2]

#     for model in models:
#         message = generate_message_with_ollama(model, prompt)
#         results[model] = {
#             'message': message.strip(),
#             'time_deviation': time_deviation,
#             'pos_deviation_x': pos_deviation_x,
#             'pos_deviation_y': pos_deviation_y
#         }

#     return results

# def main():
#     hmm_array = [13, 2.0, 1.0, 0.0081, 37]
#     rmm_array = [13, 3.0, 2.0, 0.0, 58]

#     results = process_robot_communication(hmm_array, rmm_array)

#     print("Robot Communication Analysis:\n")
#     for model, result in results.items():
#         print(f"Model: {model}")
#         print("-" * 50)
#         print(f"Message: {result['message']}")
#         print(f"Time Deviation: {result['time_deviation']} sec")
#         print(f"Position X Deviation: {result['pos_deviation_x']} units")
#         print(f"Position Y Deviation: {result['pos_deviation_y']} units\n")

# if __name__ == "__main__":
#     main()


# #too long
# # import numpy as np
# # import ollama
# # import json

# # def calculate_l1_norm(array1, array2):
# #     norm = (np.array(array2) - np.array(array1))
# #     return norm

# # def prepare_prompt(hmm_array, rmm_array):
# #     """
# #     Prepare a structured prompt for LLM interpretation
# #     """
# #     prompt = f"""
# # You are an AI assistant interpreting robot mission data. 
# # Analyze the following mission arrays and generate a concise communication message:

# # HMM Array (Estimated): [index: {hmm_array[0]}, pos_x: {hmm_array[1]}, pos_y: {hmm_array[2]}, time_taken: {hmm_array[3]}, mission_time: {hmm_array[4]}]
# # RMM Array (Actual):    [index: {rmm_array[0]}, pos_x: {rmm_array[1]}, pos_y: {rmm_array[2]}, time_taken: {rmm_array[3]}, mission_time: {rmm_array[4]}]

# # Calculate deviations and provide a professional communication message about the robot's mission status.
# # Focus on:
# # - Position differences
# # - Time discrepancies
# # - Overall mission performance

# # Generate a message that a robot commander would find informative and actionable.
# # """
# #     return prompt

# # def generate_message_with_ollama(model, prompt):
# #     """
# #     Generate message using Ollama with specified model
# #     """
# #     try:
# #         response = ollama.chat(model=model, messages=[
# #             {
# #                 'role': 'user',
# #                 'content': prompt
# #             }
# #         ])
# #         return response['message']['content']
# #     except Exception as e:
# #         return f"Error with {model}: {str(e)}"

# # def process_robot_communication(hmm_array, rmm_array):
# #     """
# #     Process robot communication using multiple LLM models
# #     """
# #     # Prepare prompt
# #     prompt = prepare_prompt(hmm_array, rmm_array)
    
# #     # List of Ollama models to try
# #     models = [
# #         'mistral',        # Mistral 7B
# #         'llama2',         # Meta's Llama 2
# #         'zephyr',         # Zephyr 7B Beta
# #         'openhermes'      # OpenHermes 2.5
# #     ]
    
# #     # Store results
# #     results = {}
    
# #     # Calculate time and position deviations
# #     time_deviation = calculate_l1_norm([hmm_array[4]], [rmm_array[4]])[0]
# #     pos_deviation_x = hmm_array[1] - rmm_array[1]
# #     pos_deviation_y = hmm_array[2] - rmm_array[2]
    
# #     # Generate messages with each model
# #     for model in models:
# #         try:
# #             message = generate_message_with_ollama(model, prompt)
# #             results[model] = {
# #                 'message': message,
# #                 'time_deviation': time_deviation,
# #                 'pos_deviation_x': pos_deviation_x,
# #                 'pos_deviation_y': pos_deviation_y
# #             }
# #         except Exception as e:
# #             results[model] = {
# #                 'error': str(e)
# #             }
    
# #     return results

# # def main():
# #     # Example arrays matching the specified format
# #     hmm_array = [13, 2.0, 1.0, 0.0081, 37]
# #     rmm_array = [13, 3.0, 2.0, 0.0, 26]
    
# #     # Process communication
# #     results = process_robot_communication(hmm_array, rmm_array)
    
# #     # Print results
# #     print("Robot Communication Analysis:\n")
# #     for model, result in results.items():
# #         print(f"Model: {model}")
# #         print("-" * 50)
        
# #         if 'message' in result:
# #             print("Generated Message:")
# #             print(result['message'])
# #             print("\nDeviations:")
# #             print(f"Time Deviation: {result['time_deviation']} seconds")
# #             print(f"Position X Deviation: {result['pos_deviation_x']} units")
# #             print(f"Position Y Deviation: {result['pos_deviation_y']} units")
# #         else:
# #             print(f"Error: {result.get('error', 'Unknown error')}")
# #         print("\n")

# # if __name__ == "__main__":
# #     main()





# # import numpy as np
# # import ollama
# # import json

# # def calculate_l1_norm(array1, array2):
# #     norm = (np.array(array2) - np.array(array1))
# #     return norm

# # def prepare_prompt(hmm_array, rmm_array):
# #     """
# #     Prepare a structured prompt for LLM interpretation
# #     """
# #     prompt = f"""
# # You are an AI assistant interpreting robot mission data. 
# # Analyze the following mission arrays and generate a concise communication message:

# # HMM Array (Estimated): [index: {hmm_array[0]}, pos_x: {hmm_array[1]}, pos_y: {hmm_array[2]}, time_taken: {hmm_array[3]}, mission_time: {hmm_array[4]}]
# # RMM Array (Actual):    [index: {rmm_array[0]}, pos_x: {rmm_array[1]}, pos_y: {rmm_array[2]}, time_taken: {rmm_array[3]}, mission_time: {rmm_array[4]}]

# # Calculate deviations and provide a professional communication message about the robot's mission status.
# # Focus on:
# # - Position differences
# # - Time discrepancies
# # - Overall mission performance

# # Generate a message that a robot commander would find informative and actionable.
# # """
# #     return prompt

# # def generate_message_with_ollama(model, prompt):
# #     """
# #     Generate message using Ollama with specified model
# #     """
# #     try:
# #         response = ollama.chat(model=model, messages=[
# #             {
# #                 'role': 'user',
# #                 'content': prompt
# #             }
# #         ])
# #         return response['message']['content']
# #     except Exception as e:
# #         return f"Error with {model}: {str(e)}"

# # def process_robot_communication(hmm_array, rmm_array):
# #     """
# #     Process robot communication using multiple LLM models
# #     """
# #     # Prepare prompt
# #     prompt = prepare_prompt(hmm_array, rmm_array)
    
# #     # List of Ollama models to try
# #     models = [
# #         'mistral',        # Mistral 7B
# #         'llama2',         # Meta's Llama 2
# #         'zephyr',         # Zephyr 7B Beta
# #         'openhermes'      # OpenHermes 2.5
# #     ]
    
# #     # Store results
# #     results = {}
    
# #     # Calculate time and position deviations
# #     time_deviation = calculate_l1_norm([hmm_array[4]], [rmm_array[4]])[0]
# #     pos_deviation_x = hmm_array[1] - rmm_array[1]
# #     pos_deviation_y = hmm_array[2] - rmm_array[2]
    
# #     # Generate messages with each model
# #     for model in models:
# #         try:
# #             message = generate_message_with_ollama(model, prompt)
# #             results[model] = {
# #                 'message': message,
# #                 'time_deviation': time_deviation,
# #                 'pos_deviation_x': pos_deviation_x,
# #                 'pos_deviation_y': pos_deviation_y
# #             }
# #         except Exception as e:
# #             results[model] = {
# #                 'error': str(e)
# #             }
    
# #     return results

# # def main():
# #     # Example arrays matching the specified format
# #     hmm_array = [13, 2.0, 1.0, 0.0081, 37]
# #     rmm_array = [13, 3.0, 2.0, 0.0, 26]
    
# #     # Process communication
# #     results = process_robot_communication(hmm_array, rmm_array)
    
# #     # Print results
# #     print("Robot Communication Analysis:\n")
# #     for model, result in results.items():
# #         print(f"Model: {model}")
# #         print("-" * 50)
        
# #         if 'message' in result:
# #             print("Generated Message:")
# #             print(result['message'])
# #             print("\nDeviations:")
# #             print(f"Time Deviation: {result['time_deviation']} seconds")
# #             print(f"Position X Deviation: {result['pos_deviation_x']} units")
# #             print(f"Position Y Deviation: {result['pos_deviation_y']} units")
# #         else:
# #             print(f"Error: {result.get('error', 'Unknown error')}")
# #         print("\n")

# # if __name__ == "__main__":
# #     main()