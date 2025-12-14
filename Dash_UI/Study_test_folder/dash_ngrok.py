#package fix





import dash

from dash import dcc, html, Input, Output, State, callback_context, no_update

from dash.dependencies import ALL

import plotly.graph_objects as go

import json

import os

import glob

from datetime import datetime

import hashlib

import csv

from dash.exceptions import PreventUpdate

import time 

from filelock import FileLock 



# Assuming backend_operations.py exists in the same directory

try:

    from backend_operations import dynamic_deviation_threshold_multi_logic

except ImportError:

    # print("FATAL ERROR: backend_operations.py not found.")

    # print("Please make sure this file is in the same directory as the app.")

    def dynamic_deviation_threshold_multi_logic(**kwargs):

        # print("Warning: Using dummy backend function.")

        hmm_array = kwargs.get('hmm_array', {})

        rmm_array = kwargs.get('rmm_array', {}) 

        sync_occurred = rmm_array.get('Replan_flag', False)

        return rmm_array if sync_occurred else hmm_array, sync_occurred



# --- Constants ---

GRID_WIDTH = 20

GRID_HEIGHT = 20

UPDATE_INTERVAL_MS = 1000

SLOW_INTERVAL_MS = 2000

CLICK_POLL_INTERVAL_MS = 1000

# --- Constants ---
# ... other constants ...
TRAINING_VIDEO_URL = "https://www.youtube.com/embed/d2aJuvjMlrs?si=M6_NDLwbvvqruKd8"

# "https://www.youtube.com/embed/dQw4w9WgXcQ?si=DyjrA0IeEKRrsVx1"
# <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=DyjrA0IeEKRrsVx1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>




# <iframe width="560" height="315" src="https://www.youtube.com/embed/d2aJuvjMlrs?si=M6_NDLwbvvqruKd8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


# https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1

PARTICIPANT_COUNT_FILE = 'study_data/participant_count.txt'

PARTICIPANT_COUNT_LOCK = 'study_data/participant_count.lock'



THRESHOLD_VALUES = {

    'with_framework': {1: 5, 2: 12, 3: 15, 4: 9, 5: 10, 6: 11},

    'without_framework': {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1} 

}



WITHOUT_FRAMEWORK_INTERVALS = {

    1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8

}



SCENARIO_CONFIG = {

    1: {'total_time': 335.0, 'total_steps': 245},

    2: {'total_time': 300.0, 'total_steps': 361},

    3: {'total_time': 360.0, 'total_steps': 417},

    4: {'total_time': 350.0, 'total_steps': 372},

    5: {'total_time': 370.0, 'total_steps': 400},

    6: {'total_time': 400.0, 'total_steps': 441}

}



PAUSE_POINTS = {

    1: [117, 159, 237],

    2: [43, 95, 317],

    3: [176, 183, 391],

    4: [20, 101, 329],

    5: [120, 143, 374],

    6: [140, 175, 322]

}



# --- 24-COMBINATION STUDY DESIGN ---

STUDY_DESIGN_TABLE = [

    [(1, 1), (2, 0), (3, 3), (4, 2)], [(1, 0), (2, 3), (3, 2), (4, 1)], 

    [(1, 3), (2, 2), (3, 1), (4, 0)], [(1, 2), (2, 1), (3, 0), (4, 3)],

    [(1, 1), (2, 0), (5, 3), (6, 2)], [(1, 0), (2, 3), (5, 2), (6, 1)], 

    [(1, 3), (2, 2), (5, 1), (6, 0)], [(1, 2), (2, 1), (5, 0), (6, 3)],

    [(3, 1), (4, 0), (1, 3), (2, 2)], [(3, 0), (4, 3), (1, 2), (2, 1)], 

    [(3, 3), (4, 2), (1, 1), (2, 0)], [(3, 2), (4, 1), (1, 0), (2, 3)],

    [(3, 1), (4, 0), (5, 3), (6, 2)], [(3, 0), (4, 3), (5, 2), (6, 1)], 

    [(3, 3), (4, 2), (5, 1), (6, 0)], [(3, 2), (4, 1), (5, 0), (6, 3)],

    [(5, 1), (6, 0), (1, 3), (2, 2)], [(5, 0), (6, 3), (1, 2), (2, 1)], 

    [(5, 3), (6, 2), (1, 1), (2, 0)], [(5, 2), (6, 1), (1, 0), (2, 3)],

    [(5, 1), (6, 0), (3, 3), (4, 2)], [(5, 0), (6, 3), (3, 2), (4, 1)], 

    [(5, 3), (6, 2), (3, 1), (4, 0)], [(5, 2), (6, 1), (3, 0), (4, 3)]

]



SCENARIO_CONTENT = {

    1: {

        "briefing": "In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points.\n\nRobot 1 is responsible for the southwest (SW) region and SW drop-off zone.\nRobot 2 is responsible for the northwest (NW) region and NW drop-off zone.\nRobot 3 acts as a support and exploration unit, assisting with package drop-offs in either region or searching for the unassigned quadrants to locate any remaining packages.\n\nRobots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey; these packages will appear on the interface as yellow triangles as they are found. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed. \n The package counter displays progress as 'X/4 + Y', where the first portion tracks the four originally known packages and the '+ Y' counts any additional discovered packages that have been delivered.",

        "questions": [

            {"text": "Has more than one package been discovered?", "options": ["Yes", "No"]},

            {"text": "Which quadrant has most packages been discovered?", "options": ["SE", "SW", "NE", "NW"]},

            {"text": "Which drop-off zone zone will robot 3 deliver its package to?", "options": ["Robot 3 will leave the SW quadrant and deliver its package in the NW", "Robot 3 will remain in the SW quadrant and deliver its package in the SW", "Robot 3 will remain in the NW quadrant and deliver its package in the NW", "Robot 3 will leave the NW quadrant and deliver its package in the SE"]}

        ]

    },

    2: {

        "briefing": "In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points.\n\nRobot 1 is responsible for the southwest (SW) region and SW drop-off zone.\nRobot 2 is responsible for the northwest (NW) region and NW drop-off zone.\nRobot 3 acts as a support and exploration unit, assisting with package drop-offs in either region or searching for the unassigned quadrants to locate any remaining packages.\n\nRobots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square.         Robots will also discover packages along their journey; these packages will appear on the interface as yellow triangles as they are found. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed. \n The package counter displays progress as 'X/4 + Y', where the first portion tracks the four originally known packages and the '+ Y' counts any additional discovered packages that have been delivered. ",

        "questions": [

            {"text": "Which robot(s) are currently navigating around an obstacle?", "options": ["Robot 1", "Robot 2", "Robot 3", "None"]},                                              

            {"text": "What obstacle is Robot 3 facing?", "options": ["Robot 3 is communicating to a different robot", "Robot 3 is stuck in rough terrain", "Robot 3 is recharging", "Robot 3 is encountering bad weather"]},

            {"text": "Which robot do you expect will finish its task last?", "options": ["Robot 1", "Robot 2", "Robot 3"]}

        ]

    },

    3: {

        "briefing": "In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points.\n\nRobot 1 is responsible for the northwest (NW) region and NW drop-off zone.\nRobot 2 is responsible for the southeast (SE) region and SE drop-off zone.\nRobot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages.\n\nRobots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square.         Robots will also discover packages along their journey; these packages will appear on the interface as yellow triangles as they are found. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed. \n The package counter displays progress as 'X/4 + Y', where the first portion tracks the four originally known packages and the '+ Y' counts any additional discovered packages that have been delivered.",

        "questions": [

            {"text": "What is the status of Robot 2?", "options": ["Replanning due to bad weather", "Replanning due to rough terrain", "Recharging", "On track"]},

            {"text": "What are the implications of robot 2 being stuck in rough terrain?", "options": ["Robot 2 will have to send its assignment to a different robot", "Robot 2’s delivery will not be impacted", "Robot 2 will desert its mission entirely", "Robot 2 will have to replan its route"]},

            {"text": "Which robot is likely to deliver a package next?", "options": ["Robot 1", "Robot 2", "Robot 3", "Robot 2 and 3 simultaneously"]}

        ]

    },

    4: {

        "briefing": "In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points.\n\nRobot 1 is responsible for the northwest (NW) region and NW drop-off zone.\nRobot 2 is responsible for the southeast (SE) region and SE drop-off zone.\nRobot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages.\n\nRobots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.",

        "questions": [

            {"text": "Which quadrant is Robot 3 in?", "options": ["SE", "NE", "NW", "SW"]},

            {"text": "Why is Robot 3 in the NW quadrant?", "options": ["Robot 3 discovered a package in the NE and is delivering it to the NW", "Robot 3 discovered a package in the NW and is delivering it", "Robot 1 requested Robot 3 to pick-up and deliver a package in the NW", "Robot 2 requested Robot 3 to pick-up and deliver a package in the NW"]},

            {"text": "Which drop-off zone will robot 3 end its mission?", "options": ["SE", "SW", "NE", "NW"]}

        ]

    },

    5: {

        "briefing": "In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points.\n\nRobot 1 is responsible for the northeast (NE) region and NE drop-off zone.\nRobot 2 is responsible for the southwest (SW) region and drop-off zone.\nRobot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages.\n\nRobots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.",

        "questions": [

            {"text": "What is the status of robot 2?", "options": ["Just picked up a package", "Just delivered a package", "Robot 2 is recharging", "Robot 2 is replanning"]},

            {"text": "Given that robot 2 just delivered a package, what comes next?", "options": ["Robot 2 will head towards a different package in the NW quadrant", "Robot 2 will assist Robot 1 in the NW quadrant", "Robot 2 will head towards a different package in the SW quadrant", "Robot 2 will assist Robot 3 in the NE quadrant", "Robot 2 will search the NE and SE quadrants for remaining packages"]},

            {"text": "Which robot is likely to finish its mission next?", "options": ["Robot 1", "Robot 2.", "Robot 3.", "Robot 1 and 2 simultaneously.", "Robot 3 and 2 simultaneously."]}

        ]

    },

    6: {

        "briefing": "In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points.\n\nRobot 1 is responsible for the northeast (NE) region and NE drop-off zone.\nRobot 2 is responsible for the southwest (SW) region and drop-off zone.\nRobot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages.\n\nRobots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.",

        "questions": [

            {"text": "Which robot(s) are currently navigating around an obstacle?", "options": ["Robot 1", "Robot 2", "Robot 3", "No robots are encountering an obstacle"]},

            {"text": "What type of obstacle(s) are robot 2 and robot 3 experiencing?", "options": ["Both robots are experiencing poor weather", "Both robots are experiencing rough terrain", "Robot 3 is experiencing poor weather, Robot 2 is experiencing rough terrain", "Robot 2 is experiencing poor weather, Robot 3 is experiencing rough terrain"]},

            {"text": "What is robot 3 going to do now that it has cleared the NW quadrant?", "options": ["Robot 3 will end its mission", "Robot 3 will assist Robot 1 in the SE", "Robot 3 will assist Robot 2 in the NE", "Robot 3 will return to the SE"]}

        ]

    }

}



def get_condition_names(condition_idx):

    view_type = 'map' if condition_idx < 2 else 'text'

    framework_mode = 'with_framework' if condition_idx % 2 == 0 else 'without_framework'

    return view_type, framework_mode



def create_message_log_entry(message_id, robot_id, scenario_num, condition_idx, 

                             frame_idx, sim_time, message_type, message_text,

                             participant_id, appear_time, robot_state, robot_x, robot_y):

    return {

        'message_id': message_id,

        'participant_id': participant_id,

        'scenario': scenario_num,

        'condition': condition_idx,

        'run_number': None, 

        'frame': frame_idx,

        'sim_time': sim_time,

        'robot_id': robot_id,

        'robot_state': robot_state,

        'robot_x': robot_x,

        'robot_y': robot_y,

        'message_type': message_type,

        'message_text': message_text,

        'appear_timestamp_iso': datetime.fromtimestamp(appear_time).isoformat(),

        'appear_timestamp_unix': appear_time,

        'clicked': 0,

        'click_timestamp_iso': None,

        'click_timestamp_unix': None,

        'time_to_click_seconds': None,

    }



def save_message_logs(participant_data, all_message_logs, study_state):

    os.makedirs('study_data', exist_ok=True)

    participant_id = participant_data['id']

    csv_file = f'study_data/{participant_id}_message_logs.csv'

    current_run_idx = study_state.get('current_run_idx', 0)

    for log in all_message_logs:

        if log.get('run_number') is None:

            log['run_number'] = current_run_idx + 1

    

    if all_message_logs:

        with open(csv_file, 'w', newline='', encoding='utf-8') as f:

            fieldnames = [

                'message_id', 'participant_id', 'scenario', 'condition', 'run_number',

                'frame', 'sim_time', 'robot_id', 'robot_state', 'robot_x', 'robot_y',

                'message_type', 'message_text', 'appear_timestamp_iso',

                'clicked', 'click_timestamp_iso', 'time_to_click_seconds', 

            ]

            existing_fieldnames = [fn for fn in fieldnames if fn in all_message_logs[0]]

            writer = csv.DictWriter(f, fieldnames=existing_fieldnames, extrasaction='ignore')

            writer.writeheader()

            writer.writerows(all_message_logs)

        print(f"Saved {len(all_message_logs)} message log entries for {participant_id}")



try:

    with open('all_scenarios_hmm_data.json', 'r') as f:

        ALL_SCENARIOS_HMM_DATA = json.load(f)

except FileNotFoundError:

    ALL_SCENARIOS_HMM_DATA = {}



def get_hmms_for_active_scenario(scenario_number):

    scenario_key = f'scenario_{scenario_number}'

    scenario_data = ALL_SCENARIOS_HMM_DATA.get(scenario_key, {})

    return scenario_data.get('HMM_Robot_1'), scenario_data.get('HMM_Robot_2'), scenario_data.get('HMM_Robot_3')



def load_static_data(filepath):

    try:

        with open(filepath, 'r') as f:

            return json.load(f)

    except FileNotFoundError:

        return {"walls": [], "zones": [], "nodes": [], "edges": []}



# --- ADD THIS NEAR TOP OF FILE ---
SCENARIO_CACHE = {}

# --- UPDATE THIS FUNCTION ---
def load_scenario_frames(scenario_id):
    # Check if this worker already has the data
    if scenario_id in SCENARIO_CACHE:
        return SCENARIO_CACHE[scenario_id]

    folder = f"scenarios_with_graphs/scenario_{scenario_id}/"
    frames = []
    if not os.path.isdir(folder):
        print(f"Error: Scenario folder not found at {folder}")
        return frames

    frame_files = sorted(glob.glob(os.path.join(folder, "frame_*.json")),
                        key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))
    for frame_file in frame_files:
        try:
            with open(frame_file, "r") as f:
                frames.append(json.load(f))
        except Exception as e:
            print(f"Error loading {frame_file}: {e}")
    
    # Save to memory so we don't read disk again
    SCENARIO_CACHE[scenario_id] = frames
    return frames


def generate_participant_id(name):

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    name_hash = hashlib.md5(name.encode()).hexdigest()[:6]

    return f"P{timestamp}_{name_hash}"



