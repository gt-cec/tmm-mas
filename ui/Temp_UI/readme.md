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
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

   

