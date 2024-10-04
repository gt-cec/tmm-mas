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

####################################################################################################
##### User Inputs #####

## File Paths

key_path = r".\grid.csv" #File describing the world grid
coord_path = r".\coords_final.csv" #File describing the path plan
usd_path = r".\Small_Enviornment.usd" #File with the world enfironment
quad_path = "/World/quadx" #Path to the drone in the environment USD

## Define Bumps

bumps = [(3,1),(4,1),(5,2),(5,3),(2,4),(3,4)] #Difficult terrain points as list of ordered pairs: (y,x)

####################################################################################################

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
dind = 0

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

dy = [key[i][0] for i in y_grid]
dx = [key[i][1] for i in x_grid]


####################################################################################################
##### Drone Controller Parameters #####

delx_prev = 0
dely_prev = 0
delz_prev = 0

## Simple PID Gains
kp = 1.5
kp_z = 2
kd = 2
kd_z = 0.5

####################################################################################################
##### Initializations #####

start = False
goal_reached = False

## Store Drone Positions
xpose_prev = 0
ypose_prev = 0
zpose_prev = 0

dc=_dynamic_control.acquire_dynamic_control_interface()
stage = omni.usd.get_context().get_stage()
prim = Articulation(quad_path, name="quadx")
rigid_body_api = UsdPhysics.RigidBodyAPI.Get(stage, quad_path)

## Trace Initializations
trace_width = 0.1
trace_color = (0,0,1)
color_rev = False
trace_xform = UsdGeom.Xform.Define(stage, '/World/trace')
trace = []
trace_iter = 0

####################################################################################################
##### Functions #####

def keyboard_event(event, *args, **kwargs):
    global start
    global dind

    if event.type == carb.input.KeyboardEventType.KEY_PRESS:
        if event.input == carb.input.KeyboardInput.P:
            start = not start
        if event.input == carb.input.KeyboardInput.R:
            dind = 0
        if event.input == carb.input.KeyboardInput.X:
            simulation_app.close()
        if event.input == carb.input.KeyboardInput.K:
            # print('Key:\n', key)
            x0 = key[x_grid[dind]][1]
            y0 = key[y_grid[dind]][0]
            print('\n')
            print(f'Origin: {y0},{x0}')
            print(dx)
            print(dy)

def print_state(gp,d,dind,v,goal):
    if not goal:
        print('Going to pose...')
        print(f'Global Pose: {gp}')
        print(f'Goal Point: {dind}')
        print(f'Goal: ({d[0]}, {d[1]}, {d[2]})')
        print(f'Velocity: {v[0]},{v[1]},{v[2]}')
        print('-------------------------------------')

def iterate_color(gradient=True,N=10):
    global trace_color
    global color_rev

    if gradient:
        r_iter = 0
        g_iter = 0.05
        b_iter = 0
        rgb_iter = (r_iter,g_iter,b_iter)
        if color_rev:
            rgb_iter = (-r_iter,-g_iter,-b_iter)
        trace_color = tuple(map(lambda i, j: i + j, trace_color, rgb_iter))
        if trace_color[1] >= 0.9:
            color_rev = not color_rev
        elif trace_color[1] < 0.1:
            color_rev = not color_rev
    else:
        gb_range = 4
        iter_val = gb_range/N
        r_iter = 0
        g_iter = 0
        b_iter = 0
        if trace_color[1] < 1 and trace_color[2] >=1:
            r_iter = 0
            g_iter = iter_val
            b_iter = 0
        elif trace_color[1] >=1 and trace_color[2] >=0:
            r_iter = 0
            g_iter = 0
            b_iter = -iter_val
        elif trace_color[1] >=1 and trace_color[0] < 1:
            r_iter = iter_val
            g_iter = 0
            b_iter = 0
        elif trace_color[1] >=0 and trace_color[0] >= 1:
            r_iter = 0
            g_iter = -iter_val
            b_iter = 0
        rgb_iter = (r_iter,g_iter,b_iter)
        trace_color = tuple(map(lambda i, j: i + j, trace_color, rgb_iter))
    print(f'New trace color: {trace_color}')


