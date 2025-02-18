# import json
# import os
# import requests

# output_dir = "robot_jsons"
# server_url = "http://127.0.0.1:5006/receive_data"

# json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")])

# # Read all JSON files into a list
# json_data = []
# for file in json_files:
#     file_path = os.path.join(output_dir, file)
    
#     with open(file_path, "r") as f:
#         data = json.load(f)
#         json_data.append(data)

# response = requests.post(server_url, json=json_data)

# if response.status_code == 200:
#     print("✅ All JSON files sent successfully!")
# else:
#     print(f"❌ Failed to send data - Status: {response.status_code}")

    
#     time.sleep(5)




import json
import os
import requests

# Directory containing JSON files
output_dir = "robot_jsons"
# server_url = "http://127.0.0.1:5000/receive_data"
server_url = "http://127.0.0.1:5211/receive_data"

# Get all JSON files
json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")])

# Read all JSON files into a list
json_data = []
for file in json_files:
    file_path = os.path.join(output_dir, file)
    
    with open(file_path, "r") as f:
        data = json.load(f)
        json_data.append(data)

# Send all JSON data in one request
response = requests.post(server_url, json=json_data)

if response.status_code == 200:
    print("✅ All JSON files sent successfully!")
else:
    print(f"❌ Failed to send data - Status: {response.status_code}")

    time.sleep(5)
