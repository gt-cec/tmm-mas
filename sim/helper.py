import numpy
import json

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

def print_state(name,gp,d,dind,v,goal):
    if not goal:
        # print('Going to pose...')
        print(f'Quad: {name}')
        print(f'Global Pose: {gp}')
        print(f'Goal: ({d[0]}, {d[1]}, {d[2]})')
        print(f'Path Step: {dind}')
        # print(f'Velocity: {v[0]},{v[1]},{v[2]}')
        print('-------------------------------------')

# def save_robot_data(robot_name, action_sequence, bumps, file_name):
#     # Call the parse_action_sequence function
#     x_coords, y_coords, z_coords, flags = parse_action_sequence(action_sequence, bumps)

#     # Create a dictionary with the results
#     robot_data = {
#         "robot_name": robot_name,
#         "x_coords": x_coords,
#         "y_coords": y_coords,
#         "z_coords": z_coords,
#         "flags": flags
#     }

#     # Save the dictionary as a JSON file
#     with open(file_name, 'w') as json_file:
#         json.dump(robot_data, json_file, indent=4)

#     print(f"Data for robot '{robot_name}' saved to {file_name}.")

def save_robot_data(robot_name, action_sequence, bumps, file_name):
    # Call the parse_action_sequence function
    x_coords, y_coords, z_coords, flags = parse_action_sequence(action_sequence, bumps)

    # Create a dictionary with the results
    robot_data = {
        "robot_name": robot_name,
        "x_coords": x_coords,
        "y_coords": y_coords,
        "z_coords": z_coords,
        "flags": flags
    }

    # Save the dictionary as a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(robot_data, json_file, indent=4)

    print(f"Data for robot '{robot_name}' saved to {file_name}.")