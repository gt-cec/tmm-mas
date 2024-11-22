from transformers import AutoModelForCausalLM, AutoTokenizer

# Load LLaMA model and tokenizer
model_name = "llama-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define the allowed tokens
allowed_tokens = ["<1>", "<2>", "<3>"]
allowed_token_ids = tokenizer.convert_tokens_to_ids(allowed_tokens)

# Create a logits processor to restrict outputs
def custom_logits_processor(logits, allowed_ids):
    import torch
    mask = torch.full_like(logits, float("-inf"))
    for token_id in allowed_ids:
        mask[:, token_id] = 0  # Allow these tokens
    return logits + mask

# Define the input
input_text = "Which option do you choose?"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# Generate with constraints
outputs = model.generate(
    input_ids,
    max_length=10,
    logits_processor=[lambda input_ids, scores: custom_logits_processor(scores, allowed_token_ids)],
)
output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(output_text)
