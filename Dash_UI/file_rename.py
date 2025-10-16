import os
import re

# Define the path to the folder containing the files.
target_folder = 'scenarios_with_graphs/scenario_1'

print(f"Scanning for files in '{target_folder}'...")

try:
    all_files = os.listdir(target_folder)
except FileNotFoundError:
    print(f"Error: The folder '{target_folder}' was not found.")
    print("Please make sure the script is in the correct parent directory.")
    exit()

# --- Part 1: Rename the JSON files ---

# Filter for files that start with 'robot_data_' AND end with '.json'.
files_to_rename = [
    f for f in all_files if f.startswith('robot_data_') and f.endswith('.json')
]

# Sort the files numerically to ensure correct order (e.g., 10 after 9).
files_to_rename.sort(key=lambda x: int(re.search(r'_(\d+)\.json', x).group(1)))

if not files_to_rename:
    print("No 'robot_data_...json' files were found to rename.")
else:
    print("\n--- Renaming JSON files ---")
    # Loop through the sorted list and rename each file.
    for i, old_filename in enumerate(files_to_rename):
        frame_number = i + 1
        
        # Create the new filename, keeping the .json extension.
        new_filename = f'frame_{str(frame_number).zfill(3)}.json'
        
        old_filepath = os.path.join(target_folder, old_filename)
        new_filepath = os.path.join(target_folder, new_filename)
        
        os.rename(old_filepath, new_filepath)
        
        print(f'Renamed: "{old_filename}"  ->  "{new_filename}"')

# --- Part 2: Clean up the .Zone.Identifier files ---

# Filter for the junk identifier files.
files_to_delete = [f for f in all_files if f.endswith('.Zone.Identifier')]

if not files_to_delete:
    print("\nNo '.Zone.Identifier' files found to clean up.")
else:
    print("\n--- Deleting Identifier files ---")
    for filename in files_to_delete:
        filepath_to_delete = os.path.join(target_folder, filename)
        os.remove(filepath_to_delete)
        print(f'Deleted: "{filename}"')

print("\n✅ Script finished!")