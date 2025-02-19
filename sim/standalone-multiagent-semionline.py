###################################
##### Simple Drone Simulation #####
#####     using Isaac Sim     #####
###################################
#####      Haris Miller       #####
#####     GA Tech - LIDAR     #####
###################################

from omni.isaac.kit import SimulationApp

## Start Simulation
CONFIG = {"width": 2560, "height": 1440, "window_width": 3840, "window_height": 2160, "sync_loads": True, "headless": False, "renderer": "RayTracedLighting"}
simulation_app = SimulationApp(CONFIG)

####################################################################################################

import argparse
import sys
import time
import numpy as np
import csv
import json

import carb
import omni

from omni.isaac.core import World
from omni.isaac.core.utils.stage import open_stage

from omni.isaac.dynamic_control import _dynamic_control
from omni.isaac.core.articulations import Articulation

from pxr import Gf, UsdPhysics, Usd, UsdGeom, Sdf
import omni.usd

import rclpy
from rclpy.node import Node
from interfaces_hmm_sim.msg import AgentPoses, Status
from ltl_automaton_msgs.msg import TransitionSystemState, TransitionSystemStateStamped, LTLPlan, RelayResponse

import drone
import helper as hp
from helper import elapsed_time, parse_action_sequence, print_state, read_selected_columns

####################################################################################################
##### User Inputs #####

## File Paths

key_path = "./example/grid.csv" #File describing the world grid
usd_path = "./environments/Small_Enviornment-Multiagent.usd" #File with the world enfironment

robot1_plan = "./plans/robot1_as.csv"
robot2_plan = "./plans/robot2_as.csv"
robot3_plan = "./plans/robot3_as.csv"

robot_plans = [robot1_plan, robot2_plan, robot3_plan]

## Isaac Sim Paths

quad_path1 = "/World/quads/quad1" #Path to drone in the environment USD
quad_path2 = "/World/quads/quad2"
quad_path3 = "/World/quads/quad3"

quad_path_list = [quad_path1, quad_path2, quad_path3]

init_grid_poses = [(0,0),(4,3),(3,2)]

## Define Bumps

bumps = [(3,1),(4,1),(5,2),(5,3),(2,4),(3,4)] #Difficult terrain points as list of ordered pairs: (y,x)
blocks = [(2,2),(0,4)]

## JSON function

filename_json = "simulation_data.json"

def generate_json(start_time, robots, filname):
    data = {
        "simulator time": elapsed_time(start_time),
        "robots": {}
    }
    for robot_id, robot_data in robots.items():
        data["robots"][robot_id] = {
            "plan": robot_data["plan"],
            "plan index": robot_data["plan index"],
            "immediate goal": robot_data["immediate goal"],
            "x": robot_data["x"],
            "y": robot_data["y"]
        }
    json_output = json.dumps(data, indent=4)

    #######################################
    ### Edit these lines to output JSON ###

    with open(filname, "w") as f:
        f.write(json_output)

    #######################################

    return json_output

####################################################################################################
##### ROS2 Setup #####

num_agents = len(quad_path_list)

replan_flag = []
for path in quad_path_list:
    replan_flag.append(False)

rclpy.init()

# RelayResponse callback
def relay_response_callback(msg, agent_node):
    # idx = agent_node["number"]
    # replan_flag[idx] = True
    agent_node["new_prefix_actions"] = msg.new_plan_prefix.action_sequence
    agent_node["node"].get_logger().info(f"Received prefix actions")
    agent_node["new_suffix_actions"] = msg.new_plan_suffix.action_sequence
    agent_node["node"].get_logger().info(f"Received suffix actions")

# PrefixPlan callback
def prefix_plan_callback(msg, agent_node):
    agent_node["prefix_actions"] = msg.action_sequence
    agent_node["node"].get_logger().info(f"Received prefix plan actions")

# SuffixPlan callback
def suffix_plan_callback(msg, agent_node):
    agent_node["suffix_actions"] = msg.action_sequence
    agent_node["node"].get_logger().info(f"Received suffix plan actions")


