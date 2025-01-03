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
import numpy as np
import csv

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
from interfaces_hmm_sim.msg import AgentPoses

import drone

####################################################################################################
##### User Inputs #####

## File Paths

key_path = "./example/grid.csv" #File describing the world grid
coord_path = "./example/coords_final.csv" #File describing the path plan
usd_path = "./environments/Small_Enviornment-Multiagent.usd" #File with the world enfironment

## Isaac Sim Paths

quad_path1 = "/World/quads/quad1" #Path to drone in the environment USD
quad_path2 = "/World/quads/quad2"
quad_path3 = "/World/quads/quad3"
quad_path4 = "/World/quads/quad4"

quad_path_list = [quad_path1, quad_path2, quad_path3, quad_path4]

## Define Bumps

bumps = [(3,1),(4,1),(5,2),(5,3),(2,4),(3,4)] #Difficult terrain points as list of ordered pairs: (y,x)

####################################################################################################

## ROS2 Setup

rclpy.init()
node = rclpy.create_node('drone_pose_publisher')
pose_publisher = node.create_publisher(AgentPoses, 'drone_poses', 10)

# Listener for /robot1/replanning_response 
# Prefix + suffix

## Initialize World

open_stage(usd_path)
world = World()

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

## Import Path Plan
coordN = 0
with open(coord_path,mode='r')as file:
    coord_file = csv.reader(file)
    coordN = sum(1 for row in coord_file)

header_coords = list()
y_grid = np.zeros((1,coordN))
x_grid = np.zeros((1,coordN))
with open(coord_path,mode='r')as file:
    coord_file = csv.reader(file)
    line_count = 0
    for lines in coord_file:
        if line_count == 0:
            y_grid[0][0] = 0
            x_grid[0][0] = 0
            header_coords = lines
        else:
            coord_line = [int(i) for i in lines]
            # print(coord_line)
            y_grid[0][line_count] = coord_line[0]
            x_grid[0][line_count] = coord_line[1]
            
            # coords[line_count-1] = coord_line[1:]
            # print(key_line)
        line_count += 1

## Drone Path Plan
# y_grid = [0,0,4,4,5,5,5,5,4,4,1,1,0,0,0,1,1,0,0] # Grid x-values
# x_grid = [0,1,1,3,3,5,0,3,3,4,4,2,2,3,2,2,1,1,0] # Grid y-values
y_grid_init = np.uint32(y_grid).tolist()[0]
x_grid_init = np.uint32(x_grid).tolist()[0]

# dz = [1,1,3,1,3,1,3,3,1,1,1,1,1,1,1,1,1,1,1]
dz = np.ones((1,len(y_grid_init)))

coords = []
count = 0
for i in y_grid_init:
    coords.append((i,x_grid_init[count]))
    count += 1

count_b = 0
for i in coords:
    # print(i)
    if i in bumps:
        dz[0][count_b] = 3
        # print('in')
    count_b += 1

# print(dz)
dz_init = np.uint32(dz).tolist()[0]
# dind = 0

dz = []
y_grid = []
x_grid = []
prev_state = 99
state_ind = 0
for i in y_grid_init:
    state = 0
    if state_ind == 0:
        print('Simplifying coords')
    else: 
        if y_grid_init[state_ind] - y_grid_init[state_ind-1] > 0:
            state = 1
        elif y_grid_init[state_ind] - y_grid_init[state_ind-1] < 0:
            state = 3
        elif x_grid_init[state_ind] - x_grid_init[state_ind-1] > 0:
            state = 2
        elif x_grid_init[state_ind] - x_grid_init[state_ind-1] < 0:
            state = 4
        elif dz_init[state_ind] - dz_init[state_ind-1] > 0:
            state = 5
        elif dz_init[state_ind] - dz_init[state_ind-1] < 0:
            state = 6
        else: state = 0

        if np.abs(state - prev_state) > 0:
            y_grid.append(y_grid_init[state_ind-1])
            x_grid.append(x_grid_init[state_ind-1])
            dz.append(dz_init[state_ind-1])

    prev_state = state
    state_ind += 1

print(f'dy: {y_grid}')
print(f'dx: {x_grid}')
y_grid.append(2)
y_grid.append(1)
x_grid.append(4)
x_grid.append(4)
dz.append(3)
dz.append(1)

