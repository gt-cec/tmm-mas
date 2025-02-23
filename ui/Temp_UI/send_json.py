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


# # All in one go!
# import time
# import json
# import os
# import requests

# # Directory containing JSON files
# output_dir = "robot_jsons"
# # server_url = "http://127.0.0.1:5000/receive_data"
# server_url = "http://127.0.0.1:5211/receive_data"

# # Get all JSON files
# json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")])

# # Read all JSON files into a list
# json_data = []
# for file in json_files:
#     file_path = os.path.join(output_dir, file)
    
#     with open(file_path, "r") as f:
#         data = json.load(f)
#         json_data.append(data)

# # Send all JSON data in one request
# response = requests.post(server_url, json=json_data)

# if response.status_code == 200:
#     print("✅ All JSON files sent successfully!")
# else:
#     print(f"❌ Failed to send data - Status: {response.status_code}")

#     time.sleep(5)



# import time
# import json
# import os
# import requests

# # Directory containing JSON files
# output_dir = "robot_jsons"
# # server_url = "http://127.0.0.1:5000/receive_data"
# server_url = "http://127.0.0.1:5211/receive_data"

# # Get all JSON files sorted numerically
# json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")], key=lambda f: int(f.split("_")[-1].split(".")[0]))

# # Send each JSON file one by one
# for file in json_files:
#     file_path = os.path.join(output_dir, file)

#     with open(file_path, "r") as f:
#         data = json.load(f)

#     # Send the data in a POST request
#     response = requests.post(server_url, json=data)

#     if response.status_code == 200:
#         print(f"✅ Successfully sent {file}!")
#     else:
#         print(f"❌ Failed to send {file} - Status: {response.status_code}")

#     # Delay between sending each request
#     time.sleep(4)  # Adjust the delay as needed




import time
import json
import os
import requests

# Directory containing JSON files
output_dir = "robot_jsons"
# server_url = "http://127.0.0.1:5000/receive_data"
server_url = "http://127.0.0.1:5211/receive_data"

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
    time.sleep(5)  # Adjust the delay as needed