def save_study_data(participant_data, responses, interactions):

    os.makedirs('study_data', exist_ok=True)

    participant_id = participant_data['id']

    with open(f'study_data/{participant_id}_responses.json', 'w') as f:

        json.dump(responses, f, indent=2)

    with open(f'study_data/{participant_id}_interactions.json', 'w') as f:

        json.dump(interactions if interactions is not None else [], f, indent=2)

    

    csv_file = 'study_data/master_post_scenario_responses.csv'

    file_exists = os.path.isfile(csv_file)

    post_scenario_responses = [r for r in responses if r.get('type') == 'post_scenario']

    if not post_scenario_responses:

        return



    with open(csv_file, 'a', newline='', encoding='utf-8') as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([

                'ParticipantID', 'Name', 'ParticipantStartTime',

                'RunNumber', 'Scenario', 'ConditionIndex', 

                'ViewType', 'Framework', 'ResponseTimestamp',

                'MentalDemand', 'PhysicalDemand', 'TemporalDemand', 'Performance',

                'Effort', 'Frustration'

            ])

        resp = post_scenario_responses[-1]

        q_answers = resp.get('answers', {})

        writer.writerow([

            participant_id, participant_data['name'], participant_data['start_time'],

            resp.get('run_number'), resp.get('scenario'), resp.get('condition'),

            resp.get('view_type'), resp.get('framework'), resp.get('timestamp'),

            q_answers.get('mental_demand'), q_answers.get('physical_demand'),

            q_answers.get('temporal_demand'), q_answers.get('performance'),

            q_answers.get('effort'), q_answers.get('frustration'),

        ])



# --- FIGURE CREATION ---

def create_figure_for_frame(static_data, frame_data):

    fig = go.Figure()

    fig.update_layout(

        xaxis=dict(range=[0, GRID_WIDTH], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False, dtick=10),

        yaxis=dict(range=[0, GRID_HEIGHT], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False),

        plot_bgcolor='#ffffff', paper_bgcolor='#ffffff', font=dict(color='black'),

        showlegend=True,

        legend=dict(

            title='Legend', orientation='v', yanchor='top', y=1, xanchor='left', x=1.02,

            bgcolor='rgba(255,255,255,0.7)', bordercolor='Black', borderwidth=1

        ),

        margin=dict(l=0, r=0, t=0, b=0), uirevision='constant',

        annotations=[

            go.layout.Annotation(x=2.5, y=17.5, text="NW", showarrow=False, font=dict(size=24, color="rgba(0, 0, 0, 0.20)")),

            go.layout.Annotation(x=17.5, y=17.5, text="NE", showarrow=False, font=dict(size=24, color="rgba(0, 0, 0, 0.20)")),

            go.layout.Annotation(x=2.5, y=2.5, text="SW", showarrow=False, font=dict(size=24, color="rgba(0, 0, 0, 0.20)")),

            go.layout.Annotation(x=17.5, y=2.5, text="SE", showarrow=False, font=dict(size=24, color="rgba(0, 0, 0, 0.20)"))

        ]

    )

    

    # --- LEGEND ENTRIES (DUMMY TRACES) ---

    fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(color='rgb(173, 216, 230)', size=10, symbol='square'), name='Bad Weather Zone'))

    fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(color='rgb(128, 128, 128)', size=10, symbol='square'), name='Rough Terrain Zone'))

    # UPDATED: Containment Zone -> Pink

    fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(color='rgb(255, 192, 203)', size=10, symbol='square'), name='Charging Station/ Drop Off Zone'))

    # fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(color='rgb(255, 255, 0)', size=10, symbol='circle'), name='Charging Station/ Drop Off Zone'))

    # NEW: Red Line

    fig.add_trace(go.Scatter(x=[None], y=[None], mode='lines', line=dict(color='red', width=2), name='Unknown Barriers'))

    # NEW: Blue Circle

    fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(color='blue', size=12, symbol='circle'), name='Robot Waiting'))





    walls_data = frame_data.get('walls', []) if frame_data else static_data.get('walls', [])

    zones_data = frame_data.get('zones', []) if frame_data else static_data.get('zones', [])

    nodes_data = frame_data.get('nodes', []) if frame_data else static_data.get('nodes', [])

    edges_data = frame_data.get('edges', []) if frame_data else static_data.get('edges', [])



    for wall in walls_data:

        wall_coords = sorted(wall.items())

        wall_x = [v for k, v in wall_coords if k.startswith('x')]

        wall_y = [v for k, v in wall_coords if k.startswith('y')]

        fig.add_trace(go.Scatter(x=wall_x, y=wall_y, mode='lines', line=dict(color='black', width=2), hoverinfo='none', showlegend=False))



    for zone in zones_data:

        color_str = zone.get('color', 'rgba(0,0,0,0)')

        if color_str.startswith('('):

            color_str = f"rgb{color_str}"

        zone_coords = sorted(zone.items())

        zone_x = [v for k, v in zone_coords if k.startswith('x')]

        zone_y = [v for k, v in zone_coords if k.startswith('y')]

        fig.add_trace(go.Scatter(x=zone_x, y=zone_y, fill="toself", fillcolor=color_str, line=dict(width=0), mode='lines', hoverinfo='none', showlegend=False))



    edge_x, edge_y = [], []

    for edge in edges_data:

        edge_x.extend([edge['x0'], edge['x1'], None])

        edge_y.extend([edge['y0'], edge['y1'], None])



    if nodes_data:

        node_x = [node[0] for node in nodes_data]

        node_y = [node[1] for node in nodes_data]

        fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers', marker=dict(size=4, color='rgba(50, 50, 150, 0.8)'), hoverinfo='none', showlegend=False))



    if frame_data:

        robots = [{'id': rid, **rdata} for rid, rdata in frame_data.get('robots', {}).items()]

        packages = frame_data.get('packages', [])



        if robots:

            traces = {'x': [], 'y': [], 'colors': [], 'texts': [], 'hovers': []}

            for r in robots:

                traces['x'].append(r['x'])

                traces['y'].append(r['y'])

                traces['texts'].append(r['id'][-1])

                traces['hovers'].append(f"{r['id']} State: {r['state']} Pos: ({r['x']:.1f}, {r['y']:.1f})")

                r_state = r['state']

                color_map = {'moving': 'red', 'carrying': 'orange', 'waiting': 'blue', 'all_tasks_complete': 'green'}

                traces['colors'].append(color_map.get(r_state, 'grey'))



            fig.add_trace(go.Scatter(x=traces['x'], y=traces['y'], mode='markers+text', name='Robot',

                                     marker=dict(size=40, color=traces['colors'], line=dict(width=2, color='white')),

                                     text=traces['texts'], textposition='middle center',

                                     textfont=dict(color='white', size=12, family="Arial Black"),

                                     hovertext=traces['hovers'], hoverinfo='text'))



        if packages:

            known_pkg_x, known_pkg_y, known_pkg_texts, known_pkg_hovers = [], [], [], []

            discovered_d_pkg_x, discovered_d_pkg_y, discovered_d_pkg_texts, discovered_d_pkg_hovers = [], [], [], []

            undiscovered_d_pkg_x, undiscovered_d_pkg_y, undiscovered_d_pkg_texts, undiscovered_d_pkg_hovers = [], [], [], []



            robot_pos = {r['id']: (r['x'], r['y']) for r in robots}

            plotted_coords = set()



            for p in packages:

                carried_by_robot = p.get('carried_by')

                is_carried = carried_by_robot is not None and carried_by_robot != "Null"

                is_d_package = p['id'].startswith('d')



                if is_d_package:

                    is_discovered = p.get('Discovered', 0) == 1

                    # --- NEW LOGIC: Undiscovered packages are invisible ---

                    if not is_discovered:

                        continue # Skip adding to lists

                else:

                    is_discovered = True



                if is_carried:

                    px, py = robot_pos.get(carried_by_robot, (p.get('x', 0), p.get('y', 0)))

                else:

                    px, py = p.get('x', 0), p.get('y', 0)



                coord_key = (round(px, 2), round(py, 2), is_carried)

                if coord_key in plotted_coords:

                    continue

                plotted_coords.add(coord_key)

                

                pkg_text = p['id'][-1]



                if is_carried:

                    known_pkg_x.append(px); known_pkg_y.append(py); known_pkg_texts.append(pkg_text); known_pkg_hovers.append(f"Package {p['id']}, Carried by {carried_by_robot}")

                elif is_d_package:

                    if is_discovered:

                        discovered_d_pkg_x.append(px); discovered_d_pkg_y.append(py); discovered_d_pkg_texts.append(pkg_text); discovered_d_pkg_hovers.append(f"Package {p['id']}, On Ground (Discovered)")

                else: 

                    known_pkg_x.append(px); known_pkg_y.append(py); known_pkg_texts.append(pkg_text); known_pkg_hovers.append(f"Package {p['id']}, On Ground (Pre-known)")



            if known_pkg_x:

                fig.add_trace(go.Scatter(x=known_pkg_x, y=known_pkg_y, name='Package (Known/Carried)', mode='markers+text',

                    marker=dict(size=20, color='gold', symbol='square', line=dict(width=1, color='black')),

                    text=known_pkg_texts, textposition='middle center', textfont=dict(color='black', size=10, family="Arial Black"), hovertext=known_pkg_hovers, hoverinfo='text'))



            if discovered_d_pkg_x:

                fig.add_trace(go.Scatter(x=discovered_d_pkg_x, y=discovered_d_pkg_y, name="Package (Discovered 'd')", mode='markers+text',

                    marker=dict(size=20, color='gold', symbol='triangle-up', line=dict(width=1, color='black')),

                    text=discovered_d_pkg_texts, textposition='middle center', textfont=dict(color='black', size=10, family="Arial Black"), hovertext=discovered_d_pkg_hovers, hoverinfo='text'))

            

            # NOTE: Green triangles (undiscovered) trace is effectively removed/empty now



    return fig
def create_rich_status_message_data(robot_data, sim_time, all_packages, selected_robot_hmm_array, selected_robot_rmm_array, scenario_id, framework_mode):
    # --- 1. Setup & ETA Calculation ---
    time_str = datetime.now().strftime('%I:%M:%S %p')
    robot_id = robot_data.get('id', 'N/A')
    robot_title = robot_id.replace("robot", "Robot ").title()
    
    x, y = float(robot_data.get('x', 0)), float(robot_data.get('y', 0))
    state = robot_data.get('state')
    quadrant = robot_data.get('Quadrant', 'N/A')
    message_id = f"{robot_id}-{sim_time:.2f}"

    plan_index = selected_robot_rmm_array.get('plan_index', 0)
    scenario_config = SCENARIO_CONFIG.get(scenario_id, {'total_time': 300.0, 'total_steps': 100})
    total_steps = scenario_config['total_steps']
    time_per_step = scenario_config['total_time'] / total_steps if total_steps > 0 else 0
    plan_list = selected_robot_rmm_array.get('plan', [])
    remaining_steps = len(plan_list) - plan_index
    eta_seconds = abs(int(remaining_steps * time_per_step))
    
    
    # --- 2. Startup Filter: Skip 0s noise ---
    # FIX: Only apply the strict ETA filter if we are using the intelligent framework.
    # If without_framework, we want the "stupid" messages even if ETA is 0.
    if framework_mode == 'with_framework':
        if (eta_seconds == 0 and state != 'all_tasks_complete') or (sim_time < 2.0):
            return None, None, None
    else:
        # For without_framework, only filter the very first second to avoid startup glitches
        if sim_time < 2.0:
            return None, None, None
        
        
        
    
    # # --- 2. Startup Filter: Skip 0s noise ---
    # if (eta_seconds == 0 and state != 'all_tasks_complete') or (sim_time < 2.0):
    #     return None, None, None




    # --- 3. Detect Features & Build Context ---
    feature_alerts = []
    summary_icons = []
    critical_feature_active = False 

    # Weather
    hmm_weather = int(selected_robot_hmm_array.get('Current_weather', 1)) if selected_robot_hmm_array else 1
    rmm_weather = int(selected_robot_rmm_array.get('Current_weather', 1))
    if rmm_weather == 0:
        summary_icons.append("⛈️")
        critical_feature_active = True
    if hmm_weather != rmm_weather:
        if rmm_weather == 0: feature_alerts.append("Encountering heavy storm.")
        else: feature_alerts.append("Weather has cleared.")

    # Terrain
    hmm_terrain = int(selected_robot_hmm_array.get('Bad_Terrain', 1)) if selected_robot_hmm_array else 1
    rmm_terrain = int(selected_robot_rmm_array.get('Bad_Terrain', 1))
    if rmm_terrain == 0:
        summary_icons.append("⛰️")
        critical_feature_active = True
    if hmm_terrain != rmm_terrain:
        if rmm_terrain == 0 and hmm_terrain == 1: feature_alerts.append("Navigating rough terrain.")
        elif rmm_terrain == 1 and hmm_terrain == 0: feature_alerts.append("Terrain cleared.") 

    # Battery
    hmm_battery = int(selected_robot_hmm_array.get('Battery_status', 1)) if selected_robot_hmm_array else 1
    rmm_battery = int(selected_robot_rmm_array.get('Battery_status', 1))
    if hmm_battery != rmm_battery:
        if rmm_battery == 0: 
            feature_alerts.append("Battery Critical.")
            summary_icons.append("🪫")
            critical_feature_active = True
        elif rmm_battery == 1: 
            feature_alerts.append("Battery optimal.")

    # Offline
    hmm_offline = int(selected_robot_hmm_array.get('Momentarily_offline', 0)) if selected_robot_hmm_array else 0
    rmm_offline = int(selected_robot_rmm_array.get('Momentarily_offline', 0))
    if hmm_offline != rmm_offline:
        if rmm_offline == 1:
            feature_alerts.append("Connection Lost.")
            summary_icons.append("🚫")
            critical_feature_active = True
        else:
             feature_alerts.append("Connection Restored.")

    # --- 4. Determine Status Type & Header ---
    replan = robot_data.get('replan_flag') == True
    core_state = 'on_track' # Default
    
    if state == 'all_tasks_complete':
        status_text = "MISSION COMPLETE"
        status_icon = "🎉"
        style_class = "on-track"
        core_state = 'complete'
    elif replan:
        status_text = "RECALCULATING"
        status_icon = "🔄"
        style_class = "replan"
        core_state = 'replan'
    elif critical_feature_active:
        status_text = "ENVIRONMENT ALERT"
        status_icon = "⚠️"
        style_class = "stationary" 
        core_state = 'feature'
    elif framework_mode == 'with_framework':
        status_text = "TIMING UPDATE" 
        status_icon = "⏱️"
        style_class = "stationary"
        core_state = 'deviation'
    else:
        status_text = "STATUS REPORT"
        status_icon = "📋"
        style_class = "on-track"
        core_state = 'on_track'

    # Build Header String
    if summary_icons:
        status_text = f"{' '.join(summary_icons)} {status_text}"
    
    # --- UPDATED PACKAGE COUNT LOGIC (n/4 + m) ---
    # n = Completed Expected Packages (Initial set)
    # m = Completed Bonus/Discovered Packages (Start with 'd')
    
    total_completed = robot_data.get('total_completed_packages', 0)
    n_expected = 0
    m_bonus = 0
    count_success = False

    # Iterate through all packages to categorize the completed ones
    if all_packages:
        for p in all_packages:
            # Check if this package is delivered by the current robot
            is_my_delivery = False
            # Check 'delivered_by' key first
            if p.get('delivered_by') == robot_id:
                is_my_delivery = True
            # Fallback: Check state + Assigned_to
            elif (p.get('state') == 'delivered' or p.get('status') == 'delivered') and p.get('Assigned_to') == robot_id:
                is_my_delivery = True
                
            if is_my_delivery:
                count_success = True
                # 'd' packages are dynamic/bonus, others (p1..p4) are expected
                if p.get('id', '').startswith('d'):
                    m_bonus += 1
                else:
                    n_expected += 1

    # Fallback: If we couldn't count individually (e.g. data missing), estimate based on total
    if not count_success and total_completed > 0:
        n_expected = min(total_completed, 4)
        m_bonus = max(0, total_completed - 4)

    # Format the display string: "Pkgs: n/4" or "Pkgs: n/4 +m"
    pkg_status_str = f"Pkgs: {n_expected}/4"
    if m_bonus > 0:
        pkg_status_str += f" +{m_bonus}"

    # Append to status text
    status_text += f"  {pkg_status_str}"

    # --- 5. Build Details Body ---
    details_msg = [f"Estimated Time to Goal: {eta_seconds} seconds."]
    
    if feature_alerts:
        details_msg.append(html.Strong(" ".join(feature_alerts)))
    
    # Add Package Context
    pkg_info = ""
    if state == 'carrying':
        # Find which package is being carried
        pkg_id = next((p['id'] for p in all_packages if p.get('carried_by') == robot_id), None)
        if pkg_id: pkg_info = f"Transporting {pkg_id}."
    elif state == 'moving':
        target_pkg = robot_data.get('target_package_id', "target")
        pkg_info = f"En route to {target_pkg}."
        
    if replan:
        details_msg.append(f"Path blocked or invalid. {pkg_info} Rerouting in {quadrant} quadrant.")
    elif state == 'waiting':
        details_msg.append(f"Holding position in {quadrant} quadrant.")
    elif state == 'all_tasks_complete':
        details_msg.append("All assigned tasks finished. Returning to base.")
    else:
        details_msg.append(f"{pkg_info} Current location: {quadrant} quadrant.")

    return {
        'message_id': message_id,
        'robot_id_title': robot_title,
        'status_icon': status_icon,
        'status_text': status_text, 
        'status_class_suffix': style_class,
        'time_str': time_str,
        'details_msg': details_msg,
        'core_state': core_state,   
        'feature_set': summary_icons,
        'pkg_count': total_completed # We keep total here for the logic check in update_simulation_views
    }, style_class, " ".join([str(item) for item in details_msg])
    
    
    
    


