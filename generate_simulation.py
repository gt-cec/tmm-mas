# Used to generate the simulation of a robot navigating through the environment with dynamic obstacles
# Outputs "robot_data_1.csv"

import random
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import csv
from matplotlib.animation import FuncAnimation

# parameters
dim = 20  # grid rows/columns
destination = (dim-1, dim-1)  # destination of the robot
num_obstacles = 10
obstacle_dim = 8

seed = "Feigh"
random.seed(seed)

def visualize_grid(robot_pos, obstacles, path, ax):
    ax.clear()  # Clear the axes to remove previous drawings

    for i in range(dim):
        for j in range(dim):
            if (i, j) == robot_pos:
                ax.add_patch(Circle((j + 0.5, i + 0.5), 0.4, color='blue'))  # Adjusted for bottom-left start
            elif (i, j) in obstacles:
                ax.add_patch(Rectangle((j, i), 1, 1, color='gray'))  # Adjusted for bottom-left start
            elif (i, j) in path:
                ax.add_patch(Circle((j + 0.5, i + 0.5), 0.2, color='green'))  # Adjusted for bottom-left start
            else:
                ax.add_patch(Rectangle((j, i), 1, 1, fill=None, edgecolor='black'))  # Adjusted for bottom-left start

    ax.set_aspect('equal', 'box')
    ax.set_xlim(0, dim)
    ax.set_ylim(0, dim)

def heuristic_cost_estimate(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def astar(start, goal, obstacles):
    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic_cost_estimate(start, goal)}

    while open_set:
        current = min(open_set, key=lambda pos: f_score.get(pos, float('inf')))
        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            return path

        open_set.remove(current)

        for neighbor in [(current[0] + 1, current[1]),
                         (current[0] - 1, current[1]),
                         (current[0], current[1] + 1),
                         (current[0], current[1] - 1)]:
            if neighbor in obstacles:
                continue  # Skip obstacles
            if neighbor[0] < 0 or neighbor[0] >= dim:
                continue
            if neighbor[1] < 0 or neighbor[1] >= dim:
                continue
            tentative_g_score = g_score.get(current, float('inf')) + 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic_cost_estimate(neighbor, goal)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None  # No path found

def log_data(frame, elapsed_time, robot_pos, path_length):
    with open('robot_data_1.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([frame, robot_pos[0], robot_pos[1], elapsed_time, path_length])

# generate obstacles
def generate_obstacles():
    obstacles = [(random.randint(0, dim), random.randint(0, dim)) for _ in range(num_obstacles)]
    _obstacles = [x for x in obstacles]
    # add additional obstacles to make them a square region
    for o in _obstacles:
        for x in range(1, obstacle_dim):
            for y in range(1, obstacle_dim):
                obstacles.append((o[0] + x, o[1]))
                obstacles.append((o[0] + x, o[1] + y))
                obstacles.append((o[0], o[1] + y))
    return list(set(obstacles))

def animate_robot():
    fig, ax = plt.subplots()
    frames = []

    def update(frame):
        nonlocal robot_pos, obstacles

        if robot_pos == destination:
            return
        
        elapsed_time = time.time() - start_time

        # Generate obstacles only once
        path = None
        
        # generate the path until it succeeds (no obstacles blocking
        while path is None:
            if frame % 3 == 0:
                obstacles = generate_obstacles()

            path = astar(robot_pos, destination, obstacles)

        visualize_grid(robot_pos, obstacles, path, ax)

        if path:
            robot_pos = path.pop(0)

        log_data(frame, elapsed_time, robot_pos, len(path))  # Log data for each frame
        frames.append([frame, robot_pos[0], robot_pos[1], elapsed_time])
        print(f"Frame {frame} - Elapsed Time: {elapsed_time:.2f}s - Robot position: {robot_pos} - Path Length: {len(path)}")

    robot_pos = (0, 0)
    obstacles = []
    start_time = time.time()

    ani = FuncAnimation(fig, update, frames=range(1, dim * 5), interval=2500)
    ani.save("robot_animation.mp4", fps=2)


if __name__ == "__main__":
    animate_robot()
