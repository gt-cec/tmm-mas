# from transformers import pipeline

# # Initialize the text generation pipeline with a local model
# # Replace 'model_name' with the actual model you have downloaded and want to use
# # Example: 'EleutherAI/gpt-neo-1.3B', 'EleutherAI/gpt-j-6B', 'decapoda-research/llama-7b-hf'
# def initialize_model(model_name):
#     generator = pipeline('text-generation', model=model_name)
#     return generator

# def generate_message_with_llm(generator, prompt):
#     messages = generator(prompt, max_length=100, num_return_sequences=1)
#     return messages[0]['generated_text']

# def main(hmm_array, rmm_array):
#     # Extract data from arrays
#     robot_number = hmm_array[0]
#     hmm_pos = (hmm_array[1], hmm_array[2])
#     rmm_pos = (rmm_array[1], rmm_array[2])
#     hmm_time = hmm_array[3]
#     rmm_time = rmm_array[3]
#     hmm_mission_time = hmm_array[4]
#     rmm_mission_time = rmm_array[4]

#     # Generate a prompt for the LLM
#     prompt = f"Robot {robot_number}'s mission status update:\n" \
#              f"- Estimated Position: {hmm_pos}, Actual Position: {rmm_pos}\n" \
#              f"- Estimated Time: {hmm_time}, Actual Time: {rmm_time}\n" \
#              f"- Estimated Mission Time: {hmm_mission_time}, Actual Mission Time: {rmm_mission_time}\n" \
#              f"Generate a detailed status message based on this data."

#     # List of models to try
#     models = ['EleutherAI/gpt-neo-1.3B', 'EleutherAI/gpt-j-6B', 'decapoda-research/llama-7b-hf']

#     for model_name in models:
#         print(f"Using model: {model_name}")
#         generator = initialize_model(model_name)
#         message = generate_message_with_llm(generator, prompt)
#         print("Generated Message:\n", message)
#         print("\n" + "="*50 + "\n")

# if __name__ == "__main__":
#     hmm_array = [13, 2.0, 1.0, 0.0081, 37]
#     rmm_array = [13, 3.0, 2.0, 0.0, 26]
#     main(hmm_array, rmm_array)


#has memory and speed issues.
from transformers import pipeline
import torch

def initialize_model(model_name, use_cpu=False):
    if use_cpu:
        generator = pipeline('text-generation', model=model_name, device_map="cpu")
    else:
        # Use GPU with mixed precision (FP16) to save memory
        generator = pipeline('text-generation', model=model_name, device=0, torch_dtype=torch.float16)
    return generator

def generate_message_with_llm(generator, prompt):
    messages = generator(prompt, max_length=100, num_return_sequences=1, batch_size=1)
    return messages[0]['generated_text']

def main(hmm_array, rmm_array):
    # Extract data from arrays
    robot_number = hmm_array[0]
    hmm_pos = (hmm_array[1], hmm_array[2])
    rmm_pos = (rmm_array[1], rmm_array[2])
    hmm_time = hmm_array[3]
    rmm_time = rmm_array[3]
    hmm_mission_time = hmm_array[4]
    rmm_mission_time = rmm_array[4]

    # Generate a prompt for the LLM
    prompt = f"Robot {robot_number}'s mission status update:\n" \
             f"- Estimated Position: {hmm_pos}, Actual Position: {rmm_pos}\n" \
             f"- Estimated Time: {hmm_time}, Actual Time: {rmm_time}\n" \
             f"- Estimated Mission Time: {hmm_mission_time}, Actual Mission Time: {rmm_mission_time}\n" \
             f"Generate a detailed status message based on this data."

    # List of models to try
    models = ['EleutherAI/gpt-neo-125M', 'gpt2', 'distilgpt2']

    for model_name in models:
        print(f"Using model: {model_name}")
        try:
            # Try GPU first, fallback to CPU if GPU memory is insufficient
            generator = initialize_model(model_name, use_cpu=False)
            message = generate_message_with_llm(generator, prompt)
            print("Generated Message:\n", message)
        except RuntimeError as e:
            print(f"GPU memory error with {model_name}. Falling back to CPU.")
            generator = initialize_model(model_name, use_cpu=True)
            message = generate_message_with_llm(generator, prompt)
            print("Generated Message:\n", message)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    hmm_array = [13, 2.0, 1.0, 0.0081, 37]
    rmm_array = [13, 3.0, 2.0, 0.0, 26]
    main(hmm_array, rmm_array)