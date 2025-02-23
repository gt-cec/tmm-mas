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




from flask import Flask, request, jsonify
import json
app = Flask(__name__)




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


# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         for idx, robot_data in enumerate(data):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {robot_data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data['robots']['robot1']['x']}, {robot_data['robots']['robot1']['y']})")
#             print(f"🎯 Immediate Goal: {robot_data['robots']['robot1']['immediate goal']}")
#             print(f"📊 Plan Progress: {robot_data['robots']['robot1']['plan index']}/{len(robot_data['robots']['robot1']['plan'])}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500
    



# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Log the full incoming data for debugging
#         print("Received JSON Data:", json.dumps(data, indent=4))

#         for idx, robot_data in enumerate(data["robots"].values()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data['x']}, {robot_data['y']})")
#             print(f"🎯 Immediate Goal: {robot_data['immediate_goal']}")
#             print(f"📊 Plan Progress: {robot_data['plan_index']}/{len(robot_data['plan'])}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500


# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Print only the necessary information for each robot
#         for idx, robot_data in enumerate(data["robots"].values()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data['x']}, {robot_data['y']})")
#             print(f"🎯 Plan Index: {robot_data['plan_index']}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500

# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Iterate through robots correctly by ensuring you're accessing dictionary values
#         for idx, (robot_id, robot_data) in enumerate(data["robots"].items()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data['x']}, {robot_data['y']})")
#             print(f"🎯 Plan Index: {robot_data['plan_index']}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500



# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Log the full incoming data for debugging
#         print("Received JSON Data:")
#         print(json.dumps(data, indent=4))

#         # Try to access the robots data, check if it's a list or dict
#         if "robots" not in data:
#             raise ValueError("Missing 'robots' in the data.")

#         # Now let's print and debug the structure of robots
#         for idx, (robot_id, robot_data) in enumerate(data["robots"].items()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data.get('x', 'N/A')}, {robot_data.get('y', 'N/A')})")
#             print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500



# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Print the full received data for debugging
#         print(f"🔍 Received data: {data}")

#         # Check if 'robots' is a list or a dictionary
#         if isinstance(data['robots'], list):
#             print("robots is a list")
#         elif isinstance(data['robots'], dict):
#             print("robots is a dictionary")
#         else:
#             print("robots is neither a list nor a dictionary")

#         # Assuming robots is a dictionary with keys like 'robot1', 'robot2', etc.
#         for idx, (robot_id, robot_data) in enumerate(data["robots"].items()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"🗺️ Current Position: ({robot_data['x']}, {robot_data['y']})")
#             print(f"🎯 Plan Index: {robot_data['plan_index']}")
        
#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500


# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Log the simulation time once
#         print(f"📅 Simulation Time: {data['simulator time']}s")

#         # Assuming robots is a dictionary with keys like 'robot1', 'robot2', etc.
#         for idx, (robot_id, robot_data) in enumerate(data["robots"].items()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"🗺️ Current Position: ({robot_data['x']}, {robot_data['y']})")
#             print(f"🎯 Plan Index: {robot_data['plan_index']}")
        
#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500



# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5211, debug=False)



# from flask import Flask, request, jsonify
# import json

# app = Flask(__name__)

# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         # Get the JSON data from the incoming request
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Log the full incoming data for debugging (optional)
#         print("Received JSON Data:")
#         print(json.dumps(data, indent=4))

#         # Check if the 'robots' key is present in the received data
#         if "robots" not in data:
#             raise ValueError("Missing 'robots' in the data.")

#         # Process and print robot data
#         for idx, (robot_id, robot_data) in enumerate(data["robots"].items()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data.get('x', 'N/A')}, {robot_data.get('y', 'N/A')})")
#             print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         # Return the error in JSON format if something goes wrong
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5211)


# from flask import Flask, request, jsonify
# import json

# app = Flask(__name__)

# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         # Get the JSON data from the incoming request
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Log the full incoming data for debugging (optional)
#         print("Received JSON Data:")
#         print(json.dumps(data, indent=4))

#         # Handle the case where the data is a list
#         if isinstance(data, list) and len(data) > 0:
#             data = data[0]  # Get the first item if the top level is a list

#         # Check if 'robots' key is present
#         if "robots" not in data:
#             raise ValueError("Missing 'robots' in the data.")

