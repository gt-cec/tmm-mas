

# Robot Monitoring and communication System

This project simulates robot movement and updates the communication between a robot's system and a simulated mental model framework. The web interface visualizes the robot's movement and includes a communication box to display updates based on dynamic thresholds. The system consists of three main Python scripts and a front-end HTML interface. The system includes a Flask server to handle API requests and a WebSocket server to stream data in real-time. It also includes functions to handle array generation, deviation thresholding, and probabilistic updates for robot missions

## Project Structure

- `Index.html`: The main HTML file for the front-end interface, which includes a canvas for the simulation and a communication box. It connects to WebSocket and REST API backends.
- **Flask_server.py**: Runs a Flask server with two main endpoints. The `/process` endpoint handles JSON POST requests for real-time robot monitoring, and the `/reset` endpoint resets the mission time to its initial state.
- **python_server.py**: Sets up a WebSocket server that reads data from a CSV file and streams it to connected clients with a delay.
- **operation_functions.py**: Contains utility functions for generating RMM and HMM arrays, selecting data based on timesteps, and calculating updates for robot mission monitoring.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gt-cec/tmm-mas.git
    cd tmm-mas
    ```


## Requirements

- Python 3.8 or higher
- Node.js (optional, if serving HTML files via a local server)

## Setup Instructions

### 1. Install Dependencies

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`




2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the input data file (e.g., `robot_data_10 1.csv` or `RMM.csv`) is in the root directory of the repository.

## Usage


### Websocket server
To start the Websocket  server:
```bash
python python_server.py


### Flask Server
To start the Flask server:
```bash
python Flask_server.py

### Front end
Open index.html in a web browser to view the simulation and communication interface.
