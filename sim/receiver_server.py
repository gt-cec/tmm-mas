# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     data = request.json  # This will be a list of JSON objects

#     for idx, robot_data in enumerate(data):
#         print(f"\n🚀 Data Received (Robot {idx + 1}):")
#         print(f"📅 Simulation Time: {robot_data['simulator time']}s")
#         print(f"📍 Current Position: ({robot_data['robots']['robot1']['x']}, {robot_data['robots']['robot1']['y']})")
#         print(f"🎯 Immediate Goal: {robot_data['robots']['robot1']['immediate goal']}")
#         print(f"📊 Plan Progress: {robot_data['robots']['robot1']['plan index']}/{len(robot_data['robots']['robot1']['plan'])}")

#     return jsonify({"message": "All data received successfully!"}), 200

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5006, debug=False)




# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     data = request.json  # This will be a list of JSON objects

#     for idx, robot_data in enumerate(data):
#         print(f"\n🚀 Data Received (Robot {idx + 1}):")
#         print(f"📅 Simulation Time: {robot_data['simulator time']}s")
#         print(f"📍 Current Position: ({robot_data['robots']['robot1']['x']}, {robot_data['robots']['robot1']['y']})")
#         print(f"🎯 Immediate Goal: {robot_data['robots']['robot1']['immediate goal']}")
#         print(f"📊 Plan Progress: {robot_data['robots']['robot1']['plan index']}/{len(robot_data['robots']['robot1']['plan'])}")

#     return jsonify({"message": "All data received successfully!"}), 200

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5211, debug=False)


import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/receive_data", methods=["POST"])
def receive_data():
    data = request.json  # Get incoming JSON data
    print("\n🚀 Data Received:")
    print(json.dumps(data, indent=4))  # Print nicely formatted JSON
    return jsonify({"message": "Data received successfully!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5211, debug=True)