def create_agent_nodes(num_agents):
    agent_nodes = []
    for i in range(num_agents):
        agent_name = f"robot{i + 1}"
        namespace = f"/{agent_name}"
        node = rclpy.create_node(f"isaac_node", namespace=namespace)

        # Publishers
        pose_publisher = node.create_publisher(AgentPoses, f"{namespace}/poses", 10)
        status_publisher = node.create_publisher(Status, f"{namespace}/status", 10)

        # Initialize agent-specific data
        agent_node = {
            "name": agent_name,
            "node": node,
            "number": i,
            "pose_publisher": pose_publisher,
            "status_publisher": status_publisher,
            "new_prefix_actions": [],
            "new_suffix_actions": [],
            "prefix_actions": [],
            "suffix_actions": [],
        }

        # Use closures to bind agent-specific data
        def relay_callback(msg, agent_node=agent_node):
            relay_response_callback(msg, agent_node)

        def prefix_callback(msg, agent_node=agent_node):
            prefix_plan_callback(msg, agent_node)

        def suffix_callback(msg, agent_node=agent_node):
            suffix_plan_callback(msg, agent_node)

        # Subscribers
        relay_response_subscriber = node.create_subscription(
            RelayResponse, f"{namespace}/replanning_response", relay_callback, 10
        )
        prefix_plan_subscriber = node.create_subscription(
            LTLPlan, f"{namespace}/prefix_plan", prefix_callback, 10
        )
        suffix_plan_subscriber = node.create_subscription(
            LTLPlan, f"{namespace}/suffix_plan", suffix_callback, 10
        )

        agent_node["relay_response_subscriber"] = relay_response_subscriber
        agent_node["prefix_plan_subscriber"] = prefix_plan_subscriber
        agent_node["suffix_plan_subscriber"] = suffix_plan_subscriber

        agent_nodes.append(agent_node)

    return agent_nodes


agent_nodes = create_agent_nodes(num_agents)
print("ROS2 Nodes initialized!")

####################################################################################################
##### Develop Grid #####

## Import Grid Reference
keyN = 0
with open(key_path,mode='r')as file:
    key_file = csv.reader(file)
    keyN = sum(1 for row in key_file)

header = list()
key = np.zeros((keyN-1,2))
with open(key_path,mode='r')as file:
    key_file = csv.reader(file)
    line_count = 0
    for lines in key_file:
        if line_count == 0:
            header = lines
        else:
            key_line = [int(i) for i in lines]
            key[line_count-1] = key_line[1:]
            # print(key_line)
        line_count += 1
print("Grid reference imported!")

# x_grid_list = []
# y_grid_list = []
# z_grid_list = []
# flags_list = []
# for path in robot_plans:
    

## Initialize World

open_stage(usd_path)
world = World()
print("World started!")

####################################################################################################
##### Drone Controller Parameters #####

## Simple PID Gains
kp = 6
kp_z = 2
kd = 2
kd_z = 0.5

PID = [kp,0,kd]
zPID = [kp_z,0,kd_z]

####################################################################################################
##### Initializations #####

start_time = time.time()
next_print_time = start_time + 10

wait_val = 40

start = False
init_paths = False
goal_reached = False

stage = omni.usd.get_context().get_stage()
dc=_dynamic_control.acquire_dynamic_control_interface()

## Create drone object
quad_list = []
finalgoal_check = []
init_start = []
wait_count = []
quad_count = 1
robots_JSON = {}
        
for path in quad_path_list:
    print(f"Initializing quad{quad_count}...")
    drone_new = drone.Drone(f"quad{quad_count}",quad_path_list[quad_count-1],PID,zPID)
    columns_to_read = ["x", "y", "z", "flag"]
    x_coords, y_coords, z_coords, flags = read_selected_columns(robot_plans[quad_count-1], columns_to_read)
    drone_new.setPath(y_coords, x_coords, z_coords, flags, key)
    # drone_new.setPath(x_grid_list[quad_count-1],y_grid_list[quad_count-1],dz_list[quad_count-1],key)

    quad_new = {
        "info": drone_new,
        "prim": Articulation(drone_new.path, name=drone_new.name),
        "rb": UsdPhysics.RigidBodyAPI.Get(stage, drone_new.path)
    }
    finalgoal_check.append(False)
    init_start.append(False)
    quad_list.append(quad_new)
    wait_count.append(wait_val)

    robot_id = drone_new.name
    plan = drone_new.getPath()
    robots_JSON[robot_id] = {
        "plan": plan,
        "plan_index": 1,
        "immediate_goal": plan[1],
        "x": plan[0],
        "y": plan[0]
    }
    quad_count += 1