def render_message_component(message_data, open_message_ids, is_new=False):

    message_id = message_data['message_id']

    component_class = f"message-container-details {message_data['status_class_suffix']}"

    if is_new:

        component_class += " new-message"

        

    summary = html.Summary(

        html.Div([

            html.Span(message_data['status_icon'], style={'marginRight': '10px', 'fontSize': '1.5em'}),

            html.Strong(f"{message_data['robot_id_title']}: {message_data['status_text']}")

        ], style={'display': 'flex', 'alignItems': 'center', 'fontSize': '1.2em', 'fontWeight': 'bold'})

    )



    details_content = html.Div([

        html.P(message_data['time_str'], style={'fontSize': '0.9em', 'color': '#555', 'margin': '10px 0 5px 0'}),

        html.P(message_data['details_msg'], style={'fontSize': '1.1em', 'margin': '5px 0 0 0'})

    ], style={'paddingLeft': '45px', 'paddingTop': '10px'})



    return html.Details([summary, details_content],

                       className=component_class,

                       id={'type': 'status-message', 'id': message_id},

                       open=(message_id in open_message_ids),

                       )



# --- App Initialization ---

app = dash.Dash(__name__, update_title=None, suppress_callback_exceptions=True)

server = app.server



static_map_data = load_static_data('static_map_data.json')

initial_figure = create_figure_for_frame(static_map_data, None)



def consent_screen():

    consent_text = """

You are invited to take part in a research study led by the Cognitive Engineering Center at the Georgia Institute of Technology. The goal of this study is to evaluate a prototype interface that helps a human operator monitor and understand the behavior of a swarm of autonomous robots through system-generated updates. Your session will last about 45–60 minutes. You will watch several short video demonstrations and answer questions about your understanding and overall experience. You will receive \$20 for completing the session.



The risks are minimal and similar to those encountered in everyday activities. There are no direct benefits to you, but your participation will help improve human–robot communication systems.



Your responses will be kept confidential. Any information shared publicly will not include identifying details. De-identified data may be used for future research.



Taking part in this study is completely voluntary. You may stop participating at any time without penalty. However, to receive the full \$20 compensation, you must complete the entire session.



If you have questions about your rights as a participant, contact the Georgia Tech Office of Research Integrity Assurance at IRB@gatech.edu.

"""

    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

                          'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',

                          'justifyContent': 'center', 'fontFamily': 'Arial', 'padding': '20px'}, children=[

        html.H1("Consent Acknowledgment", style={'color': '#00ff88', 'marginBottom': '30px'}),

        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

                       'maxWidth': '800px', 'width': '100%', 'maxHeight': '70vh', 'overflowY': 'auto'}, children=[

            dcc.Markdown(consent_text, style={'whiteSpace': 'pre-wrap', 'lineHeight': '1.8',

                                          'fontSize': '16px', 'marginBottom': '30px'}),

            html.P(html.Strong("By continuing, you acknowledge that you have read this information and consent to participate."),

                   style={'marginBottom': '20px', 'fontSize': '16px'}),

            html.Button('Acknowledge and Continue', id='acknowledge-consent-btn', n_clicks=0,

                       style={'width': '100%', 'padding': '15px', 'fontSize': '18px',

                             'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',

                             'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'})

        ])

    ])



# # --- NEW: System Briefing Screen ---

# def system_briefing_screen():

#     text = """

# In this study, you will act as a robot swarm operator. You will observe and interact with a simulated mission in which three robots work together to collect packages and deliver them to designated drop-off locations. Your role is to monitor their progress throughout the mission.



# You will watch four short videos, each demonstrating different conditions. The main difference between them is their communication styles:



# In one style, messages are sent only when the system identifies a meaningful change.

# In the other, messages are sent routinely at regular intervals.



# Additionally, you will experience two different visual layouts: one that includes a map view showing robot movements, and another that presents text-only updates describing their statuses.



# The purpose of this study is to understand how different communication styles and visual layouts affect an operator’s ability to maintain awareness during a mission.



# Your task is to stay aware of what is happening in the mission and monitor updates as you receive them. As the robots explore, they will send you information about what they encounter. Robots may replan their routes if a path becomes blocked or if environmental or technical factors cause delays. When a robot sends a message, you will see an indicator appear—click the indicator to view the message content. This interaction helps us track when you receive and acknowledge each update.

# """

#     return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

#                           'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',

#                           'justifyContent': 'center', 'fontFamily': 'Arial', 'padding': '20px'}, children=[

#         html.H1("System Briefing", style={'color': '#00ff88', 'marginBottom': '30px'}),

#         html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

#                        'maxWidth': '800px', 'width': '100%', 'maxHeight': '70vh', 'overflowY': 'auto'}, children=[

#             dcc.Markdown(text, style={'whiteSpace': 'pre-wrap', 'lineHeight': '1.8',

#                                           'fontSize': '16px', 'marginBottom': '30px'}),

#             html.Button('Continue to Training Video', id='acknowledge-system-briefing-btn', n_clicks=0,

#                        style={'width': '100%', 'padding': '15px', 'fontSize': '18px',

#                              'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',

#                              'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'})

#         ])

#     ])

def system_briefing_screen():
    text = """
In this study, you will act as a robot swarm operator. You will observe and interact with a simulated mission in which three robots work together to collect packages and deliver them to designated drop-off locations. Your role is to monitor their progress throughout the mission.

You will watch four short videos, each demonstrating different conditions. The main difference between them is their communication styles:

In one style, messages are sent only when the system identifies a meaningful change.
In the other, messages are sent routinely at regular intervals.

Additionally, you will experience two different visual layouts: one that includes a map view showing robot movements, and another that presents text-only updates describing their statuses.

The purpose of this study is to understand how different communication styles and visual layouts affect an operator’s ability to maintain awareness during a mission.

Your task is to stay aware of what is happening in the mission and monitor updates as you receive them. As the robots explore, they will send you information about what they encounter. Robots may replan their routes if a path becomes blocked or if environmental or technical factors cause delays. **<mark style="background-color: #00ff88; color: #1e1e1e; padding: 2px 4px; border-radius: 4px;">When a robot sends a message, you will see an indicator appear—click the indicator to view the message content.</mark>** This interaction helps us track when you receive and acknowledge each update.
"""
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                          'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',
                          'justifyContent': 'center', 'fontFamily': 'Arial', 'padding': '20px'}, children=[
        html.H1("System Briefing", style={'color': '#00ff88', 'marginBottom': '30px'}),
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                       'maxWidth': '800px', 'width': '100%', 'maxHeight': '70vh', 'overflowY': 'auto'}, children=[
            dcc.Markdown(text, 
                         dangerously_allow_html=True,  # <--- Essential for the highlight to work
                         style={'whiteSpace': 'pre-wrap', 'lineHeight': '1.8',
                                'fontSize': '16px', 'marginBottom': '30px'}),
            html.Button('Continue to Training Video', id='acknowledge-system-briefing-btn', n_clicks=0,
                       style={'width': '100%', 'padding': '15px', 'fontSize': '18px',
                             'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',
                             'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'})
        ])
    ])


# --- NEW: Training Video Screen ---
def video_training_screen():
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                           'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',
                           'justifyContent': 'center', 'fontFamily': 'Arial', 'padding': '20px'}, children=[
        html.H1("Training Video", style={'color': '#00ff88', 'marginBottom': '30px'}),
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '20px', 'borderRadius': '10px',
                        'maxWidth': '800px', 'width': '100%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            
            # Fixed Iframe: Removed 'allowFullScreen' causing the crash
            html.Iframe(
                src=TRAINING_VIDEO_URL, 
                title="YouTube video player",
                style={'width': '100%', 'height': '450px', 'border': 'none', 'marginBottom': '20px'},
                # Added 'fullscreen' to the allow string as a fallback
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen"
            ),
            
            html.Button('Continue to Experiment', id='acknowledge-video-btn', n_clicks=0,
                        style={'width': '100%', 'padding': '15px', 'fontSize': '18px',
                               'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',
                               'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'})
        ])
    ])


#local
# # --- NEW: Training Video Screen (Local File Version) ---
# def video_training_screen():
#     return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
#                            'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',
#                            'justifyContent': 'center', 'fontFamily': 'Arial', 'padding': '20px'}, children=[
#         html.H1("Training Video", style={'color': '#00ff88', 'marginBottom': '30px'}),
#         html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '20px', 'borderRadius': '10px',
#                         'maxWidth': '800px', 'width': '100%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            
#             # UPDATED: Use html.Video for local playback
#             # Ensure 'training_video.mp4' is inside the 'assets' folder
#             html.Video(
#                 src="/assets/training_video.mp4", 
#                 controls=True,
#                 style={'width': '100%', 'height': 'auto', 'marginBottom': '20px', 'outline': 'none'}
#             ),
            
#             html.Button('Continue to Experiment', id='acknowledge-video-btn', n_clicks=0,
#                         style={'width': '100%', 'padding': '15px', 'fontSize': '18px',
#                                'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',
#                                'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'})
#         ])
#     ])





# Resolution: 720p or 1080p.

# Bitrate: Use a tool like HandBrake or ffmpeg to lower the file size to under 20MB.

# Format: .mp4 (H.264 codec) – this plays natively in every browser without overhead.
# # --- NEW: Training Video Screen (Local File Version) ---
# def video_training_screen():
#     return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
#                            'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',
#                            'justifyContent': 'center', 'fontFamily': 'Arial', 'padding': '20px'}, children=[
#         html.H1("Training Video", style={'color': '#00ff88', 'marginBottom': '30px'}),
#         html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '20px', 'borderRadius': '10px',
#                         'maxWidth': '800px', 'width': '100%', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}, children=[
            
#             # UPDATED: Use html.Video for local playback
#             # This assumes you placed 'training_video.mp4' inside the 'assets' folder
#             # The browser handles the buffering automatically.
#             html.Video(
#                 src="/assets/training_video.mp4", 
#                 controls=True,
#                 # 'autoPlay' is often blocked by browsers with sound, so we let them click play
#                 # 'controlsList="nodownload"' stops them from downloading it easily
#                 controlsList="nodownload",
#                 style={'width': '100%', 'height': 'auto', 'marginBottom': '20px', 'outline': 'none'}
#             ),
            
#             html.Button('Continue to Experiment', id='acknowledge-video-btn', n_clicks=0,
#                         style={'width': '100%', 'padding': '15px', 'fontSize': '18px',
#                                'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',
#                                'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'})
#         ])
#     ])


def welcome_screen():

    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

                          'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',

                          'justifyContent': 'center', 'fontFamily': 'Arial'}, children=[

        html.H1("Multi-Agent Task Planner User Study", style={'color': '#00ff88', 'marginBottom': '30px'}),

        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

                       'maxWidth': '500px', 'width': '100%'}, children=[

            html.H3("Welcome!", style={'marginBottom': '20px'}),

            html.P("Thank you for participating in this study. Please enter your Prolific ID to begin.",

                  style={'marginBottom': '30px'}),

            dcc.Input(id='participant-name-input', type='text', placeholder='Enter Prolific ID',

                     style={'width': '100%', 'padding': '10px', 'marginBottom': '20px',

                           'fontSize': '16px', 'borderRadius': '5px', 'border': '1px solid #444'}),

            html.Button('Start Study', id='start-study-btn', n_clicks=0,

                       style={'width': '100%', 'padding': '15px', 'fontSize': '18px',

                             'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',

                             'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'}),

            html.Div(id='name-error', style={'color': '#ff4444', 'marginTop': '10px'})

        ])

    ])



def briefing_screen(run_number, total_runs, scenario_num, view_type, framework_mode):

    view_name = "Simulator View (Map + Log)" if view_type == 'map' else "Textual Overview"

    framework_name = "WITH Communication Framework" if framework_mode == 'with_framework' else "WITHOUT Communication Framework"

    scenario_briefing = SCENARIO_CONTENT.get(scenario_num, {}).get('briefing', "No briefing text found.")

    briefing_text = f"""

{scenario_briefing}



---

**This run will use:**

- {view_name}

- {framework_name}

---



In this scenario, you will monitor three robots delivering packages.

The simulation will pause automatically at several points to ask you questions.

Please pay close attention to all robot activities and system messages.



Click "Begin Scenario" when you're ready to start.

"""

    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

                          'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',

                          'justifyContent': 'center', 'fontFamily': 'Arial'}, children=[

        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

                       'maxWidth': '800px', 'width': '90%'}, children=[

            html.H2(f"Run {run_number} / {total_runs} - Briefing",

                   style={'color': '#00ff88', 'marginBottom': '30px'}),

            dcc.Markdown(briefing_text, style={'whiteSpace': 'pre-wrap', 'lineHeight': '1.8',

                                          'fontSize': '16px'}),

            html.Button('Begin Scenario', id='begin-scenario-btn', n_clicks=0,

                       style={'padding': '15px 40px', 'fontSize': '18px',

                             'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',

                             'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold', 'marginTop': '30px'})

        ])

    ])



