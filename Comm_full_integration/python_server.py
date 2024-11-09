
#Final
import asyncio
import websockets
import pandas as pd
import nest_asyncio
import time  # Import time module for delay

# Allow asyncio to work inside Jupyter or similar environments
nest_asyncio.apply()

# Path to the input CSV file
# input_file_path = 'robot_data_10 1.csv'
input_file_path = 'RMM.csv'

# WebSocket server logic to process and send data in real-time
async def websocket_server(websocket, path):
    print("Client connected")
    
    # Read and process the input CSV file in real-time
    df = pd.read_csv(input_file_path, header=None)
    
    try:
        # Process and send each row dynamically
        for i, row in df.iterrows():
            # Process each row (transform the data)
            pos = eval(row[0])  # Evaluate the position tuple (x, y)
            index = i + 1  # Create index starting from 1
            position_x = pos[0]
            position_y = pos[1]
            time_taken = float(row[1])
            steps_remaining = int(row[2])
            
            # Prepare the processed data as a list of strings
            processed_data = [
                str(index),
                str(position_x),
                str(position_y),
                str(time_taken),
                str(steps_remaining)
            ]
            
            # Send the processed data to the client as a string
            await websocket.send(str(processed_data))
            print(f"Sent row {index} to client: {processed_data}")

            # Add a small delay to allow client to process data
            await asyncio.sleep(0.4)  # Wait for 0.5 seconds before sending the next message

            # await asyncio.sleep(4)  # Wait for 0.5 seconds before sending the next message

        # After sending all rows, stop further communication
        print("Finished sending all data to client")

    except websockets.exceptions.ConnectionClosed:
        print("Connection closed")

# Start the WebSocket server on port 7000
start_server = websockets.serve(websocket_server, "localhost", 7000)

print("WebSocket server running on ws://localhost:7000")

# Await the server to start
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

