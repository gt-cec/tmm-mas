#do not try; failure
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import numpy as np

# Load an LLM model locally
def load_model(model_name):
    print(f"🔄 Loading model: {model_name} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
    return model, tokenizer

# Calculate L1 norm (mission time deviation)
def calculate_l1_norm(array1, array2):
    return np.abs(np.array(array2) - np.array(array1))

# Generate a communication message
def generate_communication_message(hmm_array, rmm_array, model, tokenizer):
    robot_number = "quad1"
    
    X = hmm_array[4]  # HMM mission time
    Y = rmm_array[4]  # RMM mission time
    A = (hmm_array[1], hmm_array[2])  # Expected position
    B = (rmm_array[1], rmm_array[2])  # Actual position

    time_diff = Y - X
    position_diff = (B[0] - A[0], B[1] - A[1])

    prompt = f"""
    You are an AI generating mission status updates for a commander monitoring a robot.
    Given the following data:
    - Robot: {robot_number}
    - Expected mission time: {X} sec
    - Actual mission time: {Y} sec
    - Expected position: {A}
    - Actual position: {B}
    - Time deviation: {time_diff} sec
    - Position deviation: {position_diff}

    Generate a status update in a professional but concise tone.
    """

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
    output = model.generate(input_ids, max_length=250)
    message = tokenizer.decode(output[0], skip_special_tokens=True)

    return message

# List of local models
local_models = {
    "Mistral-7B": "mistralai/Mistral-7B-Instruct-v0.1",
    "Llama-2-7B-Chat": "meta-llama/Llama-2-7b-chat-hf",
    "Phi-2": "microsoft/phi-2",
    "GPT4All-J": "nomic-ai/gpt4all-j"
}

# Test input
hmm_array = [13, 2.0, 1.0, 0.0081, 37]
rmm_array = [13, 3.0, 2.0, 0.0, 26]

# Generate messages with each LLM
for model_name, model_id in local_models.items():
    model, tokenizer = load_model(model_id)
    message = generate_communication_message(hmm_array, rmm_array, model, tokenizer)
    print(f"\n🟢 **{model_name} Output:**\n{message}\n" + "="*50)