def create_pause_question_screen(scenario_num, question_idx):

    question_num = question_idx + 1

    try:

        question_data = SCENARIO_CONTENT[scenario_num]['questions'][question_idx]

    except Exception:

        question_data = {"text": "Error: Could not load question.", "options": ["Continue"]}

    multi_select_questions = [(2, 0), (6, 0)]

    question_key = (scenario_num, question_idx)

    InputComponent = dcc.Checklist if question_key in multi_select_questions else dcc.RadioItems

        

    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

                          'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',

                          'justifyContent': 'center', 'fontFamily': 'Arial'}, children=[

        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

                       'maxWidth': '1000px', 'margin': '0 auto', 'width': '90%'}, children=[

            html.H2(f"Scenario {scenario_num} - Question #{question_num}",

                   style={'color': '#00ff88', 'marginBottom': '40px'}),

            html.P(question_data['text'], style={'fontWeight': 'bold', 'marginBottom': '25px', 'fontSize': '18px'}),

            InputComponent(

                id='pause-question-radio',

                options=[{'label': opt, 'value': opt} for opt in question_data['options']],

                labelStyle={'display': 'block', 'marginBottom': '15px', 'cursor': 'pointer', 'fontSize': '16px'},

                style={'marginBottom': '20px'}

            ),

            html.Button('Continue', id='submit-pause-question-btn', n_clicks=0,

                       style={'padding': '15px 40px', 'fontSize': '18px', 'backgroundColor': '#00ff88',

                             'color': '#1e1e1e', 'border': 'none', 'borderRadius': '5px',

                             'cursor': 'pointer', 'fontWeight': 'bold', 'marginTop': '30px'})

        ])

    ])



def create_post_scenario_questionnaire(scenario_num, run_number, total_runs):

    questions = [

        {'id': 'mental_demand', 'text': 'Mental Demand: How mentally demanding was monitoring the robots during this segment?', 'options': ['1 - Very Low', '2 - Low', '3 - Moderate', '4 - High', '5 - Very High']},

        {'id': 'physical_demand', 'text': 'Physical Demand: How physically demanding was the task (e.g., mouse clicks, visual tracking)?', 'options': ['1 - Very Low', '2 - Low', '3 - Moderate', '4 - High', '5 - Very High']},

        {'id': 'temporal_demand', 'text': 'Temporal Demand: How hurried or rushed did the pace of the task feel?', 'options': ['1 - Very Low', '2 - Low', '3 - Moderate', '4 - High', '5 - Very High']},

        {'id': 'performance', 'text': 'Performance: How successful were you in accomplishing what you were asked to do?', 'options': ['1 - Very Poor', '2 - Poor', '3 - Moderate', '4 - Good', '5 - Excellent']},

        {'id': 'effort', 'text': 'Effort: How hard did you have to work to achieve your level of performance?', 'options': ['1 - Very Low', '2 - Low', '3 - Moderate', '4 - High', '5 - Very High']},

        {'id': 'frustration', 'text': 'Frustration: How irritated, stressed, or discouraged did you feel during this segment?', 'options': ['1 - Very Low', '2 - Low', '3 - Moderate', '4 - High', '5 - Very High']},

    ]



    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

                          'padding': '40px', 'fontFamily': 'Arial', 'overflowY': 'auto'}, children=[

        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

                       'maxWidth': '1000px', 'margin': '0 auto'}, children=[

            html.H2(f"End of Run {run_number}/{total_runs} (Scenario {scenario_num}) - Questionnaire",

                   style={'color': '#00ff88', 'marginBottom': '40px'}),

            html.Div([

                html.Div([

                    html.P(q['text'], style={'fontWeight': 'bold', 'marginBottom': '15px', 'fontSize': '16px', 'marginTop': '25px'}),

                    dcc.RadioItems(

                        id={'type': 'post-scenario-question', 'id': q['id']},

                        options=[{'label': opt, 'value': opt} for opt in q['options']],

                        labelStyle={'display': 'block', 'marginBottom': '10px', 'cursor': 'pointer'},

                        style={'marginBottom': '20px'}

                    )

                ], style={'marginBottom': '20px'}) for q in questions

            ]),

            html.Button('Submit and Continue', id='submit-post-scenario-btn', n_clicks=0,

                       style={'padding': '15px 40px', 'fontSize': '18px', 'backgroundColor': '#00ff88',

                             'color': '#1e1e1e', 'border': 'none', 'borderRadius': '5px',

                             'cursor': 'pointer', 'fontWeight': 'bold', 'marginTop': '30px'})

        ])

    ])



# def post_study_questionnaire():

#     questions = [

#         # --- NEW: Ranking Question ---

#         {'text': 'Please rank the following demonstration types based on how useful they were for understanding and monitoring the robot swarm. (Please type your order preference below: Map–Improved, Map–Default, Text–Improved, Text–Default)', 'type': 'open', 'id': 'ranking'},

        

#         # --- NEW: Specific Improved + Map Questions ---

#         {'text': 'The following questions pertain to your experience with the system that utilized our improved communication and the map view. How effective were the update messages in helping you understand the robots\' behavior?', 'type': 'scale', 'id': 'improved_map_effectiveness', 'options': ['1 - Not at all effective', '2', '3', '4', '5 - Extremely effective']},

#         {'text': 'How did this differ between demonstration types?', 'type': 'open', 'id': 'improved_map_effectiveness_detail'},

#         {'text': 'How easy was it to tell why a robot replanned or changed its route? (1 = Very difficult | 5 = Very easy)', 'type': 'scale', 'id': 'replan_clarity', 'options': ['1 - Very difficult', '2', '3', '4', '5 - Very easy']},

#         {'text': 'What, if anything, was confusing about the robots\' behavior or the updates you received? How did this differ between demonstration types?', 'type': 'open', 'id': 'confusion_detail'},

#         {'text': 'Do you have any additional thoughts or feedback about the communication styles or the interface overall?', 'type': 'open', 'id': 'final_feedback'}

#     ]

    

#     return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

#                           'padding': '40px', 'fontFamily': 'Arial', 'overflowY': 'auto'}, children=[

#         html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

#                        'maxWidth': '1000px', 'margin': '0 auto'}, children=[

#             html.H2("Final Interview", style={'color': '#00ff88', 'marginBottom': '20px'}),

#             html.P("You may end the evaluation here. If you are willing to answer additional questions to assist in our understanding of your experience, please continue forward.",

#                   style={'marginBottom': '40px', 'fontSize': '16px'}),

#             html.Div([

#                 html.Div([

#                     html.P(q['text'], style={'fontWeight': 'bold', 'marginBottom': '15px', 'fontSize': '16px', 'marginTop': '25px'}),

#                     (

#                         dcc.RadioItems(

#                             id={'type': 'post-study-question', 'id': q['id']},

#                             options=[{'label': opt, 'value': opt} for opt in q['options']],

#                             labelStyle={'display': 'inline-block', 'marginRight': '20px', 'cursor': 'pointer'},

#                             style={'marginBottom': '20px'}

#                         ) if q['type'] == 'scale' else dcc.Textarea(

#                             id={'type': 'post-study-question', 'id': q['id']}, placeholder='Type your response here...',

#                             style={'width': '100%', 'minHeight': '100px', 'padding': '10px', 'fontSize': '14px',

#                                   'borderRadius': '5px', 'marginBottom': '20px', 'border': '1px solid #444',

#                                   'backgroundColor': '#1a1a1a', 'color': 'white'}

#                         )

#                     )

#                 ], style={'marginBottom': '20px'}) for q in questions

#             ]),

#             html.Button('Submit and Complete Study', id='submit-final-btn', n_clicks=0,

#                        style={'padding': '15px 40px', 'fontSize': '18px', 'backgroundColor': '#00ff88',

#                              'color': '#1e1e1e', 'border': 'none', 'borderRadius': '5px',

#                              'cursor': 'pointer', 'fontWeight': 'bold', 'marginTop': '30px'})

#         ])

#     ])


def post_study_questionnaire():
    questions = [
        # --- Ranking Question ---
        {'text': 'Please rank the following demonstration types based on how useful they were for understanding and monitoring the robot swarm. (Please type your order preference below: Map–Improved, Map–Default, Text–Improved, Text–Default)', 'type': 'open', 'id': 'ranking'},
        
        # --- Specific Improved + Map Questions ---
        {'text': 'The following questions pertain to your experience with the system that utilized our improved communication and the map view. How effective were the update messages in helping you understand the robots\' behavior?', 'type': 'scale', 'id': 'improved_map_effectiveness', 'options': ['1 - Not at all effective', '2', '3', '4', '5 - Extremely effective']},
        {'text': 'How did this differ between demonstration types?', 'type': 'open', 'id': 'improved_map_effectiveness_detail'},
        {'text': 'How easy was it to tell why a robot replanned or changed its route? (1 = Very difficult | 5 = Very easy)', 'type': 'scale', 'id': 'replan_clarity', 'options': ['1 - Very difficult', '2', '3', '4', '5 - Very easy']},
        {'text': 'What, if anything, was confusing about the robots\' behavior or the updates you received? How did this differ between demonstration types?', 'type': 'open', 'id': 'confusion_detail'},
        {'text': 'Do you have any additional thoughts or feedback about the communication styles or the interface overall?', 'type': 'open', 'id': 'final_feedback'}
    ]
    
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                          'padding': '40px', 'fontFamily': 'Arial', 'overflowY': 'auto'}, children=[
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                       'maxWidth': '1000px', 'margin': '0 auto'}, children=[
            html.H2("Final Interview (Optional)", style={'color': '#00ff88', 'marginBottom': '20px'}),
            html.P("You have completed the main study. You may end the evaluation here using the 'Skip' button, or answer the questions below to help us improve.",
                  style={'marginBottom': '40px', 'fontSize': '16px'}),
            html.Div([
                html.Div([
                    html.P(q['text'], style={'fontWeight': 'bold', 'marginBottom': '15px', 'fontSize': '16px', 'marginTop': '25px'}),
                    (
                        dcc.RadioItems(
                            id={'type': 'post-study-question', 'id': q['id']},
                            options=[{'label': opt, 'value': opt} for opt in q['options']],
                            labelStyle={'display': 'inline-block', 'marginRight': '20px', 'cursor': 'pointer'},
                            style={'marginBottom': '20px'}
                        ) if q['type'] == 'scale' else dcc.Textarea(
                            id={'type': 'post-study-question', 'id': q['id']}, placeholder='Type your response here...',
                            style={'width': '100%', 'minHeight': '100px', 'padding': '10px', 'fontSize': '14px',
                                  'borderRadius': '5px', 'marginBottom': '20px', 'border': '1px solid #444',
                                  'backgroundColor': '#1a1a1a', 'color': 'white'}
                        )
                    )
                ], style={'marginBottom': '20px'}) for q in questions
            ]),
            
            # --- BUTTON CONTAINER ---
            html.Div(style={'display': 'flex', 'gap': '20px', 'marginTop': '30px'}, children=[
                html.Button('Submit Answers', id='submit-final-btn', n_clicks=0,
                           style={'padding': '15px 40px', 'fontSize': '18px', 'backgroundColor': '#00ff88',
                                 'color': '#1e1e1e', 'border': 'none', 'borderRadius': '5px',
                                 'cursor': 'pointer', 'fontWeight': 'bold'}),
                
                # NEW SKIP BUTTON
                html.Button('Skip & Finish', id='skip-final-btn', n_clicks=0,
                           style={'padding': '15px 40px', 'fontSize': '18px', 'backgroundColor': '#666',
                                 'color': 'white', 'border': 'none', 'borderRadius': '5px',
                                 'cursor': 'pointer', 'fontWeight': 'bold'})
            ])
        ])
    ])
    
    

def create_simulation_layout():

    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'fontFamily': 'Arial', 'height': '100vh', 'display': 'flex', 'flexDirection': 'column'}, children=[

        html.H1("Multi-Agent Task Planner Simulation",

               style={'textAlign': 'center', 'color': '#00ff88', 'flexShrink': 0}),

        html.Div(id='study-context-header', style={'textAlign': 'center', 'padding': '5px', 'backgroundColor': '#2b2b2b', 'borderBottom': '2px solid #444'}),

        html.Div(id='main-content-area', style={'flexGrow': 1, 'overflow': 'hidden', 'padding': '20px'}, children=[

            html.Div(id='simulation-layout-loaded-signal', style={'display': 'none'}),

            

            # MAP VIEW

            html.Div(id='map-view-container', style={'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}, children=[

                html.Div(style={'width': '70%', 'height': '100%'}, children=[dcc.Graph(id='simulation-graph', figure=initial_figure)]),

                html.Div(style={'width': '30%', 'height': '100%', 'display': 'flex', 'flexDirection': 'column', 'gap': '10px', 'overflow': 'hidden'}, children=[

                    html.Div(style={'flex': '1', 'overflowY': 'auto', 'backgroundColor': '#1a1a1a', 'border': '1px solid #666', 'borderRadius': '3px', 'padding': '15px'}, children=[

                        html.H3("Message Logs", style={'color': '#00ff88', 'textAlign': 'center', 'flexShrink': 0}),

                        html.Div(id='all-messages-feed', className='message-box-dark-theme')

                    ]),

                ])

            ]),

            

            # TEXT VIEW

            html.Div(id='text-view-container', style={'display': 'none', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}, children=[

                *[html.Div(className='robot-column', children=[

                    html.Div(className='robot-card-top', children=[dcc.Slider(id=f'robot-{i}-timeline', min=0, max=49, value=0, disabled=True, marks={}, tooltip={"always_visible": False})]),

                    html.Div(className='robot-card-bottom', children=[

                        html.H3(f'Robot {i} Status', style={'textAlign': 'center', 'color': '#333'}),

                        html.Div(id=f'robot-{i}-messages', className='message-box')

                    ])

                ]) for i in range(1, 4)],

                dcc.Graph(

                    id='simulation-map-snapshot',

                    figure=initial_figure,

                    config={'staticPlot': True, 'displayModeBar': False},

                    style={'width': '300px', 'height': '200px', 'border': '1px solid #666'}

                )

            ]),

        ]),

    ])



def thank_you_screen():
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                           'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',
                           'justifyContent': 'center', 'fontFamily': 'Arial'}, children=[
        html.H1("Thank You!", style={'color': '#00ff88', 'marginBottom': '30px'}),
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                        'maxWidth': '600px', 'textAlign': 'center'}, children=[
            html.H3("Study Complete", style={'marginBottom': '20px'}),
            html.P("Thank you for participating in this study. Your responses have been recorded.",
                   style={'fontSize': '18px', 'lineHeight': '1.6'}),
            
            # --- NEW: Completion Code Section ---
            html.Div(style={'marginTop': '30px', 'marginBottom': '30px', 'padding': '20px', 
                            'backgroundColor': '#1e1e1e', 'borderRadius': '5px', 'border': '1px solid #00ff88'}, children=[
                html.P("Your Completion Code is:", style={'color': '#aaa', 'marginBottom': '10px', 'fontSize': '16px'}),
                # The code you provided:
                html.H2("CUWHCZ1Z", style={'color': '#00ff88', 'margin': '0', 'fontSize': '32px', 'letterSpacing': '2px', 'fontWeight': 'bold'})
            ]),

            html.P("Please copy this code and send this code to the researcher to receive your compensation.", 
                   style={'fontSize': '16px', 'color': '#ccc', 'marginBottom': '10px'}),
            
            html.P("You may now close this window.", style={'marginTop': '30px', 'color': '#888'})
        ])
    ])
    
    
    