#         # Process and print robot data
#         for idx, (robot_id, robot_data) in enumerate(data["robots"].items()):
#             print(f"\n🚀 Data Received (Robot {idx + 1}):")
#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data.get('x', 'N/A')}, {robot_data.get('y', 'N/A')})")
#             print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         # Return the error in JSON format if something goes wrong
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5211)



# from flask import Flask, request, jsonify
# import json

# app = Flask(__name__)

# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         # Get the JSON data from the incoming request
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Log the full incoming data for debugging (optional)
#         # print("Received JSON Data:")
#         # print(json.dumps(data, indent=4))

#         # Handle the case where the data is a list (your incoming data might be a list of dictionaries)
#         if isinstance(data, list) and len(data) > 0:
#             data = data[0]  # Get the first item if the top level is a list

#         # Check if 'robots' key is present
#         if "robots" not in data:
#             raise ValueError("Missing 'robots' in the data.")

#         # Process and print robot data for all robots in the 'robots' key
#         for robot_id, robot_data in data["robots"].items():
#             print(f"\n🚀 Data Received (Robot ID: {robot_id}):")
#             # print(f"📅 Simulator Time: {data['simulator time']}s")
#             # print(f"📍 Current Position: ({robot_data.get('x', 'N/A')}, {robot_data.get('y', 'N/A')})")
#             # print(f"🎯 Immediate Goal: {robot_data.get('immediate_goal', 'N/A')}")
#             # print(f"🔢 Plan: {robot_data.get('plan', 'N/A')}")
#             # print(f"⏳ Mission Time: {robot_data.get('mission_time', 'N/A')} seconds")
#             # print(f"📊 Plan Index: {robot_data.get('plan_index', 'N/A')}\n")

#             print(f"📅 Simulation Time: {data['simulator time']}s")
#             print(f"📍 Current Position: ({robot_data.get('x', 'N/A')}, {robot_data.get('y', 'N/A')})")
#             print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")

#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         # Return the error in JSON format if something goes wrong
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5211)







# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         # Get the JSON data from the incoming request
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Check if 'robots' key is present
#         if not isinstance(data, list):
#             raise ValueError("Data should be a list of JSONs.")

#         if len(data) == 0:
#             raise ValueError("No data found in the list.")

#         # Process and print robot data for all robots in all JSON objects in the list
#         for index, json_obj in enumerate(data):
#             if "robots" not in json_obj:
#                 raise ValueError(f"Missing 'robots' in data at index {index}.")

#             print(f"\n🚀 Data Received from JSON {index + 1}:")
#             for robot_id, robot_data in json_obj["robots"].items():
#                 print(f"\n🚀 Data Received (Robot ID: {robot_id}):")
#                 print(f"📅 Simulation Time: {json_obj.get('simulator time', 'N/A')}s")
#                 print(f"📍 Current Position: (x: {robot_data['x'][0]}, y: {robot_data['y'][1]})")
#                 print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")
            
#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         # Return the error in JSON format if something goes wrong
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500


# @app.route("/receive_data", methods=["POST"])
# def receive_data():
#     try:
#         # Get the JSON data from the incoming request
#         data = request.json
#         if not data:
#             raise ValueError("No JSON data received")

#         # Log the received data for debugging
#         print(f"Received data: {json.dumps(data, indent=4)}")

#         # Check if 'robots' key is present
#         if not isinstance(data, list):
#             raise ValueError("Data should be a list of JSONs.")

#         if len(data) == 0:
#             raise ValueError("No data found in the list.")

#         # Process and print robot data for all robots in all JSON objects in the list
#         for index, json_obj in enumerate(data):
#             if "robots" not in json_obj:
#                 raise ValueError(f"Missing 'robots' in data at index {index}.")

#             print(f"\n🚀 Data Received from JSON {index + 1}:")
#             for robot_id, robot_data in json_obj["robots"].items():
#                 print(f"\n🚀 Data Received (Robot ID: {robot_id}):")
#                 print(f"📅 Simulation Time: {json_obj.get('simulator time', 'N/A')}s")
#                 print(f"📍 Current Position: (x: {robot_data['x'][0]}, y: {robot_data['y'][1]})")
#                 print(f"🎯 Plan Index: {robot_data.get('plan_index', 'N/A')}")
            
#         return jsonify({"message": "All data received successfully!"}), 200

#     except Exception as e:
#         # Return the error in JSON format if something goes wrong
#         print(f"❌ Error: {e}")
#         return jsonify({"message": "Failed to process data", "error": str(e)}), 500



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

