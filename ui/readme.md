

# Robot Monitoring and communication System

This project simulates robot movement and updates the communication between a robot's system and a simulated mental model framework. The web interface visualizes the robot's movement and includes a communication box to display updates based on dynamic thresholds. The system consists of three main Python scripts and a front-end HTML interface. The system includes a Flask server to handle API requests and a WebSocket server to stream data in real-time. It also includes functions to handle array generation, deviation thresholding, and probabilistic updates for robot missions

## Project Structure

- **server.py**: Runs a Flask server with two main endpoints. The `/process` endpoint handles JSON POST requests for real-time robot monitoring, and the `/reset` endpoint resets the mission time to its initial state. Also runs a websocket server that can be triggered to send mock data to the client
- **operation_functions.py**: Contains utility functions for generating RMM and HMM arrays, selecting data based on timesteps, and calculating updates for robot mission monitoring.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/gt-cec/tmm-mas.git
    cd tmm-mas
    ```

## Requirements

- Python 3.8 or higher

## Setup Instructions

### 1. Install Dependencies

1. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Ensure the input data file (e.g., `robot_data_10 1.csv` or `RMM.csv`) is in the root directory of the repository.

## Usage

### Websocket server
To start the Websocket server:

`python server.py`

In a web browser, open `127.0.0.1:8080`