# def thank_you_screen():

#     return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',

#                           'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',

#                           'justifyContent': 'center', 'fontFamily': 'Arial'}, children=[

#         html.H1("Thank You!", style={'color': '#00ff88', 'marginBottom': '30px'}),

#         html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',

#                        'maxWidth': '600px', 'textAlign': 'center'}, children=[

#             html.H3("Study Complete", style={'marginBottom': '20px'}),

#             html.P("Thank you for participating in this study. Your responses have been recorded.",

#                   style={'fontSize': '18px', 'lineHeight': '1.6'}),

#             html.P("You may now close this window.", style={'marginTop': '30px', 'color': '#888'})

#         ])

#     ])



app.layout = html.Div([

    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content', children=welcome_screen()),

    dcc.Store(id='participant-store', data={}),

    dcc.Store(id='study-state-store', data={}),

    dcc.Store(id='scenario-data-store'),

    dcc.Store(id='current-frame-store', data=0),

    dcc.Store(id='hmm-data-store'),

    dcc.Store(id='open-messages-store', data=[]),

    dcc.Store(id='all-messages-store', data=[]),

    dcc.Store(id='responses-store', data=[]),

    dcc.Store(id='interaction-log-store', data=[]),

    dcc.Store(id='message-timestamps-store', data={}),

    dcc.Store(id='robot-1-messages-store', data=[]),

    dcc.Store(id='robot-2-messages-store', data=[]),

    dcc.Store(id='robot-3-messages-store', data=[]),

    dcc.Store(id='all-message-logs-store', data=[]),

    html.Div(id='message-click-relay', style={'display': 'none'}),

    dcc.Interval(id='animation-interval', interval=UPDATE_INTERVAL_MS, n_intervals=0, disabled=True),

    dcc.Interval(id='click-logger-interval', interval=CLICK_POLL_INTERVAL_MS, n_intervals=0, disabled=True) 

])



app.clientside_callback(

    """

    function(n_intervals) {

        if (!window.messageClickQueue) {

            window.messageClickQueue = [];

        }

        const detailsElements = document.querySelectorAll('details[id*="status-message"]');

        detailsElements.forEach(function(details) {

            if (details.dataset.listenerAttached) {

                return; 

            }

            details.dataset.listenerAttached = 'true'; 

            details.addEventListener('toggle', function(event) {

                const idAttr = details.getAttribute('id');

                let messageIdStr = '';

                try {

                    const idObj = JSON.parse(idAttr.replace(/'/g, '"'));

                    messageIdStr = idObj.id;

                } catch (e) {

                    messageIdStr = idAttr;

                }

                const isOpen = details.open;

                const clickData = {

                    messageId: messageIdStr,

                    isOpen: isOpen,

                    timestamp: Date.now()

                };

                window.messageClickQueue.push(JSON.stringify(clickData));

            });

        });

        if (window.messageClickQueue.length > 0) {

            const dataToReturn = JSON.stringify(window.messageClickQueue); 

            window.messageClickQueue = []; 

            return dataToReturn;

        }

        return null;

    }

    """,

    Output('message-click-relay', 'children'),

    Input('click-logger-interval', 'n_intervals') 

)



@app.callback(

    Output('interaction-log-store', 'data', allow_duplicate=True),

    Output('all-message-logs-store', 'data', allow_duplicate=True),

    Output('open-messages-store', 'data', allow_duplicate=True), 

    Input('message-click-relay', 'children'),

    State('interaction-log-store', 'data'),

    State('all-message-logs-store', 'data'),

    State('open-messages-store', 'data'), 

    State('participant-store', 'data'),

    State('study-state-store', 'data'),

    State('current-frame-store', 'data'),

    prevent_initial_call=True

)

def log_message_clicks(click_data_json_array, interactions, all_message_logs, 

                             open_message_ids, 

                             participant_data, study_state, frame_idx):

    if not click_data_json_array or not all([participant_data, study_state, all_message_logs]):

        raise PreventUpdate

    new_interactions = interactions.copy() if interactions is not None else []

    new_all_message_logs = all_message_logs.copy()

    new_open_message_ids = set(open_message_ids.copy() if open_message_ids is not None else [])

    try:

        click_data_list = json.loads(click_data_json_array)

        for click_data in click_data_list:

            click_info = json.loads(click_data)

            is_open = click_info.get('isOpen', False)

            message_id = click_info.get('messageId', '')

            if is_open:

                new_open_message_ids.add(message_id) 

            else:

                new_open_message_ids.discard(message_id)

            if is_open:

                message_found = False

                for entry in new_all_message_logs:

                    if entry['message_id'] == message_id:

                        message_found = True

                        if entry['clicked'] == 0:

                            click_time_unix = click_info.get('timestamp', time.time() * 1000) / 1000.0

                            click_time_iso = datetime.fromtimestamp(click_time_unix).isoformat()

                            action = "opened"

                            entry['click_timestamp_unix'] = click_time_unix

                            entry['click_timestamp_iso'] = click_time_iso

                            entry['time_to_click_seconds'] = click_time_unix - entry['appear_timestamp_unix']

                            entry['clicked'] = 1 

                            current_run_idx = study_state.get('current_run_idx', 0)

                            current_run_info = participant_data['track'][current_run_idx]

                            scenario_num = current_run_info[0]

                            condition_idx = current_run_info[1]

                            interaction_entry = {

                                'timestamp_iso': click_time_iso,

                                'timestamp_unix': click_time_unix,

                                'participant': participant_data.get('id'),

                                'scenario': scenario_num,

                                'condition': condition_idx,

                                'frame': frame_idx,

                                'type': 'message_click',

                                'message_id': message_id,

                                'action': action,

                            }

                            new_interactions.append(interaction_entry)

                        break

    except Exception as e:

        print(f"Error logging message click: {e}")

    return new_interactions, new_all_message_logs, list(new_open_message_ids)



@app.callback(

    Output('page-content', 'children'),

    Output('participant-store', 'data'),

    Output('study-state-store', 'data'),

    Output('name-error', 'children'),

    Input('start-study-btn', 'n_clicks'),

    State('participant-name-input', 'value'),

    prevent_initial_call=True

)

def start_study(n_clicks, name):

    if not name or len(name.strip()) < 2:

        return no_update, no_update, no_update, "Please enter your Prolific ID."

    os.makedirs('study_data', exist_ok=True)

    lock = FileLock(PARTICIPANT_COUNT_LOCK, timeout=10)

    try:

        with lock:

            try:

                with open(PARTICIPANT_COUNT_FILE, 'r') as f:

                    current_count = int(f.read().strip())

            except (FileNotFoundError, ValueError):

                current_count = 0

            track_idx = current_count % 24

            assigned_track = STUDY_DESIGN_TABLE[track_idx]

            with open(PARTICIPANT_COUNT_FILE, 'w') as f:

                f.write(str(current_count + 1))

            print(f"Participant {current_count + 1} ('{name}') assigned to ComboID C{track_idx + 1:02d} with track: {assigned_track}")

    except Exception as e:

        print(f"FATAL ERROR: Could not acquire lock or assign participant track. {e}")

        error_msg = "Error assigning participant. Please try again or contact the administrator."

        return no_update, no_update, no_update, error_msg

    participant_id = generate_participant_id(name)

    participant_data = {

        'id': participant_id,

        'name': name,

        'track': assigned_track,

        'start_time': datetime.now().isoformat()

    }

    study_state = {

        'current_run_idx': 0,

        'current_question_idx': 0,

        'phase': 'consent', 

        'segment_start_time': None

    }

    return consent_screen(), participant_data, study_state, ""
    # return thank_you_screen(), participant_data, study_state, ""


# --- NEW: Sequence Logic for new screens ---



@app.callback(

    Output('page-content', 'children', allow_duplicate=True),

    Input('acknowledge-consent-btn', 'n_clicks'),

    State('study-state-store', 'data'),

    prevent_initial_call=True

)

def acknowledge_consent(n_clicks, study_state):

    if n_clicks is None or n_clicks == 0: raise PreventUpdate

    study_state['phase'] = 'system_briefing'

    return system_briefing_screen()



@app.callback(

    Output('page-content', 'children', allow_duplicate=True),

    Input('acknowledge-system-briefing-btn', 'n_clicks'),

    State('study-state-store', 'data'),

    prevent_initial_call=True

)

def acknowledge_system_briefing(n_clicks, study_state):

    if n_clicks is None or n_clicks == 0: raise PreventUpdate

    study_state['phase'] = 'video_training'

    return video_training_screen()



@app.callback(

    Output('page-content', 'children', allow_duplicate=True),

    Input('acknowledge-video-btn', 'n_clicks'),

    State('study-state-store', 'data'),

    State('participant-store', 'data'),

    prevent_initial_call=True

)

def acknowledge_video(n_clicks, study_state, participant_data):

    if n_clicks is None or n_clicks == 0: raise PreventUpdate

    study_state['phase'] = 'briefing'

    

    current_run_idx = study_state['current_run_idx']

    total_runs = len(participant_data['track'])

    first_run_info = participant_data['track'][current_run_idx]

    scenario_num = first_run_info[0]

    condition_idx = first_run_info[1]

    view_type, framework_mode = get_condition_names(condition_idx)

    

    return briefing_screen(current_run_idx + 1, total_runs, scenario_num, view_type, framework_mode)



@app.callback(

    Output('page-content', 'children', allow_duplicate=True),

    Output('study-state-store', 'data', allow_duplicate=True),

    Input('begin-scenario-btn', 'n_clicks'),

    State('study-state-store', 'data'),

    State('participant-store', 'data'),

    prevent_initial_call=True

)

def begin_scenario(n_clicks, study_state, participant_data):

    if n_clicks == 0 or not study_state or not participant_data:

        raise PreventUpdate

    new_study_state = study_state.copy()

    new_study_state['phase'] = 'simulation'

    new_study_state['segment_start_time'] = datetime.now().isoformat()

    return create_simulation_layout(), new_study_state




@app.callback(
    Output('scenario-data-store', 'data'), # This will now receive None
    Output('hmm-data-store', 'data'),
    Output('current-frame-store', 'data', allow_duplicate=True),
    Output('robot-1-timeline', 'max'),
    Output('robot-2-timeline', 'max'),
    Output('robot-3-timeline', 'max'),
    Output('robot-1-timeline', 'marks'),
    Output('robot-2-timeline', 'marks'),
    Output('robot-3-timeline', 'marks'),
    Output('all-messages-store', 'data', allow_duplicate=True),
    Output('open-messages-store', 'data', allow_duplicate=True),
    Output('message-timestamps-store', 'data', allow_duplicate=True),
    Output('robot-1-messages-store', 'data', allow_duplicate=True),
    Output('robot-2-messages-store', 'data', allow_duplicate=True),
    Output('robot-3-messages-store', 'data', allow_duplicate=True),
    Input('simulation-layout-loaded-signal', 'children'),
    State('study-state-store', 'data'),
    State('participant-store', 'data'),
    prevent_initial_call=True
)

def load_data_and_start_simulation(layout_signal, study_state, participant_data):
    if not study_state or study_state.get('phase') != 'simulation' or not participant_data:
        raise PreventUpdate
    
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    
    # Load into SERVER cache (returns the data, but we won't send it to client)
    frames = load_scenario_frames(scenario_num) 
    
    HMM_Robot_1, HMM_Robot_2, HMM_Robot_3 = get_hmms_for_active_scenario(scenario_num)
    hmms = {'robot1': HMM_Robot_1, 'robot2': HMM_Robot_2, 'robot3': HMM_Robot_3}
    
    start_frame = 0
    pause_points = PAUSE_POINTS.get(scenario_num, [100, 200, 300])
    if study_state['current_question_idx'] > 0:
        start_frame = pause_points[study_state['current_question_idx'] - 1] + 1
    
    max_frames = len(frames) - 1 if frames else 0
    mid_point = max_frames // 2
    marks = {0: 'Start', mid_point: 'Midpoint', max_frames: 'End'}

    # KEY CHANGE: Return None for the first output
    return None, hmms, start_frame, max_frames, max_frames, max_frames, marks, marks, marks, [], [], {}, [], [], []





@app.callback(

    Output('animation-interval', 'disabled'),

    Output('click-logger-interval', 'disabled'), 

    Input('study-state-store', 'data'),

)

def control_animation(study_state):

    if study_state and study_state.get('phase') == 'simulation':

        return False, False 

    return True, True 




