# Multi-Robot JSON Server

This project is a Flask-based server that processes JSON data for multi-robot operations. It simulates the behavior of robots and updates their states based on incoming JSON data. The server uses WebSocket communication to emit real-time updates to connected clients.

## Features

- **Real-time Robot State Updates**: The server processes JSON data and emits updated robot states to connected clients in real-time.
- **Multi-Robot Support**: Handles data for multiple robots (e.g., `quad1`, `quad2`, `quad3`).
- **Dynamic Mission Updates**: Updates robot mission times and positions dynamically based on incoming data.
- **WebSocket Integration**: Uses Flask-SocketIO for real-time communication between the server and clients.

## Prerequisites

Before running the server, ensure you have the following installed:

- Python 3.10 or higher
- Flask (`pip install flask`)
- Flask-SocketIO (`pip install flask-socketio`)
- Pandas (`pip install pandas`)
- Other dependencies as specified in `multirobot_operation_functions.py`

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:gt-cec/tmm-mas.git
   cd tmm-mas/ui/Temp_Ui

   
2. Running the Server
Start the server by running the following command:


   ```bash
    python final_receiver_server_json.py

The server will start on http://0.0.0.0:5211. You can access it via http://127.0.0.1:5211 in your browser.

3. Sending JSON Data
To send JSON data to the server, use the send_json.py script. This script reads JSON files from a directory (robot_jsons) and sends them to the server one by one.

Place your JSON files in the robot_jsons directory. Ensure the files are named in a sequential order (e.g., robot_1.json, robot_2.json, etc.).

Run the send_json.py script:
   ```bash
    python send_json.py