# dy = [key[i][0] for i in y_grid]
# dx = [key[i][1] for i in x_grid]

y_grid1 = y_grid
x_grid1 = x_grid
dz1 =  dz

y_grid2 = [2, 3, 3, 1, 1, 0, 0, 0, 0, 0, 2]
x_grid2 = [2, 2, 4, 4, 1, 1, 0, 1, 0, 1, 1]
dz2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

y_grid3 = [3, 3, 1, 1, 4, 4, 4, 1, 1, 4, 4, 4, 3, 3]
x_grid3 = [2, 5, 5, 0, 0, 1, 5, 5, 0, 0, 1, 5, 5, 2]
dz3 = [1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1]

y_grid4 = [0, 0, 0, 0]
x_grid4 = [4, 5, 4, 5]
dz4 = [1, 1, 1, 1]

x_grid_list = [x_grid1, x_grid2, x_grid3, x_grid4]
y_grid_list = [y_grid1, y_grid2, y_grid3, y_grid4]
dz_list = [dz1, dz2, dz3, dz4]

####################################################################################################
##### Drone Controller Parameters #####

## Simple PID Gains
kp = 5
kp_z = 2
kd = 2
kd_z = 0.5

PID = [kp,0,kd]
zPID = [kp_z,0,kd_z]

####################################################################################################
##### Initializations #####

start = False
goal_reached = False

stage = omni.usd.get_context().get_stage()
dc=_dynamic_control.acquire_dynamic_control_interface()

## Create drone object
quad_list = []
finalgoal_check = []
quad_count = 1
for path in quad_path_list:
    drone_new = drone.Drone(f"quad{quad_count}",quad_path_list[quad_count-1],PID,zPID)
    drone_new.setPath(x_grid_list[quad_count-1],y_grid_list[quad_count-1],dz_list[quad_count-1],key)

    quad_new = {
        "info": drone_new,
        "prim": Articulation(drone_new.path, name=drone_new.name),
        "rb": UsdPhysics.RigidBodyAPI.Get(stage, drone_new.path)
    }
    finalgoal_check.append(False)
    quad_list.append(quad_new)
    quad_count += 1


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

def print_state(name,gp,d,dind,v,goal):
    if not goal:
        # print('Going to pose...')
        print(f'Quad: {name}')
        print(f'Global Pose: {gp}')
        # print(f'Goal Point: {dind}')
        print(f'Goal: ({d[0]}, {d[1]}, {d[2]})')
        # print(f'Velocity: {v[0]},{v[1]},{v[2]}')
        print('-------------------------------------')
        
####################################################################################################
##### Main Code #####

world.reset()
# rate = node.create_rate(1000) # Settings a rate too low may cause the simulation to crash
                                # It is probably better to keep this off unless needed

while rclpy.ok():
    rclpy.spin_once(node, timeout_sec=0)
    appwindow = omni.appwindow.get_default_app_window()
    input = carb.input.acquire_input_interface()
    input.subscribe_to_keyboard_events(appwindow.get_keyboard(), keyboard_event)

    drone_poses_msg = AgentPoses()

    drone_count = 0
    if start:
        for quad in quad_list:
            drone_obj = quad["info"]
        
        
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
                if np.abs(delx) <= 0.5 and np.abs(dely) <= 0.5 and np.abs(delz) <= 0.05:
                    # vx = 0
                    # vy = 0
                    # vz = 0
                    drone_obj.dind +=1
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
                
                print_state(drone_obj.name,global_pose,d_curr,dind,v_curr,goal_reached)
                if np.all(np.array(finalgoal_check)):
                    print("All goals reach!")
                    start = not start
            else:
                finalgoal_check[drone_count] = True

                vel = Gf.Vec3f(0,0,0)
                quad["rb"].GetVelocityAttr().Set(vel)

            quad["info"] = drone_obj
            drone_count += 1

        # Publish drone poses
        pose_publisher.publish(drone_poses_msg)
        # rate.sleep() # See comment about rate above

    else:
        vel = Gf.Vec3f(0,0,0)
        for quad in quad_list:
            quad["rb"].GetVelocityAttr().Set(vel) 
        

    world.step(render=True)

simulation_app.close()
rclpy.shutdown()