@app.callback(
    Output('current-frame-store', 'data', allow_duplicate=True),
    Output('page-content', 'children', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
    Input('animation-interval', 'n_intervals'),
    State('current-frame-store', 'data'),
    # REMOVED: State('scenario-data-store', 'data'),
    State('study-state-store', 'data'),
    State('participant-store', 'data'),
    prevent_initial_call=True
)
def update_frame_and_check_pause(n_intervals, current_frame, study_state, participant_data):
    # Removed scenario_data from arguments
    if not study_state or study_state.get('phase') != 'simulation' or not participant_data:
        raise PreventUpdate

    # RETRIEVE DATA FROM CACHE
    current_run_idx = study_state['current_run_idx']
    scenario_num = participant_data['track'][current_run_idx][0]
    scenario_data = load_scenario_frames(scenario_num)

    if not scenario_data: raise PreventUpdate

    max_frames = len(scenario_data) - 1
    total_runs = len(participant_data['track'])
    
    # ... (The rest of the function logic is exactly the same as before) ...
    # just ensure you use 'scenario_data' variable we just loaded above
    
    if current_frame >= max_frames:
        new_state = study_state.copy()
        new_state['phase'] = 'post_scenario_questions' 
        new_page = create_post_scenario_questionnaire(scenario_num, current_run_idx + 1, total_runs)
        return no_update, new_page, new_state

    pause_points = PAUSE_POINTS.get(scenario_num, [100, 200, 300])
    current_question_idx = study_state['current_question_idx']
    
    if current_question_idx < len(pause_points):
        current_pause_point = pause_points[current_question_idx]
        if current_frame == current_pause_point:
            new_study_state = study_state.copy()
            new_study_state['phase'] = 'questions' 
            new_page = create_pause_question_screen(scenario_num, current_question_idx)
            return no_update, new_page, new_study_state
    
    next_frame = current_frame + 1
    return next_frame, no_update, no_update





@app.callback(

    Output('map-view-container', 'style'),

    Output('text-view-container', 'style'),

    Output('study-context-header', 'children'),

    Input('study-state-store', 'data'),

    State('participant-store', 'data'),

)

def programmatically_switch_view(study_state, participant_data):

    if not study_state or not participant_data:

        return {'display': 'none'}, {'display': 'none'}, ""

    if study_state.get('phase') != 'simulation':

        return {'display': 'none'}, {'display': 'none'}, ""

    

    current_run_idx = study_state['current_run_idx']

    current_run_info = participant_data['track'][current_run_idx]

    scenario_num = current_run_info[0]

    condition_idx = current_run_info[1]

    

    map_style = {'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}

    text_style = {'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}

    

    view_type, framework_mode = get_condition_names(condition_idx)

    view_name = "Simulator View (Map + Log)" if view_type == 'map' else "Textual Overview"

    framework_name = "WITH Communication Framework" if framework_mode == 'with_framework' else "WITHOUT Communication Framework"

    

    if view_type == 'map':

        map_style['display'] = 'flex'

        text_style['display'] = 'none'

    else:  

        map_style['display'] = 'none'

        text_style['display'] = 'flex'

    

    header_text = f"Run: {current_run_idx + 1} / {len(participant_data['track'])} | Scenario: {scenario_num} | View: {view_name} | Framework: {framework_name}"

    return map_style, text_style, header_text










@app.callback(
    Output('simulation-graph', 'figure'),
    Output('robot-1-messages-store', 'data', allow_duplicate=True),
    Output('robot-2-messages-store', 'data', allow_duplicate=True),
    Output('robot-3-messages-store', 'data', allow_duplicate=True),
    Output('robot-1-timeline', 'value'),
    Output('robot-2-timeline', 'value'),
    Output('robot-3-timeline', 'value'),
    Output('hmm-data-store', 'data', allow_duplicate=True),
    Output('all-messages-feed', 'children'),
    Output('all-messages-store', 'data', allow_duplicate=True),
    Output('animation-interval', 'interval'),
    Output('open-messages-store', 'data', allow_duplicate=True),
    Output('message-timestamps-store', 'data', allow_duplicate=True),
    Output('all-message-logs-store', 'data', allow_duplicate=True),
    Input('current-frame-store', 'data'),
    Input('study-state-store', 'data'),
    
    # REMOVED: State('scenario-data-store', 'data'),
    
    State('hmm-data-store', 'data'),
    State('participant-store', 'data'),
    [State(f'robot-{i}-messages-store', 'data') for i in range(1, 4)],
    State('open-messages-store', 'data'),
    State('all-messages-store', 'data'),
    State('message-timestamps-store', 'data'),
    State('all-message-logs-store', 'data'),
    prevent_initial_call=True
)
def update_simulation_views(frame_idx, study_state,
                            # REMOVED: scenario_data, 
                            hmm_data,
                            participant_data, hist1, hist2, hist3,
                            open_message_ids, all_messages_data_history,
                            message_timestamps, all_message_logs):
    
    # --- 1. Safety Checks ---
    if not study_state or study_state.get('phase') != 'simulation':
        return (no_update,) * 14

    current_open_message_ids = list(set(open_message_ids)) if open_message_ids else []
    new_message_timestamps = message_timestamps.copy() if message_timestamps else {}
    
    # Clean up history if it contains React components instead of data
    current_all_messages_data = all_messages_data_history or []
    if current_all_messages_data and isinstance(current_all_messages_data[0], dict) and 'props' in current_all_messages_data[0]:
        current_all_messages_data = []

    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    condition_idx = current_run_info[1]
    view_type, framework_mode = get_condition_names(condition_idx)

    # --- 2. RETRIEVE DATA FROM SERVER CACHE (Performance Fix) ---
    # We load directly from the server memory/disk rather than waiting for the client to send it
    scenario_data = load_scenario_frames(scenario_num)

    if not scenario_data or frame_idx >= len(scenario_data):
        current_fig = initial_figure
        try: current_fig = callback_context.outputs_list[0].get('value', initial_figure)
        except: pass
        # Return safely with no updates
        return (current_fig, hist1 or [], hist2 or [], hist3 or [], 
                frame_idx or 0, frame_idx or 0, frame_idx or 0,
                hmm_data, [], current_all_messages_data, UPDATE_INTERVAL_MS,
                current_open_message_ids, new_message_timestamps, no_update)

    # --- 3. HELPER: Direct Disk Writer (Memory Leak Fix) ---
    def write_log_to_disk(log_entry):
        log_file = f"study_data/{participant_data['id']}_message_logs.csv"
        file_exists = os.path.isfile(log_file)
        # Using the standard fieldnames from your existing code
        fieldnames = [
            'message_id', 'participant_id', 'scenario', 'condition', 'run_number',
            'frame', 'sim_time', 'robot_id', 'robot_state', 'robot_x', 'robot_y',
            'message_type', 'message_text', 'appear_timestamp_iso',
            'clicked', 'click_timestamp_iso', 'time_to_click_seconds', 
            'appear_timestamp_unix', 'click_timestamp_unix'
        ]
        try:
            with open(log_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                if not file_exists:
                    writer.writeheader()
                writer.writerow(log_entry)
        except Exception as e:
            print(f"Error writing log: {e}")

    # --- 4. Main Simulation Logic ---
    current_hmms = hmm_data.copy() if hmm_data else {}
    current_frame_data = scenario_data[frame_idx]
    
    # Generate the Map
    fig = create_figure_for_frame(static_map_data, current_frame_data)
    
    mission_time_threshold = THRESHOLD_VALUES['with_framework'].get(scenario_num, 1)
    robots_dict = current_frame_data.get('robots', {})
    packages = current_frame_data.get('packages', [])
    
    histories = [hist1, hist2, hist3]
    new_robot_message_outputs = [histories[0] or [], histories[1] or [], histories[2] or []]
    sim_time = current_frame_data.get('simulator time', 0)
    any_sync_occurred_with_framework = False
    
    new_messages_data_list = [] 
    
    # --- Robot Loop ---
    for i in range(1, 4):
        robot_id = f'robot{i}'
        if robot_id in robots_dict:
            raw_robot_data = robots_dict[robot_id]
            rmm_keys_to_select = ["state", "plan_index", "x", "y", "mission_time", "Current_weather", "Battery_status", 
                                  "Momentarily_offline", "Replan_flag", "target_package_id", "plan", 
                                  "immediate_goal_x", "immediate_goal_y", "Quadrant", "Bad_Terrain"]
            selected_robot_rmm_array = {'id': robot_id}
            for key in rmm_keys_to_select:
                selected_robot_rmm_array[key] = raw_robot_data.get(key)
            selected_robot_rmm_array['robot_time'] = sim_time
            
            selected_robot_hmm_array = current_hmms.get(robot_id)
            robot_info = {**robots_dict[robot_id], 'id': robot_id}
            
            sync_occurred = False 
            generate_message = False 
            
            # Update HMM Logic
            if framework_mode == 'with_framework':
                if selected_robot_hmm_array:
                    try:
                        updated_hmm_array, sync_occurred = dynamic_deviation_threshold_multi_logic(
                            hmm_array=selected_robot_hmm_array,
                            rmm_array=selected_robot_rmm_array,
                            update_logic_functions={},
                            uncertainty_factor_pos=0.1,
                            uncertainty_factor_time=0.1,
                            dynamic_threshold_mission_time=mission_time_threshold,
                            robot_id=robot_id
                        )
                    except Exception:
                        sync_occurred = False
                        updated_hmm_array = selected_robot_hmm_array
                    current_hmms[robot_id] = updated_hmm_array 
                    if sync_occurred: any_sync_occurred_with_framework = True 
            else: 
                interval = WITHOUT_FRAMEWORK_INTERVALS.get(scenario_num, 20) 
                if frame_idx > 0 and frame_idx % interval == 0:
                    generate_message = True

            # Force Message if Task Complete
            if framework_mode == 'with_framework' and robot_info.get('state') == 'all_tasks_complete':
                generate_message = True

            # Message Generation Attempt
            if sync_occurred or generate_message:
                new_message_data, message_type, message_text_for_log = create_rich_status_message_data(
                    robot_info, sim_time, packages, selected_robot_hmm_array, selected_robot_rmm_array, scenario_num, framework_mode
                )
                
                # Smart Suppression Logic
                should_send = True
                if new_message_data is None:
                    should_send = False
                else:
                    current_robot_history = new_robot_message_outputs[i-1]
                    if current_robot_history:
                        last_msg = current_robot_history[0]
                        current_core_state = new_message_data.get('core_state', 'unknown')
                        last_core_state = last_msg.get('core_state', 'unknown')
                        current_features = set(new_message_data.get('feature_set', []))
                        last_features = set(last_msg.get('feature_set', []))
                        current_pkgs = new_message_data.get('pkg_count', 0)
                        last_pkgs = last_msg.get('pkg_count', 0)
                        
                        if current_core_state == 'complete' and last_core_state == 'complete':
                            should_send = False

                        if framework_mode == 'with_framework' and should_send:
                            if current_core_state == last_core_state:
                                if current_features == last_features:
                                    should_send = False
                            if current_core_state == 'deviation' and last_core_state == 'deviation':
                                if current_features == last_features:
                                    should_send = False
                            if current_pkgs != last_pkgs:
                                should_send = True
                            if current_features != last_features:
                                should_send = True

                if should_send:
                    msg_id = new_message_data['message_id'] 
                    if msg_id not in new_message_timestamps:
                        appear_time = time.time()
                        new_message_timestamps[msg_id] = appear_time
                        
                        log_entry = create_message_log_entry(
                            message_id=msg_id, robot_id=robot_id, scenario_num=scenario_num, condition_idx=condition_idx,
                            frame_idx=frame_idx, sim_time=sim_time, message_type=message_type, message_text=message_text_for_log, 
                            participant_id=participant_data.get('id'), appear_time=appear_time,
                            robot_state=robot_info.get('state'), robot_x=robot_info.get('x'), robot_y=robot_info.get('y')
                        )
                        # WRITE TO DISK IMMEDIATELY
                        write_log_to_disk(log_entry)
                    
                    new_messages_data_list.append(new_message_data)
                    updated_history = [new_message_data] + (new_robot_message_outputs[i-1] or [])
                    new_robot_message_outputs[i-1] = updated_history

    # --- Package Assignment/Discovery Logic ---
    if frame_idx > 0 and framework_mode == 'with_framework':
        current_packages = current_frame_data.get('packages', [])
        prev_packages_list = scenario_data[frame_idx - 1].get('packages', [])
        prev_packages_dict = {p['id']: p for p in prev_packages_list}

        for pkg in current_packages:
            current_assigned = pkg.get('Assigned_to')
            prev_assigned = prev_packages_dict.get(pkg['id'], {}).get('Assigned_to')
            if (prev_assigned in ['Null', None] or prev_assigned == '') and current_assigned.startswith('robot') and pkg.get('carried_by') in ['Null', None]:
                pkg_id = pkg['id']
                assigned_to = current_assigned
                message_text_list = ["Package ", html.Strong(pkg_id), f" has been assigned to ", html.Strong(assigned_to), " for collection."]
                message_text_for_log = " ".join([str(item) for item in message_text_list])
                msg_id = f"{pkg_id}-assigned-{sim_time:.2f}"
                message_type = "assignment"
                new_message_data = {
                    'message_id': msg_id, 'robot_id_title': "System", 'status_icon': '🔗', 'status_text': 'PACKAGE ASSIGNED',
                    'status_class_suffix': 'on-track', 'time_str': datetime.now().strftime('%I:%M:%S %p'), 'details_msg': message_text_list
                }
                if msg_id not in new_message_timestamps:
                    appear_time = time.time()
                    new_message_timestamps[msg_id] = appear_time
                    log_entry = create_message_log_entry(
                        message_id=msg_id, robot_id="System", scenario_num=scenario_num, condition_idx=condition_idx,
                        frame_idx=frame_idx, sim_time=sim_time, message_type=message_type, message_text=message_text_for_log,
                        participant_id=participant_data.get('id'), appear_time=appear_time, robot_state="N/A", robot_x=pkg.get('x'), robot_y=pkg.get('y')
                    )
                    # WRITE TO DISK IMMEDIATELY
                    write_log_to_disk(log_entry)
                    
                    new_messages_data_list.insert(0, new_message_data)
                    robot_index = int(assigned_to[-1]) - 1
                    if 0 <= robot_index < 3:
                        new_robot_message_outputs[robot_index].insert(0, new_message_data)

        for pkg in current_packages:
            if pkg['id'].startswith('d'):
                prev_pkg = prev_packages_dict.get(pkg['id'])
                current_discovered = pkg.get('Discovered', 0) == 1
                prev_discovered = prev_pkg.get('Discovered', 0) == 1 if prev_pkg else False
                if current_discovered and not prev_discovered:
                    pkg_id = pkg['id']
                    discovered_by = pkg.get('Discovered_by', 'N/A')
                    assigned_to = pkg.get('Assigned_to', 'N/A')
                    if discovered_by in ['Null', 'N/A', '', None]: continue 
                    message_text_list = []
                    if discovered_by != 'N/A' and discovered_by == assigned_to:
                         message_text_list = ["Package ", html.Strong(pkg_id), f" discovered by {discovered_by} and it is en route to collect it."]
                    elif discovered_by != assigned_to and assigned_to != 'N/A':
                        message_text_list = ["Package ", html.Strong(pkg_id), f" discovered by {discovered_by}.", f" Assigned to {assigned_to}."]
                    else:
                        message_text_list = ["Package ", html.Strong(pkg_id), f" discovered by {discovered_by}."]
                    message_text_for_log = " ".join([str(item) for item in message_text_list])
                    msg_id = f"{pkg_id}-discovered-{sim_time:.2f}"
                    message_type = "discovery"
                    new_message_data = {
                        'message_id': msg_id, 'robot_id_title': "System", 'status_icon': '📣', 'status_text': 'PACKAGE DISCOVERED',
                        'status_class_suffix': 'on-track', 'time_str': datetime.now().strftime('%I:%M:%S %p'), 'details_msg': message_text_list
                    }
                    if msg_id not in new_message_timestamps:
                        appear_time = time.time()
                        new_message_timestamps[msg_id] = appear_time
                        log_entry = create_message_log_entry(
                            message_id=msg_id, robot_id="System", scenario_num=scenario_num, condition_idx=condition_idx, 
                            frame_idx=frame_idx, sim_time=sim_time, message_type=message_type, message_text=message_text_for_log, 
                            participant_id=participant_data.get('id'), appear_time=appear_time, robot_state="N/A", robot_x=pkg.get('x'), robot_y=pkg.get('y')
                        )
                        # WRITE TO DISK IMMEDIATELY
                        write_log_to_disk(log_entry)
                        
                        new_messages_data_list.insert(0, new_message_data)
                        if discovered_by.startswith('robot'):
                            robot_index = int(discovered_by[-1]) - 1
                            if 0 <= robot_index < 3:
                                new_robot_message_outputs[robot_index].insert(0, new_message_data)

    # --- 5. Render & Return ---
    updated_all_messages_data = new_messages_data_list + current_all_messages_data
    updated_all_messages_data = updated_all_messages_data[:100] 
    
    feed_children = [
        render_message_component(
            msg_data, 
            current_open_message_ids, 
            is_new=(msg_data in new_messages_data_list)
        ) 
        for msg_data in updated_all_messages_data
    ]
    
    new_interval = SLOW_INTERVAL_MS if any_sync_occurred_with_framework else UPDATE_INTERVAL_MS
    
    # Return `no_update` for the all-message-logs-store (last element) to prevent lag
    return (fig, new_robot_message_outputs[0], new_robot_message_outputs[1], new_robot_message_outputs[2],
            frame_idx, frame_idx, frame_idx, current_hmms, feed_children, updated_all_messages_data,
            new_interval, current_open_message_ids, new_message_timestamps, no_update)
    
    



# @app.callback(
#     Output('simulation-graph', 'figure'),
#     Output('robot-1-messages-store', 'data', allow_duplicate=True),
#     Output('robot-2-messages-store', 'data', allow_duplicate=True),
#     Output('robot-3-messages-store', 'data', allow_duplicate=True),
#     Output('robot-1-timeline', 'value'),
#     Output('robot-2-timeline', 'value'),
#     Output('robot-3-timeline', 'value'),
#     Output('hmm-data-store', 'data', allow_duplicate=True),
#     Output('all-messages-feed', 'children'),
#     Output('all-messages-store', 'data', allow_duplicate=True),
#     Output('animation-interval', 'interval'),
#     Output('open-messages-store', 'data', allow_duplicate=True),
#     Output('message-timestamps-store', 'data', allow_duplicate=True),
#     Output('all-message-logs-store', 'data', allow_duplicate=True),
#     Input('current-frame-store', 'data'),
#     Input('study-state-store', 'data'),
#     State('scenario-data-store', 'data'),
#     State('hmm-data-store', 'data'),
#     State('participant-store', 'data'),
#     [State(f'robot-{i}-messages-store', 'data') for i in range(1, 4)],
#     State('open-messages-store', 'data'),
#     State('all-messages-store', 'data'),
#     State('message-timestamps-store', 'data'),
#     State('all-message-logs-store', 'data'),
#     prevent_initial_call=True
# )
# def update_simulation_views(frame_idx, study_state,
#                             scenario_data, hmm_data,
#                             participant_data, hist1, hist2, hist3,
#                             open_message_ids, all_messages_history,
#                             message_timestamps, all_message_logs):
#     if not study_state or study_state.get('phase') != 'simulation':
#         return (no_update,) * 14
    
#     current_open_message_ids = list(set(open_message_ids)) if open_message_ids else []
#     new_message_timestamps = message_timestamps.copy() if message_timestamps else {}
#     new_all_message_logs = all_message_logs.copy() if all_message_logs else []
    
#     current_run_idx = study_state['current_run_idx']
#     current_run_info = participant_data['track'][current_run_idx]
#     scenario_num = current_run_info[0]
#     condition_idx = current_run_info[1]
#     view_type, framework_mode = get_condition_names(condition_idx)
    
#     if not all([scenario_data, hmm_data, study_state, participant_data]):
#         return (no_update,) * 14
    
#     if frame_idx is None or frame_idx >= len(scenario_data):
#         current_fig = initial_figure
#         try: current_fig = callback_context.outputs_list[0].get('value', initial_figure)
#         except: pass
#         return (current_fig, hist1 or [], hist2 or [], hist3 or [], frame_idx or 0, frame_idx or 0, frame_idx or 0,
#                 hmm_data, all_messages_history or [], all_messages_history or [], UPDATE_INTERVAL_MS,
#                 current_open_message_ids, new_message_timestamps, new_all_message_logs)
    
#     current_hmms = hmm_data.copy() if hmm_data else {}
#     current_frame_data = scenario_data[frame_idx]
#     fig = create_figure_for_frame(static_map_data, current_frame_data)
    
#     mission_time_threshold = THRESHOLD_VALUES['with_framework'].get(scenario_num, 1)
#     robots_dict = current_frame_data.get('robots', {})
#     packages = current_frame_data.get('packages', [])
    
#     histories = [hist1, hist2, hist3]
#     new_robot_message_outputs = [histories[0] or [], histories[1] or [], histories[2] or []]
#     sim_time = current_frame_data.get('simulator time', 0)
#     any_sync_occurred_with_framework = False
#     newly_generated_messages_for_feed = []
    
#     for i in range(1, 4):
#         robot_id = f'robot{i}'
#         if robot_id in robots_dict:
#             raw_robot_data = robots_dict[robot_id]
#             rmm_keys_to_select = ["state", "plan_index", "x", "y", "mission_time", "Current_weather", "Battery_status", 
#                                   "Momentarily_offline", "Replan_flag", "target_package_id", "plan", 
#                                   "immediate_goal_x", "immediate_goal_y", "Quadrant", "Bad_Terrain"]
#             selected_robot_rmm_array = {'id': robot_id}
#             for key in rmm_keys_to_select:
#                 selected_robot_rmm_array[key] = raw_robot_data.get(key)
#             selected_robot_rmm_array['robot_time'] = sim_time
            
#             selected_robot_hmm_array = current_hmms.get(robot_id)
#             robot_info = {**robots_dict[robot_id], 'id': robot_id}
            
#             sync_occurred = False 
#             generate_message = False 
            
#             # 1. Update HMM Logic
#             if framework_mode == 'with_framework':
#                 if selected_robot_hmm_array:
#                     try:
#                         updated_hmm_array, sync_occurred = dynamic_deviation_threshold_multi_logic(
#                             hmm_array=selected_robot_hmm_array,
#                             rmm_array=selected_robot_rmm_array,
#                             update_logic_functions={},
#                             uncertainty_factor_pos=0.1,
#                             uncertainty_factor_time=0.1,
#                             dynamic_threshold_mission_time=mission_time_threshold,
#                             robot_id=robot_id
#                         )
#                     except Exception:
#                         sync_occurred = False
#                         updated_hmm_array = selected_robot_hmm_array
#                     current_hmms[robot_id] = updated_hmm_array 
#                     if sync_occurred: any_sync_occurred_with_framework = True 
#             else: 
#                 interval = WITHOUT_FRAMEWORK_INTERVALS.get(scenario_num, 20) 
#                 if frame_idx > 0 and frame_idx % interval == 0:
#                     generate_message = True

# # Force Message if Task Complete (ONLY applies to framework mode now)
#             if framework_mode == 'with_framework' and robot_info.get('state') == 'all_tasks_complete':
#                 generate_message = True

#             # 2. Message Generation Attempt
#             if sync_occurred or generate_message:
#                 new_message_data, message_type, message_text_for_log = create_rich_status_message_data(
#                     robot_info, sim_time, packages, selected_robot_hmm_array, selected_robot_rmm_array, scenario_num, framework_mode
#                 )
                
#                 # --- SMART SUPPRESSION LOGIC ---
#                 should_send = True
#                 if new_message_data is None:
#                     should_send = False
#                 else:
#                     current_robot_history = new_robot_message_outputs[i-1]
                    
#                     if current_robot_history:
#                         last_msg = current_robot_history[0]
                        
#                         current_core_state = new_message_data.get('core_state', 'unknown')
#                         last_core_state = last_msg.get('core_state', 'unknown')
                        
#                         # Compare features (e.g. did we add 'Low Battery' to 'Bad Weather'?)
#                         current_features = set(new_message_data.get('feature_set', []))
#                         last_features = set(last_msg.get('feature_set', []))
                        
#                         # Compare package counts
#                         current_pkgs = new_message_data.get('pkg_count', 0)
#                         last_pkgs = last_msg.get('pkg_count', 0)
                        
#                         # --- GLOBAL RULE: Suppress consecutive 'complete' ---
#                         if current_core_state == 'complete' and last_core_state == 'complete':
#                             should_send = False

#                         # --- FRAMEWORK ONLY RULES ---
#                         # We only filter 'On Track' and 'Timing Updates' for the framework condition.
#                         # The 'without_framework' condition MUST remain spammy for the control comparison.
#                         if framework_mode == 'with_framework' and should_send:
                            
#                             # 1. Suppress if identical state (e.g. On Track -> On Track) AND no feature changes
#                             if current_core_state == last_core_state:
#                                 if current_features == last_features:
#                                     should_send = False
                            
#                             # 2. Suppress if we are just sending another Timing Update with no new features
#                             if current_core_state == 'deviation' and last_core_state == 'deviation':
#                                 if current_features == last_features:
#                                     should_send = False
                                    
#                             # 3. OVERRIDE: Always send if Package Count Changed
#                             if current_pkgs != last_pkgs:
#                                 should_send = True
                                
#                             # 4. OVERRIDE: Always send if Features Changed (e.g. Battery added)
#                             if current_features != last_features:
#                                 should_send = True

#                 if should_send:
#                     msg_id = new_message_data['message_id'] 
#                     if msg_id not in new_message_timestamps:
#                         appear_time = time.time()
#                         new_message_timestamps[msg_id] = appear_time
                        
#                         log_entry = create_message_log_entry(
#                             message_id=msg_id, robot_id=robot_id, scenario_num=scenario_num, condition_idx=condition_idx,
#                             frame_idx=frame_idx, sim_time=sim_time, message_type=message_type, message_text=message_text_for_log, 
#                             participant_id=participant_data.get('id'), appear_time=appear_time,
#                             robot_state=robot_info.get('state'), robot_x=robot_info.get('x'), robot_y=robot_info.get('y')
#                         )
#                         new_all_message_logs.append(log_entry)
                    
#                     new_message_div = render_message_component(new_message_data, current_open_message_ids, is_new=True)
#                     newly_generated_messages_for_feed.append(new_message_div)
                    
#                     updated_history = [new_message_data] + (new_robot_message_outputs[i-1] or [])
#                     new_robot_message_outputs[i-1] = updated_history

# # STRICT FIX: Only check for package events if we are in the framework condition.
#     # If without_framework, these instant alerts are suppressed.
#     if frame_idx > 0 and framework_mode == 'with_framework':
#         current_packages = current_frame_data.get('packages', [])
#         prev_packages_list = scenario_data[frame_idx - 1].get('packages', [])
#         # ... (keep the indentation of the code below this line exactly as it was)
#     # if frame_idx > 0:
#     #     current_packages = current_frame_data.get('packages', [])
#     #     prev_packages_list = scenario_data[frame_idx - 1].get('packages', [])
#         prev_packages_dict = {p['id']: p for p in prev_packages_list}

#         for pkg in current_packages:
#             current_assigned = pkg.get('Assigned_to')
#             prev_assigned = prev_packages_dict.get(pkg['id'], {}).get('Assigned_to')
#             if (prev_assigned in ['Null', None] or prev_assigned == '') and current_assigned.startswith('robot') and pkg.get('carried_by') in ['Null', None]:
#                 pkg_id = pkg['id']
#                 assigned_to = current_assigned
#                 message_text_list = ["Package ", html.Strong(pkg_id), f" has been assigned to ", html.Strong(assigned_to), " for collection."]
#                 message_text_for_log = " ".join([str(item) for item in message_text_list])
#                 msg_id = f"{pkg_id}-assigned-{sim_time:.2f}"
#                 message_type = "assignment"
#                 new_message_data = {
#                     'message_id': msg_id, 'robot_id_title': "System", 'status_icon': '🔗', 'status_text': 'PACKAGE ASSIGNED',
#                     'status_class_suffix': 'on-track', 'time_str': datetime.now().strftime('%I:%M:%S %p'), 'details_msg': message_text_list
#                 }
#                 if msg_id not in new_message_timestamps:
#                     appear_time = time.time()
#                     new_message_timestamps[msg_id] = appear_time
#                     log_entry = create_message_log_entry(
#                         message_id=msg_id, robot_id="System", scenario_num=scenario_num, condition_idx=condition_idx,
#                         frame_idx=frame_idx, sim_time=sim_time, message_type=message_type, message_text=message_text_for_log,
#                         participant_id=participant_data.get('id'), appear_time=appear_time, robot_state="N/A", robot_x=pkg.get('x'), robot_y=pkg.get('y')
#                     )
#                     new_all_message_logs.append(log_entry)
#                     new_message_div = render_message_component(new_message_data, current_open_message_ids, is_new=True)
#                     newly_generated_messages_for_feed.insert(0, new_message_div)
#                     robot_index = int(assigned_to[-1]) - 1
#                     if 0 <= robot_index < 3:
#                         new_robot_message_outputs[robot_index].insert(0, new_message_data)

#         for pkg in current_packages:
#             if pkg['id'].startswith('d'):
#                 prev_pkg = prev_packages_dict.get(pkg['id'])
#                 current_discovered = pkg.get('Discovered', 0) == 1
#                 prev_discovered = prev_pkg.get('Discovered', 0) == 1 if prev_pkg else False
#                 if current_discovered and not prev_discovered:
#                     pkg_id = pkg['id']
#                     discovered_by = pkg.get('Discovered_by', 'N/A')
#                     assigned_to = pkg.get('Assigned_to', 'N/A')
#                     if discovered_by in ['Null', 'N/A', '', None]: continue 
#                     message_text_list = []
#                     if discovered_by != 'N/A' and discovered_by == assigned_to:
#                          message_text_list = ["Package ", html.Strong(pkg_id), f" discovered by {discovered_by} and it is en route to collect it."]
#                     elif discovered_by != assigned_to and assigned_to != 'N/A':
#                         message_text_list = ["Package ", html.Strong(pkg_id), f" discovered by {discovered_by}.", f" Assigned to {assigned_to}."]
#                     else:
#                         message_text_list = ["Package ", html.Strong(pkg_id), f" discovered by {discovered_by}."]
#                     message_text_for_log = " ".join([str(item) for item in message_text_list])
#                     msg_id = f"{pkg_id}-discovered-{sim_time:.2f}"
#                     message_type = "discovery"
#                     new_message_data = {
#                         'message_id': msg_id, 'robot_id_title': "System", 'status_icon': '📣', 'status_text': 'PACKAGE DISCOVERED',
#                         'status_class_suffix': 'on-track', 'time_str': datetime.now().strftime('%I:%M:%S %p'), 'details_msg': message_text_list
#                     }
#                     if msg_id not in new_message_timestamps:
#                         appear_time = time.time()
#                         new_message_timestamps[msg_id] = appear_time
#                         log_entry = create_message_log_entry(
#                             message_id=msg_id, robot_id="System", scenario_num=scenario_num, condition_idx=condition_idx, 
#                             frame_idx=frame_idx, sim_time=sim_time, message_type=message_type, message_text=message_text_for_log, 
#                             participant_id=participant_data.get('id'), appear_time=appear_time, robot_state="N/A", robot_x=pkg.get('x'), robot_y=pkg.get('y')
#                         )
#                         new_all_message_logs.append(log_entry)
#                         new_message_div = render_message_component(new_message_data, current_open_message_ids, is_new=True)
#                         newly_generated_messages_for_feed.insert(0, new_message_div)
#                         if discovered_by.startswith('robot'):
#                             robot_index = int(discovered_by[-1]) - 1
#                             if 0 <= robot_index < 3:
#                                 new_robot_message_outputs[robot_index].insert(0, new_message_data)

#     updated_all_messages = newly_generated_messages_for_feed + (all_messages_history or [])
#     updated_all_messages = updated_all_messages[:100]
#     new_interval = SLOW_INTERVAL_MS if any_sync_occurred_with_framework else UPDATE_INTERVAL_MS
    
#     return (fig, new_robot_message_outputs[0], new_robot_message_outputs[1], new_robot_message_outputs[2],
#             frame_idx, frame_idx, frame_idx, current_hmms, updated_all_messages, updated_all_messages,
#             new_interval, current_open_message_ids, new_message_timestamps, new_all_message_logs)
    
    


@app.callback(

    Output('robot-1-messages', 'children'),

    Input('robot-1-messages-store', 'data'),

    State('open-messages-store', 'data') 

)

def update_robot_1_ui(message_data_list, open_message_ids):

    if not message_data_list: return []

    if open_message_ids is None: open_message_ids = []

    children = [render_message_component(message_data_list[0], open_message_ids, is_new=True)]

    if len(message_data_list) > 1:

        children.append(html.P("--- previous updates ---", className="divider"))

        for msg_data in message_data_list[1:]:

            children.append(render_message_component(msg_data, open_message_ids, is_new=False))

    return children



@app.callback(

    Output('robot-2-messages', 'children'),

    Input('robot-2-messages-store', 'data'),

    State('open-messages-store', 'data')

)

def update_robot_2_ui(message_data_list, open_message_ids):

    if not message_data_list: return []

    if open_message_ids is None: open_message_ids = []

    children = [render_message_component(message_data_list[0], open_message_ids, is_new=True)]

    if len(message_data_list) > 1:

        children.append(html.P("--- previous updates ---", className="divider"))

        for msg_data in message_data_list[1:]:

            children.append(render_message_component(msg_data, open_message_ids, is_new=False))

    return children



@app.callback(

    Output('robot-3-messages', 'children'),

    Input('robot-3-messages-store', 'data'),

    State('open-messages-store', 'data')

)

def update_robot_3_ui(message_data_list, open_message_ids):

    if not message_data_list: return []

    if open_message_ids is None: open_message_ids = []

    children = [render_message_component(message_data_list[0], open_message_ids, is_new=True)]

    if len(message_data_list) > 1:

        children.append(html.P("--- previous updates ---", className="divider"))

        for msg_data in message_data_list[1:]:

            children.append(render_message_component(msg_data, open_message_ids, is_new=False))

    return children





@app.callback(
    Output('simulation-map-snapshot', 'figure'),
    # CHANGED: We trigger this only on study_state changes now
    Input('study-state-store', 'data'),
    # ADDED: We need participant data to know WHICH scenario to load
    State('participant-store', 'data')
)
def update_snapshot(study_state, participant_data): 
    # 1. Safety Checks
    if not study_state or study_state.get('phase') != 'simulation' or not participant_data:
        return no_update
    
    # 2. Retrieve Scenario from Server Cache
    current_run_idx = study_state['current_run_idx']
    scenario_num = participant_data['track'][current_run_idx][0]
    
    # LOAD FROM CACHE
    scenario_data = load_scenario_frames(scenario_num)
    
    if not scenario_data:
        return initial_figure 
    
    # 3. Use the first frame (Frame 0) for the static snapshot
    frame_0_data = scenario_data[0]
    
    # Create the figure using the standard function
    static_fig = create_figure_for_frame(static_map_data, frame_0_data)
    
    # --- MODIFICATIONS FOR STATIC VIEW (Keep your existing styling logic) ---
    new_data = []
    for trace in static_fig.data:
        if hasattr(trace, 'marker') and isinstance(trace.marker.color, str) and '50, 50, 150' in trace.marker.color:
            continue 
        if hasattr(trace, 'name') and trace.name and 'Package' in trace.name:
            trace.mode = 'markers' 
            trace.text = None      
            trace.hoverinfo = 'none' 
        if hasattr(trace, 'marker') and trace.marker is not None:
            current_size = trace.marker.size
            if isinstance(current_size, (list, tuple)):
                trace.marker.size = [s * 0.6 for s in current_size]
            elif isinstance(current_size, (int, float)):
                trace.marker.size = current_size * 0.6
        if hasattr(trace, 'line') and trace.line is not None:
            trace.line.width = (trace.line.width or 1) * 0.5
        new_data.append(trace)
    
    static_fig.data = new_data
    static_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0),
        showlegend=False, 
        title=None,
        font=dict(size=8),
        xaxis=dict(range=[0, GRID_WIDTH], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[0, GRID_HEIGHT], showgrid=False, zeroline=False, showticklabels=False)
    )
    return static_fig




@app.callback(

    Output('interaction-log-store', 'data', allow_duplicate=True),

    Input('simulation-graph', 'clickData'),

    State('interaction-log-store', 'data'),

    State('participant-store', 'data'),

    State('study-state-store', 'data'),

    State('current-frame-store', 'data'),

    prevent_initial_call=True

)

def log_graph_click(clickData, interactions, participant_data, study_state, frame_idx):

    if clickData is None or not all([participant_data, study_state]):

        raise PreventUpdate

    new_interactions = interactions.copy() if interactions is not None else []

    try:

        clicked_point_info = clickData['points'][0]

        details = clicked_point_info.get('hovertext', clicked_point_info.get('text', f"point_index_{clicked_point_info.get('pointIndex')}"))

    except Exception as e:

        details = "graph_click_parse_error"

    current_run_idx = study_state['current_run_idx']

    current_run_info = participant_data['track'][current_run_idx]

    scenario_num = current_run_info[0]

    condition_idx = current_run_info[1]

    interaction_entry = {

        'timestamp_iso': datetime.now().isoformat(),

        'timestamp_unix': time.time(),

        'participant': participant_data.get('id'),

        'scenario': scenario_num,

        'condition': condition_idx,

        'frame': frame_idx,

        'type': 'graph_click',

        'click_details': details

    }

    new_interactions.append(interaction_entry)

    return new_interactions



@app.callback(

    Output('page-content', 'children', allow_duplicate=True),

    Output('responses-store', 'data', allow_duplicate=True),

    Output('study-state-store', 'data', allow_duplicate=True),

    Input('submit-pause-question-btn', 'n_clicks'),

    State('study-state-store', 'data'),

    State('participant-store', 'data'),

    State('responses-store', 'data'),

    State('pause-question-radio', 'value'),

    prevent_initial_call=True

)

def submit_pause_question(n_clicks, study_state, participant_data, responses, answer_value):

    if n_clicks == 0 or not study_state or not participant_data or not answer_value:

        return no_update, no_update, no_update

    

    current_run_idx = study_state['current_run_idx']

    current_run_info = participant_data['track'][current_run_idx]

    scenario_num = current_run_info[0]

    condition_idx = current_run_info[1]

    question_idx = study_state['current_question_idx'] 

    

    try:

        question_text = SCENARIO_CONTENT[scenario_num]['questions'][question_idx]['text']

    except Exception:

        question_text = "N/A"



    response_entry = {

        'timestamp': datetime.now().isoformat(),

        'type': 'pause_question',

        'run_number': current_run_idx + 1,

        'scenario': scenario_num,

        'condition': condition_idx,

        'pause_point': question_idx + 1,

        'question': question_text,

        'answer': answer_value

    }

    new_responses = (responses or []) + [response_entry]

    new_study_state = study_state.copy()

    new_study_state['current_question_idx'] += 1 

    new_study_state['phase'] = 'simulation'

    new_study_state['segment_start_time'] = datetime.now().isoformat() 

    return create_simulation_layout(), new_responses, new_study_state



@app.callback(

    Output('page-content', 'children', allow_duplicate=True),

    Output('responses-store', 'data', allow_duplicate=True),

    Output('study-state-store', 'data', allow_duplicate=True),

    Output('current-frame-store', 'data', allow_duplicate=True), 

    Input('submit-post-scenario-btn', 'n_clicks'),

    State('study-state-store', 'data'),

    State('participant-store', 'data'),

    State('responses-store', 'data'),

    State({'type': 'post-scenario-question', 'id': ALL}, 'value'),

    State({'type': 'post-scenario-question', 'id': ALL}, 'id'),

    State('interaction-log-store', 'data'),

    State('all-message-logs-store', 'data'),

    prevent_initial_call=True

)

def submit_post_scenario_questions(n_clicks, study_state, participant_data, responses, q_values, q_ids, interactions, all_message_logs):

    if n_clicks == 0 or not study_state or not participant_data:

        raise PreventUpdate

    if not all(q_values):

            return no_update, no_update, no_update, no_update

        

    current_run_idx = study_state['current_run_idx']

    current_run_info = participant_data['track'][current_run_idx]

    scenario_num = current_run_info[0]

    condition_idx = current_run_info[1]

    view_type, framework_mode = get_condition_names(condition_idx)

    answer_dict = {q_id['id']: val for q_id, val in zip(q_ids, q_values)}

    

    response_entry = {

        'timestamp': datetime.now().isoformat(),

        'type': 'post_scenario', 

        'segment_start_time': study_state.get('segment_start_time'),

        'run_number': current_run_idx + 1,

        'scenario': scenario_num,

        'condition': condition_idx,

        'view_type': view_type,

        'framework': framework_mode,

        'answers': answer_dict 

    }

    new_responses = (responses or []) + [response_entry]

    try:

        save_study_data(participant_data, new_responses, interactions)

        save_message_logs(participant_data, all_message_logs, study_state)

    except Exception as e:

        print(f"Error during incremental save: {e}")

    

    new_study_state = study_state.copy()

    new_study_state['current_run_idx'] += 1

    new_study_state['current_question_idx'] = 0 

    total_runs = len(participant_data['track'])

    

    if new_study_state['current_run_idx'] < total_runs:

        new_study_state['phase'] = 'briefing'

        next_run_idx = new_study_state['current_run_idx']

        next_run_info = participant_data['track'][next_run_idx]

        next_scenario_num = next_run_info[0]

        next_condition_idx = next_run_info[1]

        next_view_type, next_framework = get_condition_names(next_condition_idx)

        return briefing_screen(next_run_idx + 1, total_runs, next_scenario_num, next_view_type, next_framework), new_responses, new_study_state, 0 

    else:

        new_study_state['phase'] = 'post_study'

        return post_study_questionnaire(), new_responses, new_study_state, 0 





# @app.callback(
#     Output('page-content', 'children', allow_duplicate=True),
#     Input('submit-final-btn', 'n_clicks'),
#     State('participant-store', 'data'),
#     State('study-state-store', 'data'),
#     State('responses-store', 'data'),
#     State('interaction-log-store', 'data'),
#     State('all-message-logs-store', 'data'),
#     State({'type': 'post-study-question', 'id': ALL}, 'value'),
#     State({'type': 'post-study-question', 'id': ALL}, 'id'),
#     prevent_initial_call=True
# )
# def submit_final_questionnaire(n_clicks, participant_data, study_state, responses, interactions, all_message_logs, post_values, post_ids):
#     if not participant_data:
#         raise PreventUpdate
    
#     # Map answers to their IDs
#     answer_dict = {q_id['id']: val for q_id, val in zip(post_ids, post_values)}
    
#     post_response = {
#         'timestamp': datetime.now().isoformat(),
#         'type': 'post_study',
#         'answers': answer_dict
#     }
    
#     final_responses = (responses or []) + [post_response]
    
#     try:
#         # Save all data (interactions, message logs, and the appended responses JSON)
#         save_study_data(participant_data, final_responses, interactions)
#         save_message_logs(participant_data, all_message_logs, study_state)
#     except Exception as e:
#         print(f"Error during final save: {e}")
        
#     return thank_you_screen()


@app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('submit-final-btn', 'n_clicks'),
    Input('skip-final-btn', 'n_clicks'), # Added Skip Input
    State('participant-store', 'data'),
    State('study-state-store', 'data'),
    State('responses-store', 'data'),
    State('interaction-log-store', 'data'),
    State('all-message-logs-store', 'data'),
    State({'type': 'post-study-question', 'id': ALL}, 'value'),
    State({'type': 'post-study-question', 'id': ALL}, 'id'),
    prevent_initial_call=True
)
def submit_final_questionnaire(submit_clicks, skip_clicks, participant_data, study_state, responses, interactions, all_message_logs, post_values, post_ids):
    if not participant_data:
        raise PreventUpdate
    
    # Determine which button triggered the callback
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    answer_dict = {}

    # If they clicked Submit, we gather the answers. 
    # If they clicked Skip, we leave answer_dict empty or mark as skipped.
    if button_id == 'submit-final-btn':
        answer_dict = {q_id['id']: val for q_id, val in zip(post_ids, post_values)}
    else:
        answer_dict = {"status": "skipped_by_user"}
    
    post_response = {
        'timestamp': datetime.now().isoformat(),
        'type': 'post_study',
        'answers': answer_dict
    }
    
    final_responses = (responses or []) + [post_response]
    
    try:
        # Save all data (interactions, message logs, and the appended responses JSON)
        save_study_data(participant_data, final_responses, interactions)
        save_message_logs(participant_data, all_message_logs, study_state)
    except Exception as e:
        print(f"Error during final save: {e}")
        
    return thank_you_screen()


if __name__ == '__main__':
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    with open("assets/style.css", "w") as f:
        f.write("""
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
.robot-column { display: flex; flex-direction: column; gap: 15px; flex: 1; height: 100%; }
.robot-card-top { background-color: #ffffff; border: 1px solid #dee2e6; border-radius: 0.5rem; padding: 10px 20px; width: 90%; margin-left: auto; margin-right: auto; flex-shrink: 0; }
.robot-card-bottom { background-color: #ffffff; border: 1px solid #dee2e6; border-radius: 0.5rem; padding: 15px; display: flex; flex-direction: column; flex-grow: 1; min-height: 0; }
.message-box { height: 100%; overflow-y: auto; padding-right: 10px; flex-grow: 1; }
.message-box-dark-theme { height: 100%; overflow-y: auto; padding-right: 10px; flex-grow: 1; }
.divider { text-align: center; color: #aaa; font-size: 0.9em; margin: 15px 0; }
.divider::before, .divider::after { content: ' ― '; }
.robot-card-top .rc-slider-track { background-color: #007bff !important; height: 12px;}
.robot-card-top .rc-slider-rail { background-color: #e9ecef !important; height: 12px;}
.robot-card-top .rc-slider-mark-text { color: #555; font-weight: bold; }
.robot-card-top .rc-slider-disabled .rc-slider-handle { display: none; }

/* Base style for all message containers */
.message-container-details {
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 13px;
    border: 1px solid #ddd;
    color: #212529;
    background-color: #f8f9fa; /* Default light background */
}

.message-container-details summary {
    cursor: pointer;
    outline: none;
    display: block;
}

.message-container-details summary::-webkit-details-marker {
    display: none;
}

/* Specific background colors via classes */
.message-container-details.replan {
    background-color: #ffdede; /* Red for replan */
    border-color: #ffb0b0;
}

.message-container-details.on-track {
    background-color: #e0f5e1; /* Green for on-track */
    border-color: #b0dcb0;
}

.message-container-details.stationary {
    background-color: #fff9c4; /* Yellow for stationary */
    border-color: #e0dcb0;
}

/* Animation for new messages */
@keyframes flash-border {
    0% { box-shadow: 0 0 10px 3px #00ff88; }
    100% { box-shadow: none; }
}

.message-container-details.new-message {
    animation: flash-border 1.2s ease-out;
}
""")

    # Run the app using app.run instead of app.run_server
    app.run(debug=False, host='0.0.0.0', port=8081)