# sphere.CreateDisplayOpacityAttr([float(0.1)])
# print(sphere.GetDisplayOpacityAttr())
        
####################################################################################################
##### Main Code #####

world.reset()
while True:
    appwindow = omni.appwindow.get_default_app_window()
    input = carb.input.acquire_input_interface()
    input.subscribe_to_keyboard_events(appwindow.get_keyboard(), keyboard_event)
    if start:
        object=dc.get_rigid_body(quad_path)
        object_pose=dc.get_rigid_body_pose(object)
        global_pose,global_orient = prim.get_world_pose()

        xpose = global_pose[0]
        ypose = global_pose[1]
        zpose = global_pose[2]
        
        # print("position:", object_pose.p)
        # print("rotation:", object_pose.r)
        d_curr = [0,0,0]
        v_curr = [0,0,0]

        if rigid_body_api and dind < len(dx):
            d_curr = [dx[dind],dy[dind],dz[dind]]
            delx = dx[dind]-global_pose[0]
            dely = dy[dind]-global_pose[1]
            delz = dz[dind]-global_pose[2]
            
            dist = np.sqrt((xpose-xpose_prev)**2 + (ypose-ypose_prev)**2 + (zpose-zpose_prev)**2)
            # print(dist)
            if trace_iter == 0:
                trace_iter += 1
            elif dist >= 0.3:
                sphere = UsdGeom.Sphere.Define(stage, f'/World/trace/sphere{trace_iter}')
                sphere.CreateRadiusAttr(trace_width)
                sphere_x = float(global_pose[0])
                sphere_y = float(global_pose[1])
                sphere_z = float(global_pose[2])
                sphere.AddTranslateOp().Set(Gf.Vec3f(sphere_x,sphere_y,sphere_z))
                sphere.AddScaleOp().Set(Gf.Vec3f(1.0))
                sphere.GetDisplayColorAttr().Set([trace_color])

                # primvarsapi = UsdGeom.PrimvarsAPI(sphere)
                # sphere_shadow = primvarsapi.CreatePrimvar('doNotCastShadows', Sdf.ValueTypeNames.Bool)
                # # sphere_shadow = sphere.CreateAttribute('primvars:doNotCastShadows', bool)
                # # sphere_shadow.Set(False)
                # sphere_shadow.Set(False)

                trace.append(sphere)
                
                # print(sphere.GetSchemaAttributeNames())
                trace_iter += 1


            kp_mod = kp

            if delz > 0.5:
                kp_mod = 0.25*kp
            elif delz < -0.5 and (np.abs(delx) < 0.5 and np.abs(dely) < 0.5):
                kp_mod = 0.25*kp
            vx = kp_mod*delx + kd*(delx - delx_prev)
            vy = kp_mod*dely + kd*(dely - dely_prev)
            vz = kp_z*(delz) + kd_z*(delz - delz_prev)
            v_curr = [vx,vy,vz]
            if np.abs(delx) <= 0.5 and np.abs(dely) <= 0.5 and np.abs(delz) <= 0.05:
                # vx = 0
                # vy = 0
                # vz = 0
                dind +=1
                iterate_color(False,len(dz))
            vel = Gf.Vec3f(vx,vy,vz)
            rigid_body_api.GetVelocityAttr().Set(vel)
            # rigid_body_api.GetAngularVelocityAttr().Set(vel)
            
            xpose_prev = xpose
            ypose_prev = xpose
            zpose_prev = xpose

            delx_prev = delx
            dely_prev = dely
            delz_prev = delz
            print(f'Trace Color: {trace_color}')
            print_state(global_pose,d_curr,dind,v_curr,goal_reached)
            if dind > len(dz):
                start = not start
        else:

            vel = Gf.Vec3f(0,0,0)
            rigid_body_api.GetVelocityAttr().Set(vel)

        
    else:
        vel = Gf.Vec3f(0,0,0)
        rigid_body_api.GetVelocityAttr().Set(vel)
        
    world.step(render=True)

simulation_app.close()
