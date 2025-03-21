import numpy
import json
import csv
import yaml
import time

def elapsed_time(start_time):
    return time.time() - start_time

def parse_action_sequence(action_sequence, bumps):
    x_coords = []
    y_coords = []
    z_coords = []
    flags = []

    last_x, last_y = None, None

    for action in action_sequence:
        z = 2  # Default z value

        if action.startswith("goto_c"):
            parts = action.split("_r")
            x = int(parts[0].split("c")[-1])
            y = int(parts[1])
            flag = 'g'
            if (x, y) in bumps:
                z = 3  # Bump condition
        elif action == "load":
            x, y = last_x, last_y
            flag = 'l'
            z = 1  # Load condition
        elif action == "unload":
            x, y = last_x, last_y
            flag = 'u'
            z = 1.5  # Unload condition
        elif action == "stay":
            x, y = last_x, last_y
            flag = 's'
            z = 0.5  # Stay condition
        else:
            continue

        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
        flags.append(flag)

        last_x, last_y = x, y

    return x_coords, y_coords, z_coords, flags

def parse_action_sequence_from_yaml(file_path, bumps):

    # Load the YAML file
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    # Extract the action sequence
    action_sequence = data.get('action_sequence', [])

    x_coords = []
    y_coords = []
    z_coords = []
    flags = []

    last_x, last_y = None, None

    for action in action_sequence:
        z = 2  # Default z value

        if action.startswith("goto_c"):
            parts = action.split("_r")
            x = int(parts[0].split("c")[-1])
            y = int(parts[1])
            flag = 'g'
            if (x, y) in bumps:
                z = 3  # Bump condition
        elif action == "load":
            x, y = last_x, last_y
            flag = 'l'
            z = 1  # Load condition
        elif action == "unload":
            x, y = last_x, last_y
            flag = 'u'
            z = 1.5  # Unload condition
        elif action == "stay":
            x, y = last_x, last_y
            flag = 's'
            z = 0.5  # Stay condition
        else:
            continue

        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
        flags.append(flag)

        last_x, last_y = x, y

    return x_coords, y_coords, z_coords, flags

def save_action_sequence_to_csv(file_path, bumps, output_csv):

    x_coords, y_coords, z_coords, flags = parse_action_sequence_from_yaml(file_path, bumps)

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(["x", "y", "z", "flag"])
        # Write the rows
        for x, y, z, flag in zip(x_coords, y_coords, z_coords, flags):
            writer.writerow([x, y, z, flag])

def print_state(name,gp,d,dind,v,goal):
    if not goal:
        # print('Going to pose...')
        print(f'Quad: {name}')
        print(f'Global Pose: {gp}')
        print(f'Goal: ({d[0]}, {d[1]}, {d[2]})')
        print(f'Path Step: {dind}')
        # print(f'Velocity: {v[0]},{v[1]},{v[2]}')
        print('-------------------------------------')

def read_selected_columns(file_path, columns):

    extracted_columns = {col: [] for col in columns}

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for col in columns:
                if col in row:
                    value = row[col]
                    if col in ["x", "y"]:  # Convert x, y to int
                        extracted_columns[col].append(int(value))
                    elif col == "z":  # Convert z to float
                        extracted_columns[col].append(float(value))
                    else:
                        extracted_columns[col].append(value)

    return tuple(extracted_columns[col] for col in columns)

def load_replans(file_path):

    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    
    action_sequences = {}
    
    for key, value in data.items():
        action_sequences[key] = value.get("action_sequence", [])
    
    return action_sequences