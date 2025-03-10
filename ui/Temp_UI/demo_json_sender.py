

# #play/stop does work
import time
import json
import os
import requests
import socketio

# output_dir = "robot_jsons"
output_dir = "updated_robot_jsons_03_08"
server_url = "http://127.0.0.1:5211/receive_data"
socket_server_url = "http://127.0.0.1:5211"

sio = socketio.Client()
is_playing = False

@sio.event
def connect():
    print("✅ Connected to WebSocket server.")

@sio.event
def disconnect():
    print("❌ Disconnected from WebSocket server.")

@sio.on("message")
def message(data):
    global is_playing
    if isinstance(data, bool):
        is_playing = data
        print(f"🟢 Play Status Updated: {is_playing}")

sio.connect(socket_server_url)

json_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".json")], key=lambda f: int(f.split("_")[-1].split(".")[0]))

print("🚀 Ready! Waiting for Play signal...")

while True:
    if is_playing:
        for file in json_files:
            file_path = os.path.join(output_dir, file)
            with open(file_path, "r") as f:
                data = json.load(f)
            response = requests.post(server_url, json=[data])

            if response.status_code == 200:
                print(f"✅ Sent {file}")
            else:
                print(f"❌ Failed to send {file} - Status: {response.status_code}")

            time.sleep(5)
            if not is_playing:
                print("⏸️ Play stopped. Pausing...")
                break
    # time.sleep(5)

