
from flask import Flask, request, jsonify
import json

app = Flask(__name__)




@app.route("/receive_data", methods=["POST"])
def receive_data():
    try:
        # Get the JSON data from the incoming request
        data = request.json
        if not data:
            raise ValueError("No JSON data received")

        # Log the full incoming data for debugging (optional)
        # print("Received JSON Data:")
        # print(json.dumps(data, indent=4))

        # Check if 'robots' key is present
        if not isinstance(data, list):
            raise ValueError("Data should be a list of JSONs.")

        if len(data) == 0:
            raise ValueError("No data found in the list.")

        # Process and print robot data for all robots in all JSON objects in the list
        for index, json_obj in enumerate(data):
            if "robots" not in json_obj:
                raise ValueError(f"Missing 'robots' in data at index {index}.")
            
            print(f"\n🚀 JSON Data Received ")
            for robot_id, robot_data in json_obj["robots"].items():
                print(f"\n🚀 Data Received (Robot ID: {robot_id}):")
                print(f"📅 Simulation Time: {json_obj.get('simulator time', 'N/A')}s")
                print(f"📍 Current Position: (x: {robot_data['x'][0]}, y: {robot_data['y'][1]})")
                print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")
            
        return jsonify({"message": "All data received successfully!"}), 200

    except Exception as e:
        # Return the error in JSON format if something goes wrong
        print(f"❌ Error: {e}")
        return jsonify({"message": "Failed to process data", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5211)

