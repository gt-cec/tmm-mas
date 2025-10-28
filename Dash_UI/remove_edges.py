import os
import json

# Define the base directory containing the scenario folders
base_dir = 'scenarios_with_graphs'

# Loop through each scenario folder (scenario_1 to scenario_6)
for i in range(1, 7):
    scenario_folder = os.path.join(base_dir, f'scenario_{i}')

    # Check if the scenario folder actually exists
    if not os.path.isdir(scenario_folder):
        print(f"Warning: Folder not found - {scenario_folder}")
        continue # Skip to the next scenario if folder doesn't exist

    print(f"Processing folder: {scenario_folder}")

    # Loop through all files in the current scenario folder
    for filename in os.listdir(scenario_folder):
        # Check if the file is a JSON file and follows the frame naming pattern
        if filename.startswith('frame_') and filename.endswith('.json'):
            file_path = os.path.join(scenario_folder, filename)

            try:
                # Open and load the JSON data from the file
                with open(file_path, 'r') as f:
                    data = json.load(f)

                # Check if the 'edges' key exists and remove it if it does
                if 'edges' in data:
                    del data['edges']
                    print(f"  Removed 'edges' from {filename}")

                    # Open the file again in write mode to overwrite it
                    with open(file_path, 'w') as f:
                        # Write the modified data back to the file
                        # Use indent=4 for pretty printing (optional, but makes files readable)
                        json.dump(data, f, indent=4)
                else:
                    # Optional: Print a message if 'edges' key was not found
                    # print(f"  'edges' key not found in {filename}")
                    pass


            except json.JSONDecodeError:
                print(f"  Error: Could not decode JSON from {filename}")
            except Exception as e:
                print(f"  An unexpected error occurred with {filename}: {e}")

print("\nProcessing complete.")