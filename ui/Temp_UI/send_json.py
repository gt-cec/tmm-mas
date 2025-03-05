



import time
import json
import os
import requests

# Directory containing JSON files
output_dir = "robot_jsons"
# output_dir = "04_03_robot_jsons"
# server_url = "http://127.0.0.1:5000/receive_data"
server_url = "http://127.0.0.1:5211/receive_data"
# server_url = "http://127.0.0.1:5211/reset"

# Get all JSON files sorted numerically
json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")], key=lambda f: int(f.split("_")[-1].split(".")[0]))

# print(json_files)

# # Sort the files numerically by extracting the number from the filename
# sorted_json_files = sorted(json_files, key=lambda f: int(f.split("_")[-1].split(".")[0]))

# # Print sorted list
# print("Sorted files:", sorted_json_files)



# Send each JSON file one by one
for file in json_files:
    file_path = os.path.join(output_dir, file)

    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Wrap the data in a list (as required by the server)
    data_list = [data]

    # Send the data in a POST request
    response = requests.post(server_url, json=data_list)

    if response.status_code == 200:
        print(f"✅ Successfully sent {file}!")
    else:
        print(f"❌ Failed to send {file} - Status: {response.status_code}")

    # Delay between sending each request
    time.sleep(3)  # Adjust the delay as needed






# import time
# import json
# import os
# import requests

# # Directory containing JSON files
# output_dir = "robot_jsons"
# server_url = "http://127.0.0.1:5211/receive_data"

# # Wait for the server to start JSON sending
# def wait_for_start_signal():
#     while True:
#         try:
#             response = requests.get("http://127.0.0.1:5211/start_json_sending")
#             if response.status_code == 200:
#                 print("✅ Received start signal. Starting JSON sending...")
#                 break
#         except requests.exceptions.ConnectionError:
#             print("Waiting for server to start...")
#         time.sleep(2)

# # Get all JSON files sorted numerically
# json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")], key=lambda f: int(f.split("_")[-1].split(".")[0]))

# # Wait for the start signal
# wait_for_start_signal()

# # Send each JSON file one by one
# for file in json_files:
#     file_path = os.path.join(output_dir, file)

#     with open(file_path, "r") as f:
#         data = json.load(f)
    
#     # Wrap the data in a list (as required by the server)
#     data_list = [data]

#     # Send the data in a POST request
#     response = requests.post(server_url, json=data_list)

#     if response.status_code == 200:
#         print(f"✅ Successfully sent {file}!")
#     else:
#         print(f"❌ Failed to send {file} - Status: {response.status_code}")

#     # Delay between sending each request
#     time.sleep(5)  # Adjust the delay as needed


# import time
# import json
# import os
# import requests

# # Directory containing JSON files
# output_dir = "robot_jsons"
# # server_url = "http://127.0.0.1:5211/reset"  # Your server URL
# server_url = "http://127.0.0.1:5211/receive_data"

# # Get all JSON files sorted numerically
# json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")], key=lambda f: int(f.split("_")[-1].split(".")[0]))

# # Send each JSON file one by one
# for file in json_files:
#     file_path = os.path.join(output_dir, file)

#     with open(file_path, "r") as f:
#         data = json.load(f)
    
#     # Send the data in a POST request
#     response = requests.post(server_url, json=data)  # Send the data as a JSON object (not wrapped in a list)

#     if response.status_code == 200:
#         print(f"✅ Successfully sent {file}!")
#     else:
#         print(f"❌ Failed to send {file} - Status: {response.status_code}")

#     # Delay between sending each request
#     time.sleep(5)  # Adjust the delay as needed




# import time
# import json
# import os
# import requests

# # Directory containing JSON files
# output_dir = "robot_jsons"
# server_url = "http://127.0.0.1:5211/receive_data"

# # Get all JSON files sorted numerically
# json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")], key=lambda f: int(f.split("_")[-1].split(".")[0]))

# # Send each JSON file one by one
# for file in json_files:
#     file_path = os.path.join(output_dir, file)

#     with open(file_path, "r") as f:
#         data = json.load(f)

#     # Send the data directly, without wrapping it in a list
#     response = requests.post(server_url, json=data)

#     if response.status_code == 200:
#         print(f"✅ Successfully sent {file}!")
#     else:
#         print(f"❌ Failed to send {file} - Status: {response.status_code}")

#     # Delay between sending each request
#     time.sleep(5)  # Adjust the delay as needed