out_json = generate_json(start_time, robots_JSON, filename_json)

print("Agents created!")

####################################################################################################
##### Functions #####

def keyboard_event(event, *args, **kwargs):
    global start
    # global dind

    if event.type == carb.input.KeyboardEventType.KEY_PRESS:
        if event.input == carb.input.KeyboardInput.P:
            start = not start
        # if event.input == carb.input.KeyboardInput.R:
        #     dind = 0
        if event.input == carb.input.KeyboardInput.X:
            simulation_app.close()
        # if event.input == carb.input.KeyboardInput.K:
        #     # print('Key:\n', key)
        #     x0 = key[x_grid[dind]][1]
        #     y0 = key[y_grid[dind]][0]
        #     print('\n')
        #     print(f'Origin: {y0},{x0}')
        #     print(dx)
        #     print(dy)
        
####################################################################################################
##### Main Code #####

world.reset()
# rate = node.create_rate(1000) # Settings a rate too low may cause the simulation to crash
                                # It is probably better to keep this off unless needed
print("Sim ready!")
while rclpy.ok():
    for agent in agent_nodes:
        rclpy.spin_once(agent["node"], timeout_sec=0)
    # rclpy.spin_once(node, timeout_sec=0)
    appwindow = omni.appwindow.get_default_app_window()
    input = carb.input.acquire_input_interface()
    input.subscribe_to_keyboard_events(appwindow.get_keyboard(), keyboard_event)

    robots_JSON = {}

    if start:
        drone_count = 0
        for quad in quad_list:
            drone_obj = quad["info"]
            agent = agent_nodes[drone_count]

            drone_poses_msg = AgentPoses()
            drone_status = Status()
        
            object=dc.get_rigid_body(drone_obj.path)
            object_pose=dc.get_rigid_body_pose(object)
            global_pose,global_orient = quad["prim"].get_world_pose()

            xpose = global_pose[0]
            ypose = global_pose[1]
            zpose = global_pose[2]

            drone_obj.pose = [xpose, ypose, zpose]
            
            # print("position:", object_pose.p)
            # print("rotation:", object_pose.r)
            # d_curr = [0,0,0]
            # v_curr = [0,0,0]

            pose_prev = drone_obj.pose_prev
            del_prev = drone_obj.del_prev
            dind = drone_obj.dind

            dx = drone_obj.dx
            dy = drone_obj.dy
            dz = drone_obj.dz

            flags = drone_obj.flags

          

            if quad["rb"] and dind < len(dx):

                d_curr = [dx[dind],dy[dind],dz[dind]]
                delx = dx[dind]-global_pose[0]
                dely = dy[dind]-global_pose[1]
                delz = dz[dind]-global_pose[2]
                
                dist = np.sqrt((xpose-pose_prev[0])**2 + (ypose-pose_prev[1])**2 + (zpose-pose_prev[2])**2)


                kp_mod = kp

                if delz > 0.5:
                    kp_mod = 0.25*kp
                elif delz < -0.5 and (np.abs(delx) < 0.5 and np.abs(dely) < 0.5):
                    kp_mod = 0.25*kp
                vx = kp_mod*delx + kd*(delx - del_prev[0])
                vy = kp_mod*dely + kd*(dely - del_prev[1])
                vz = kp_z*(delz) + kd_z*(delz - del_prev[2])
                v_curr = [vx,vy,vz]
                # if (np.abs(delx) <= 1.5 and np.abs(dely) <= 1.5 and np.abs(delz) <= 0.05) and not drone_status_sent[drone_count]:
                #     drone_status.agent = agent["name"]
                #     drone_status.arrived = True
                #     agent["status_publisher"].publish(drone_status)

                #     drone_status_sent[drone_count] = True
                if (wait_count[drone_count] < wait_val):
                    
                    if not replan_flag[drone_count]:
                        goal_y = drone_obj.y_grid[dind]
                        goal_x = drone_obj.x_grid[dind]
                        goal = [goal_x,goal_y,dz[dind]]
                        print("Waiting....")
                        print_state(drone_obj.name,global_pose,goal,dind,v_curr,goal_reached)

                        wait_count[drone_count] += 1
                        replan_flag[drone_count] = True

                        drone_status.agent = agent["name"]
                        drone_status.replan_received = True
                        agent["status_publisher"].publish(drone_status)
                    
                    wait_count[drone_count] += 1

                    if (wait_count[drone_count] == (wait_val-1)):
                        print("Next...")
                        drone_obj.dind +=1

                        drone_status.agent = agent["name"]
                        drone_status.replan_received = True
                        agent["status_publisher"].publish(drone_status)

                elif (np.abs(delx) <= 0.5 and np.abs(dely) <= 0.5 and np.abs(delz) <= 0.05):
                    # vx = 0
                    # vy = 0
                    # vz = 0
                    print("Arrived!")
                    goal_y = drone_obj.y_grid[dind]
                    goal_x = drone_obj.x_grid[dind]
                    goal = [goal_x,goal_y,dz[dind]]

                    print_state(drone_obj.name,global_pose,goal,dind,v_curr,goal_reached)
                    
                    if flags[dind] == 'r':
                        wait_count[drone_count] = 0
                    else:
                        drone_obj.dind +=1
                    
                    drone_status.agent = agent["name"]
                    drone_status.arrived = True
                    agent["status_publisher"].publish(drone_status)
                vel = Gf.Vec3f(vx,vy,vz)
                quad["rb"].GetVelocityAttr().Set(vel)
                # rigid_body_api.GetAngularVelocityAttr().Set(vel)
                
                # xpose_prev = xpose
                # ypose_prev = ypose
                # zpose_prev = zpose
                drone_obj.pose_prev = [xpose, ypose, zpose]

                # delx_prev = delx
                # dely_prev = dely
                # delz_prev = delz
                drone_obj.del_prev = [delx,dely,delz]

                # Add drone pose to message
                drone_poses_msg.agents.append(drone_count+1)
                drone_poses_msg.x.append(xpose)
                drone_poses_msg.y.append(ypose)
                drone_poses_msg.z.append(zpose)
                
                # goal_y = drone_obj.y_grid[dind]
                # goal_x = drone_obj.x_grid[dind]
                # goal = [goal_x,goal_y,dz[dind]]

                # print_state(drone_obj.name,global_pose,goal,dind,v_curr,goal_reached)
                
                if np.all(np.array(finalgoal_check)):
                    print("All goals reach!")
                    start = not start
            else:
                finalgoal_check[drone_count] = True

                vel = Gf.Vec3f(0,0,0)
                quad["rb"].GetVelocityAttr().Set(vel)

            quad["info"] = drone_obj
            robot_id = drone_obj.name
            plan = drone_obj.getPath()
            curr_ind = dind if dind > 0 else 0
            robots_JSON[robot_id] = {
                "plan": plan,
                "plan_index": dind,
                "immediate_goal": plan[dind],
                "x": plan[curr_ind],
                "y": plan[curr_ind]
            }

            drone_count += 1

            # Publish drone poses
            # pose_publisher.publish(drone_poses_msg)
            # rate.sleep() # See comment about rate above

    else:
        vel = Gf.Vec3f(0,0,0)
        for quad in quad_list:
            quad["rb"].GetVelocityAttr().Set(vel) 

    current_time = time.time()
    if current_time >= next_print_time:
        json_output = generate_json(current_time, robots_JSON)
        next_print_time += 10
        

    world.step(render=True)

simulation_app.close()
rclpy.shutdown()
