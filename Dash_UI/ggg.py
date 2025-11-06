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
import time # Import time for interaction timing
from filelock import FileLock # <-- ADDED FOR SEQUENTIAL ASSIGNMENT

# Assuming backend_operations.py exists in the same directory
try:
    from backend_operations import dynamic_deviation_threshold_multi_logic
except ImportError:
    print("FATAL ERROR: backend_operations.py not found.")
    print("Please make sure this file is in the same directory as the app.")
    def dynamic_deviation_threshold_multi_logic(**kwargs):
        print("Warning: Using dummy backend function.")
        hmm_array = kwargs.get('hmm_array', {})
        rmm_array = kwargs.get('rmm_array', {}) # Get RMM too
        # Simple dummy logic: Sync if replan flag is true
        sync_occurred = rmm_array.get('Replan_flag', False)
        # Return the RMM on sync, HMM otherwise, consistent with real logic
        return rmm_array if sync_occurred else hmm_array, sync_occurred
    
    
    

# Assuming backend_operations.py exists in the same directory
try:
    from backend_operations import dynamic_deviation_threshold_multi_logic
except ImportError:
    print("FATAL ERROR: backend_operations.py not found.")
    print("Please make sure this file is in the same directory as the app.")
    def dynamic_deviation_threshold_multi_logic(**kwargs):
        print("Warning: Using dummy backend function.")
        hmm_array = kwargs.get('hmm_array', {})
        rmm_array = kwargs.get('rmm_array', {}) # Get RMM too
        # Simple dummy logic: Sync if replan flag is true
        sync_occurred = rmm_array.get('Replan_flag', False)
        # Return the RMM on sync, HMM otherwise, consistent with real logic
        return rmm_array if sync_occurred else hmm_array, sync_occurred

# --- Constants ---
GRID_WIDTH = 20
GRID_HEIGHT = 20
UPDATE_INTERVAL_MS = 1000
SLOW_INTERVAL_MS = 2000
# --- NEW: Fast interval for click polling ---
CLICK_POLL_INTERVAL_MS = 100 

# --- ADDED CONSTANTS for participant counting ---
PARTICIPANT_COUNT_FILE = 'study_data/participant_count.txt'
PARTICIPANT_COUNT_LOCK = 'study_data/participant_count.lock'
# -----------------------------------------------

THRESHOLD_VALUES = {
    'with_framework': {1: 5, 2: 12, 3: 15, 4: 9, 5: 10, 6: 11},
    'without_framework': {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
}

SCENARIO_CONFIG = {
    1: {'total_time': 332.0, 'total_steps': 236},
    2: {'total_time': 307.0, 'total_steps': 212},
    3: {'total_time': 362.0, 'total_steps': 417},
    4: {'total_time': 358.0, 'total_steps': 373},
    5: {'total_time': 363.0, 'total_steps': 399},
    6: {'total_time': 398.0, 'total_steps': 441}
}

PAUSE_POINTS = {
    1: [10, 160, 220],
    2: [10, 100, 140],
    3: [10, 120, 170],
    4: [10, 100, 150],
    5: [10, 140, 190],
    6: [10, 130, 180]
}

# --- 24-COMBINATION STUDY DESIGN ---
STUDY_DESIGN_TABLE = [
    # C01-C04: Board (E1, E2) using Seq1-Seq4
    [(1, 1), (2, 0), (3, 3), (4, 2)],  # C01: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(1, 0), (2, 3), (3, 2), (4, 1)],  # C02: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(1, 3), (2, 2), (3, 1), (4, 0)],  # C03: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(1, 2), (2, 1), (3, 0), (4, 3)],  # C04: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C05-C08: Board (E1, E3) using Seq1-Seq4
    [(1, 1), (2, 0), (5, 3), (6, 2)],  # C05: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(1, 0), (2, 3), (5, 2), (6, 1)],  # C06: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(1, 3), (2, 2), (5, 1), (6, 0)],  # C07: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(1, 2), (2, 1), (5, 0), (6, 3)],  # C08: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C09-C12: Board (E2, E1) using Seq1-Seq4
    [(3, 1), (4, 0), (1, 3), (2, 2)],  # C09: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(3, 0), (4, 3), (1, 2), (2, 1)],  # C10: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(3, 3), (4, 2), (1, 1), (2, 0)],  # C11: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(3, 2), (4, 1), (1, 0), (2, 3)],  # C12: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C13-C16: Board (E2, E3) using Seq1-Seq4
    [(3, 1), (4, 0), (5, 3), (6, 2)],  # C13: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(3, 0), (4, 3), (5, 2), (6, 1)],  # C14: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(3, 3), (4, 2), (5, 1), (6, 0)],  # C15: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(3, 2), (4, 1), (5, 0), (6, 3)],  # C16: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C17-C20: Board (E3, E1) using Seq1-Seq4
    [(5, 1), (6, 0), (1, 3), (2, 2)],  # C17: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(5, 0), (6, 3), (1, 2), (2, 1)],  # C18: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(5, 3), (6, 2), (1, 1), (2, 0)],  # C19: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(5, 2), (6, 1), (1, 0), (2, 3)],  # C20: Seq4 - Textual+F, Map+N, Map+F, Textual+N
    # C21-C24: Board (E3, E2) using Seq1-Seq4
    [(5, 1), (6, 0), (3, 3), (4, 2)],  # C21: Seq1 - Map+N, Map+F, Textual+N, Textual+F
    [(5, 0), (6, 3), (3, 2), (4, 1)],  # C22: Seq2 - Map+F, Textual+N, Textual+F, Map+N
    [(5, 3), (6, 2), (3, 1), (4, 0)],  # C23: Seq3 - Textual+N, Textual+F, Map+N, Map+F
    [(5, 2), (6, 1), (3, 0), (4, 3)]   # C24: Seq4 - Textual+F, Map+N, Map+F, Textual+N
]


# --- NEW: SCENARIO CONTENT (BRIEFINGS AND QUESTIONS) ---
SCENARIO_CONTENT = {
    1: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the southwest (SW) region. 
Robot 2 is responsible for the northwest (NW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Has more than one package been discovered?",
                "options": ["Yes", "No"]
            },
            {
                "text": "Which quadrant has most packages been discovered?",
                "options": ["SE", "SW", "NE", "NW"]
            },
            {
                "text": "Which containment zone will robot 3 deliver its package to?",
                "options": [
                    "a. Robot 3 will leave the SW quadrant and deliver its package in the NW",
                    "b. Robot 3 will remain in the SW quadrant and deliver its package in the SW",
                    "c. Robot 3 will go to the NE quadrant and deliver its package in the NW",
                    "d. Robot 3 will leave the SW quadrant and deliver its package in the SE"
                ]
            }
        ]
    },
    2: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the southwest (SW) region. 
Robot 2 is responsible for the northwest (NW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Which robot(s) are currently navigating around an obstacle?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "None"]
            },
            {
                "text": "What obstacle is Robot 3 facing?",
                "options": [
                    "Robot 3 is communicating to a different robot",
                    "Robot 3 is stuck in rough terrain",
                    "Robot 3 is recharging",
                    "Robot 3 is encountering bad weather"
                ]
            },
            {
                "text": "Which robot do you expect will finish its task last?",
                "options": ["Robot 1", "Robot 2", "Robot 3"]
            }
        ]
    },
    3: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northwest (NW) region. 
Robot 2 is responsible for the southeast (SE) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "What is the status of Robot 2?",
                "options": ["Replanning due to bad weather", "Replanning due to rough terrain", "Recharging", "On track"]
            },
            {
                "text": "What are the implications of robot 2 being caught in a bad weather system?",
                "options": [
                    "Robot 2 will have to send its assignment to a different robot",
                    "Robot 2’s delivery will not be impacted",
                    "Robot 2 will desert its mission entirely",
                    "Robot 2 will have to replan its route"
                ]
            },
            {
                "text": "Which robot is likely to deliver a package next?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "Robot 2 and 3 simultaneously"]
            }
        ]
    },
    4: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northwest (NW) region. 
Robot 2 is responsible for the southeast (SE) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Which quadrant is Robot 3 in?",
                "options": ["SE", "NE", "NW", "SW"]
            },
            {
                "text": "Why is Robot 3 in the NW quadrant?",
                "options": [
                    "Robot 3 discovered a package in the NE and is delivering it to the NW",
                    "Robot 3 was assigned a package in the NW and is delivering it",
                    "Robot 1 requested Robot 3 to pick-up a package in the NW region",
                    "Robot 2 requested Robot 3 to pick-up a package in the NW region"
                ]
            },
            {
                "text": "Which containment zone will robot 3 end its mission?",
                "options": ["SE", "SW", "NE", "NW"]
            }
        ]
    },
    5: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northeast (NE) region. 
Robot 2 is responsible for the southwest (SW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "What is the status of robot 2?",
                "options": ["Just picked up a package", "Just delivered a package", "Robot 2 is recharging", "Robot 2 is replanning"]
            },
            {
                "text": "Given that robot 2 just delivered a package, what comes next?",
                "options": [
                    "Robot 2 will head towards a different package in the NW quadrant",
                    "Robot 2 will assist Robot 2 in the NW quadrant",
                    "Robot 2 will head towards a different package in the SW quadrant",
                    "Robot 2 will assist Robot 3 in the NE quadrant",
                    "Robot 2 will search the NE and SE quadrants for remaining packages"
                ]
            },
            {
                "text": "Which robot is likely to finish its mission next?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "Robot 1 and 2 simultaneously", "Robot 3 and 2 simultaneously"]
            }
        ]
    },
    6: {
        "briefing": """In this mission, three robots are working together to collect packages distributed throughout the environment and deliver them to two designated drop-off points. 

Robot 1 is responsible for the northeast (NE) region. 
Robot 2 is responsible for the southwest (SW) region. 
Robot 3 acts as a support and exploration unit, assisting with package drop-offs and searching for the unassigned quadrants to locate any remaining packages. 

Robots 1 and 2 begin the mission with knowledge of four package locations within their respective regions. These are represented on the map as a yellow square. Robots will also discover packages along their journey. These are represented by green triangles. Robots will add these packages to their workload or the workload of one another as they are discovered. Robot 3 will adapt to assist where needed.""",
        "questions": [
            {
                "text": "Which robot(s) are currently navigating around an obstacle?",
                "options": ["Robot 1", "Robot 2", "Robot 3", "No robots are encountering an obstacle"]
            },
            {
                "text": "What type of obstacle(s) are robot 2 and robot 3 experiencing?",
                "options": [
                    "Both robots are experiencing poor weather",
                    "Both robots are experiencing rough terrain",
                    "Robot 2 is experiencing poor weather, Robot 3 is experiencing rough terrain",
                    "Robot 2 is experiencing rough terrain, Robot 3 is experiencing poor weather" # Assuming this was the intended non-duplicate
                ]
            },
            {
                "text": "What is robot 3 going to do now that it has cleared both the NE and SE quadrants and dropped off any discovered packages?",
                "options": [
                    "Robot 3 will end its mission",
                    "Robot 3 will assist Robot 2 in the SE",
                    "Robot 3 will assist Robot 1 in the NW",
                    "Robot 3 will recharge"
                ]
            }
        ]
    }
}
# --- END NEW CONTENT ---


# --- ADDED HELPER FUNCTION ---
def get_condition_names(condition_idx):
    """Translates a condition index (0-3) into names."""
    view_type = 'map' if condition_idx < 2 else 'text'
    framework_mode = 'with_framework' if condition_idx % 2 == 0 else 'without_framework'
    return view_type, framework_mode
# -----------------------------

# --- MODIFIED: Message Log Creation Function (Removed close data) ---
def create_message_log_entry(message_id, robot_id, scenario_num, condition_idx, 
                             frame_idx, sim_time, message_type, message_text,
                             participant_id, appear_time, robot_state, robot_x, robot_y):
    """Creates a comprehensive message log entry for ALL messages"""
    return {
        'message_id': message_id,
        'participant_id': participant_id,
        'scenario': scenario_num,
        'condition': condition_idx,
        'run_number': None,  # Will be filled in when saved
        'frame': frame_idx,
        'sim_time': sim_time,
        'robot_id': robot_id,
        'robot_state': robot_state,
        'robot_x': robot_x,
        'robot_y': robot_y,
        'message_type': message_type,
        'message_text': message_text,
        'appear_timestamp_iso': datetime.fromtimestamp(appear_time).isoformat(),
        'appear_timestamp_unix': appear_time, # Internal-only
        'clicked': 0, # This will be a counter
        'click_timestamp_iso': None,
        'click_timestamp_unix': None, # Internal-only
        'time_to_click_seconds': None,
    }

# --- MODIFIED: Message Log Saving Function (Removed close data) ---
def save_message_logs(participant_data, all_message_logs, study_state):
    """Save ALL message logs to CSV - one row per message"""
    os.makedirs('study_data', exist_ok=True)
    participant_id = participant_data['id']
    
    csv_file = f'study_data/{participant_id}_message_logs.csv'
    
    # Fill in the current run number for logs that don't have it
    current_run_idx = study_state.get('current_run_idx', 0)
    for log in all_message_logs:
        if log.get('run_number') is None:
            log['run_number'] = current_run_idx + 1
    
    if all_message_logs:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            # --- MODIFIED fieldnames to remove _unix and close columns ---
            fieldnames = [
                'message_id', 'participant_id', 'scenario', 'condition', 'run_number',
                'frame', 'sim_time', 'robot_id', 'robot_state', 'robot_x', 'robot_y',
                'message_type', 'message_text', 
                'appear_timestamp_iso',
                'clicked', # This is now a counter
                'click_timestamp_iso', 
                'time_to_click_seconds', 
            ]
            # --- END MODIFICATION ---

            # Only include fields that actually exist in the log
            existing_fieldnames = [fn for fn in fieldnames if fn in all_message_logs[0]]
            
            writer = csv.DictWriter(f, fieldnames=existing_fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(all_message_logs)
        print(f"Saved {len(all_message_logs)} message log entries for {participant_id}")

# --- HMM Data Loading ---
try:
    with open('all_scenarios_hmm_data.json', 'r') as f:
        ALL_SCENARIOS_HMM_DATA = json.load(f)
except FileNotFoundError:
    print("FATAL ERROR: 'all_scenarios_hmm_data.json' not found.")
    ALL_SCENARIOS_HMM_DATA = {}

def get_hmms_for_active_scenario(scenario_number):
    scenario_key = f'scenario_{scenario_number}'
    scenario_data = ALL_SCENARIOS_HMM_DATA.get(scenario_key, {})
    return scenario_data.get('HMM_Robot_1'), scenario_data.get('HMM_Robot_2'), scenario_data.get('HMM_Robot_3')

# --- Data Loading ---
def load_static_data(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Will use data from frame files.")
        return {"walls": [], "zones": [], "nodes": [], "edges": []}

def load_scenario_frames(scenario_id):
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
    print(f"Loaded {len(frames)} frames for scenario_{scenario_id}")
    return frames

def generate_participant_id(name):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    name_hash = hashlib.md5(name.encode()).hexdigest()[:6]
    return f"P{timestamp}_{name_hash}"

# --- MODIFIED: save_study_data ---
def save_study_data(participant_data, responses, interactions):
    """
    Saves responses to JSON and master CSVs.
    - Pause questions are saved to the JSON.
    - Post-scenario 6 questions are saved to master_post_scenario_responses.csv.
    - Final post-study questions are saved to the JSON.
    - Interactions are saved to a separate JSON.
    """
    os.makedirs('study_data', exist_ok=True)
    participant_id = participant_data['id']
    
    # Save all responses (pause, post-scenario, post-study) to one JSON file
    with open(f'study_data/{participant_id}_responses.json', 'w') as f:
        json.dump(responses, f, indent=2)
        
    # Save interactions log
    with open(f'study_data/{participant_id}_interactions.json', 'w') as f:
        json.dump(interactions if interactions is not None else [], f, indent=2)
    
    # --- NEW CSV logic for POST-SCENARIO questions ---
    csv_file = 'study_data/master_post_scenario_responses.csv'
    file_exists = os.path.isfile(csv_file)
    
    post_scenario_responses = [r for r in responses if r.get('type') == 'post_scenario']
    
    if not post_scenario_responses:
        print("No post-scenario responses to save to CSV yet.")
        return # Don't try to write an empty CSV

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
            
        # Get the *last* post-scenario response to write
        # (This function is called incrementally, so we just write the newest one)
        resp = post_scenario_responses[-1]
        q_answers = resp.get('answers', {})
        
        writer.writerow([
            participant_id,
            participant_data['name'],
            participant_data['start_time'],
            resp.get('run_number'),
            resp.get('scenario'),
            resp.get('condition'),
            resp.get('view_type'),
            resp.get('framework'),
            resp.get('timestamp'),
            q_answers.get('mental_demand'),
            q_answers.get('physical_demand'),
            q_answers.get('temporal_demand'),
            q_answers.get('performance'),
            q_answers.get('effort'),
            q_answers.get('frustration'),
        ])
    print(f"Saved post-scenario response for run {resp.get('run_number')} to CSV.")
# --- END MODIFICATION ---


# --- Figure and Component Creation ---
# --- vvv MODIFICATIONS BELOW vvv ---
def create_figure_for_frame(static_data, frame_data):
    fig = go.Figure()

    # Annotations for quadrants
    fig.update_layout(
        xaxis=dict(range=[0, GRID_WIDTH], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False, dtick=10),
        yaxis=dict(range=[0, GRID_HEIGHT], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False),
        plot_bgcolor='#ffffff', paper_bgcolor='#ffffff', font=dict(color='black'),
        showlegend=False, margin=dict(l=0, r=0, t=0, b=0), uirevision='constant',
        annotations=[
            go.layout.Annotation(
                x=2.5, y=17.5, text="NW", showarrow=False,
                font=dict(size=24, color="rgba(0, 0, 0, 0.20)"),
            ),
            go.layout.Annotation(
                x=17.5, y=17.5, text="NE", showarrow=False,
                font=dict(size=24, color="rgba(0, 0, 0, 0.20)"),
            ),
            go.layout.Annotation(
                x=2.5, y=2.5, text="SW", showarrow=False,
                font=dict(size=24, color="rgba(0, 0, 0, 0.20)"),
            ),
            go.layout.Annotation(
                x=17.5, y=2.5, text="SE", showarrow=False,
                font=dict(size=24, color="rgba(0, 0, 0, 0.20)"),
            )
        ]
    )

    walls_data = frame_data.get('walls', []) if frame_data else static_data.get('walls', [])
    zones_data = frame_data.get('zones', []) if frame_data else static_data.get('zones', [])
    nodes_data = frame_data.get('nodes', []) if frame_data else static_data.get('nodes', [])
    edges_data = frame_data.get('edges', []) if frame_data else static_data.get('edges', [])

    for wall in walls_data:
        wall_coords = sorted(wall.items())
        wall_x = [v for k, v in wall_coords if k.startswith('x')]
        wall_y = [v for k, v in wall_coords if k.startswith('y')]
        fig.add_trace(go.Scatter(x=wall_x, y=wall_y, mode='lines',
                                 line=dict(color='black', width=2), hoverinfo='none'))

    for zone in zones_data:
        color_str = zone.get('color', 'rgba(0,0,0,0)')
        if color_str.startswith('('):
            color_str = f"rgb{color_str}"
        zone_coords = sorted(zone.items())
        zone_x = [v for k, v in zone_coords if k.startswith('x')]
        zone_y = [v for k, v in zone_coords if k.startswith('y')]
        fig.add_trace(go.Scatter(x=zone_x, y=zone_y, fill="toself", fillcolor=color_str,
                                 line=dict(width=0), mode='lines', hoverinfo='none'))

    edge_x, edge_y = [], []
    for edge in edges_data:
        edge_x.extend([edge['x0'], edge['x1'], None])
        edge_y.extend([edge['y0'], edge['y1'], None])

    if nodes_data:
        node_x = [node[0] for node in nodes_data]
        node_y = [node[1] for node in nodes_data]
        fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers',
                                 marker=dict(size=4, color='rgba(50, 50, 150, 0.8)'), hoverinfo='none'))

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
                color_map = {
                    'moving': 'red',
                    'carrying': 'orange',
                    'waiting': 'blue',
                    'all_tasks_complete': 'green'
                }
                traces['colors'].append(color_map.get(r_state, 'grey'))

            fig.add_trace(go.Scatter(x=traces['x'], y=traces['y'], mode='markers+text',
                                     marker=dict(size=40, color=traces['colors'], line=dict(width=2, color='white')),
                                     text=traces['texts'], textposition='middle center',
                                     textfont=dict(color='white', size=12, family="Arial Black"),
                                     hovertext=traces['hovers'], hoverinfo='text'))

        # ===== FIXED PACKAGE RENDERING SECTION =====
        if packages:
            pkg_x = []
            pkg_y = []
            pkg_texts = []
            pkg_hovers = []
            pkg_colors = []
            pkg_symbols = []

            robot_pos = {r['id']: (r['x'], r['y']) for r in robots}

            # Track plotted coordinates to avoid duplicates
            plotted_coords = set()

            for p in packages:
                carried_by_robot = p.get('carried_by')
                is_carried = carried_by_robot is not None and carried_by_robot != "Null"
                is_d_package = p['id'].startswith('d')

                if is_d_package:
                    # 'd' packages default to 0 (undiscovered) if 'Discovered' key is missing
                    is_discovered = p.get('Discovered', 0) == 1
                else:
                    # 'p' packages are ALWAYS treated as discovered
                    is_discovered = True

                # Get position
                if is_carried:
                    px, py = robot_pos.get(carried_by_robot, (p.get('x', 0), p.get('y', 0)))
                else:
                    px, py = p.get('x', 0), p.get('y', 0)

                # Create coordinate key for duplicate checking
                coord_key = (round(px, 2), round(py, 2), is_carried)

                # Skip if this coordinate already has a package plotted
                if coord_key in plotted_coords:
                    continue

                plotted_coords.add(coord_key)

                pkg_x.append(px)
                pkg_y.append(py)
                pkg_texts.append(p['id'][-1])

                # Determine color and shape based on state
                if is_carried:
                    pkg_colors.append('gold')
                    pkg_symbols.append('square')
                    pkg_hovers.append(f"Package {p['id']}, Carried by {carried_by_robot}")
                elif is_d_package:
                    if is_discovered:
                        # 'd' package that is now discovered
                        pkg_colors.append('gold')  # yellow
                        pkg_symbols.append('triangle-up')  # triangle
                        pkg_hovers.append(f"Package {p['id']}, On Ground (Discovered 'd' package)")
                    else:
                        # 'd' package that is still undiscovered
                        pkg_colors.append('lightgreen')  # green
                        pkg_symbols.append('triangle-up')  # triangle
                        pkg_hovers.append(f"Package {p['id']}, On Ground (Undiscovered 'd' package)")
                else:  # 'p' package (always discovered)
                    pkg_colors.append('gold')
                    pkg_symbols.append('square')
                    pkg_hovers.append(f"Package {p['id']}, On Ground (Pre-known 'p' package)")

            fig.add_trace(go.Scatter(
                x=pkg_x,
                y=pkg_y,
                mode='markers+text',
                marker=dict(
                    size=20,
                    color=pkg_colors,
                    symbol=pkg_symbols,
                    line=dict(width=1, color='black')
                ),
                text=pkg_texts,
                textposition='middle center',
                textfont=dict(color='black', size=10, family="Arial Black"),
                hovertext=pkg_hovers,
                hoverinfo='text'
            ))

    return fig

def create_rich_status_message_data(robot_data, sim_time, all_packages, selected_robot_hmm_array, selected_robot_rmm_array, scenario_id):
    time_str = datetime.now().strftime('%I:%M:%S %p')
    robot_id = robot_data.get('id', 'N/A')
    x, y = float(robot_data.get('x', 0)), float(robot_data.get('y', 0))
    state = robot_data.get('state')
    message_id = f"{robot_id}-{sim_time:.2f}"

    status_map = {
        'replan': {'text': 'REPLANNING', 'color': '#ffdede', 'icon': '🔄', 'class_suffix': 'replan'},
        'on_track': {'text': 'ON TRACK', 'color': '#e0f5e1', 'icon': '✅', 'class_suffix': 'on-track'},
        'stationary': {'text': 'STATIONARY', 'color': '#fff9c4', 'icon': '⏸️', 'class_suffix': 'stationary'}
    }

    plan_index = selected_robot_rmm_array.get('plan_index', 0)
    scenario_config = SCENARIO_CONFIG.get(scenario_id, {'total_time': 300.0, 'total_steps': 100})
    total_expected_time = scenario_config['total_time']
    total_steps = scenario_config['total_steps']
    time_per_step = total_expected_time / total_steps if total_steps > 0 else 0
    time_difference = (plan_index * time_per_step) - sim_time if plan_index > 0 else 0

    time_status_text = ""
    if abs(time_difference) > 0.1:
        time_status_text = f"Robot is {int(abs(time_difference))} seconds {'ahead' if time_difference > 0 else 'behind'} of schedule."

    feature_alerts = []
    hmm_weather = int(selected_robot_hmm_array.get('Current_weather', 1)) if selected_robot_hmm_array else 1
    rmm_weather = int(selected_robot_rmm_array.get('Current_weather', 1))
    if hmm_weather != rmm_weather:
        feature_alerts.append("Weather has turned bad." if rmm_weather == 0 else "Weather has improved.")

    hmm_battery = int(selected_robot_hmm_array.get('Battery_status', 1)) if selected_robot_hmm_array else 1
    rmm_battery = int(selected_robot_rmm_array.get('Battery_status', 1))
    if hmm_battery != rmm_battery:
        if rmm_battery == 0: feature_alerts.append("Battery is low (<40%).")
        elif rmm_battery == 2: feature_alerts.append("Battery is dead.")
        elif rmm_battery == 1: feature_alerts.append("Battery is good (>40%).")

    hmm_offline = int(selected_robot_hmm_array.get('Momentarily_offline', 0)) if selected_robot_hmm_array else 0
    rmm_offline = int(selected_robot_rmm_array.get('Momentarily_offline', 0))
    if hmm_offline != rmm_offline:
        feature_alerts.append("Robot is momentarily offline." if rmm_offline == 1 else "Robot is back online.")

    feature_text = " ".join(feature_alerts)

    status_key = 'stationary'
    details_msg = ""

    time_and_features = []
    if time_status_text: time_and_features.append(time_status_text)
    if feature_text: time_and_features.append(feature_text)
    combined_info = " ".join(time_and_features).strip()

    if robot_data.get('replan_flag') == True:
        status_key = 'replan'
        pkg_id_text = ""
        if state == 'carrying':
            pkg_id = next((p['id'] for p in all_packages if p.get('carried_by') == robot_id), "N/A")
            pkg_id_text = f" Carrying {pkg_id}."
        details_msg = f"Route recalculated.{pkg_id_text} Current Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()
    elif state == 'carrying':
        status_key = 'on_track'
        pkg_id = next((p['id'] for p in all_packages if p.get('carried_by') == robot_id), "N/A")
        plan = robot_data.get('plan', [])
        dest_x, dest_y = (plan[-1][0], plan[-1][1]) if plan else (x, y)
        details_msg = f"Transporting {pkg_id} to Position (X{dest_x:.0f}, Y{dest_y:.0f}). Currently at Position (X{x:.0f}, Y{y:.0f}). {feature_text}".strip()
    elif state == 'moving':
        status_key = 'on_track'
        pkg_id = robot_data.get('target_package_id', "package")
        goal_x, goal_y = robot_data.get('immediate_goal_x', x), robot_data.get('immediate_goal_y', y)
        details_msg = f"Moving to acquire {pkg_id} at Position (X{goal_x:.0f}, Y{goal_y:.0f}). {feature_text}".strip()
    elif state == 'waiting':
        status_key = 'stationary'
        details_msg = f"Robot is awaiting task at Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()
    # --- MODIFICATION: Handle 'all_tasks_complete' state text ---
    elif state == 'all_tasks_complete':
        status_key = 'on_track' # Use 'on_track' style (green)
        details_msg = f"All tasks complete. Robot is at Position (X{x:.0f}, Y{y:.0f}). {feature_text}".strip()
    # --- END MODIFICATION ---
    else:
        status_key = 'stationary'
        details_msg = f"Robot in unknown state '{state}' at Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()

    status_info = status_map[status_key]
    
    # --- MODIFICATION: Handle 'all_tasks_complete' icon/text ---
    final_status_text = status_info['text']
    final_status_icon = status_info['icon']
    if state == 'all_tasks_complete':
        final_status_text = 'TASKS COMPLETE'
        final_status_icon = '🎉' # Or '🏁' or '✅'
    # --- END MODIFICATION ---

    # --- RETURN DATA, NOT COMPONENT ---
    return {
        'message_id': message_id,
        'robot_id_title': robot_id.title(),
        'status_icon': final_status_icon, # <-- Use final icon
        'status_text': final_status_text, # <-- Use final text
        'status_class_suffix': status_info['class_suffix'],
        'time_str': time_str,
        'details_msg': details_msg
    }, status_key, details_msg # <-- RETURN LOGGABLE DATA + RENDER DATA
# --- END MODIFICATION ---

# --- NEW: Function to render a message component from data ---
def render_message_component(message_data, open_message_ids, is_new=False):
    """
    Takes a message_data dict and renders the html.Details component.
    Applies 'new-message' class only if is_new is True.
    Sets 'open' state based on open_message_ids.
    """
    message_id = message_data['message_id']
    component_class = f"message-container-details {message_data['status_class_suffix']}"
    if is_new:
        component_class += " new-message"
        
    summary = html.Summary(
        html.Div([
            html.Span(message_data['status_icon'], style={'marginRight': '10px', 'fontSize': '1.5em'}),
            html.Strong(f"{message_data['robot_id_title']}: {message_data['status_text']}")
        ], style={'display': 'flex', 'alignItems': 'center', 'fontSize': '1.2em'})
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
# --- END NEW FUNCTION ---


# --- App Initialization ---
app = dash.Dash(__name__, update_title=None, suppress_callback_exceptions=True)
server = app.server

static_map_data = load_static_data('static_map_data.json')
initial_figure = create_figure_for_frame(static_map_data, None)

# --- Study Screen Layouts ---
# welcome_screen is UNCHANGED
def welcome_screen():
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                          'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',
                          'justifyContent': 'center', 'fontFamily': 'Arial'}, children=[
        html.H1("Multi-Agent Task Planner User Study", style={'color': '#00ff88', 'marginBottom': '30px'}),
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                       'maxWidth': '500px', 'width': '100%'}, children=[
            html.H3("Welcome!", style={'marginBottom': '20px'}),
            html.P("Thank you for participating in this study. Please enter your full name to begin.",
                  style={'marginBottom': '30px'}),
            dcc.Input(id='participant-name-input', type='text', placeholder='Enter your name',
                     style={'width': '100%', 'padding': '10px', 'marginBottom': '20px',
                           'fontSize': '16px', 'borderRadius': '5px', 'border': '1px solid #444'}),
            html.Button('Start Study', id='start-study-btn', n_clicks=0,
                       style={'width': '100%', 'padding': '15px', 'fontSize': '18px',
                             'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',
                             'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold'}),
            html.Div(id='name-error', style={'color': '#ff4444', 'marginTop': '10px'})
        ])
    ])

# --- MODIFIED: briefing_screen ---
def briefing_screen(run_number, total_runs, scenario_num, view_type, framework_mode):
    view_name = "Simulator View (Map + Log)" if view_type == 'map' else "Textual Overview"
    framework_name = "WITH Communication Framework" if framework_mode == 'with_framework' else "WITHOUT Communication Framework"
    
    # Load scenario-specific briefing
    scenario_briefing = SCENARIO_CONTENT.get(scenario_num, {}).get('briefing', "No briefing text found for this scenario.")
    
    # Combine specific briefing with dynamic run info
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
# --- END MODIFICATION ---

# --- NEW: create_pause_question_screen ---
def create_pause_question_screen(scenario_num, question_idx):
    """
    Generates the layout for a single pause-point question.
    question_idx is 0-based (0, 1, or 2).
    """
    question_num = question_idx + 1
    try:
        question_data = SCENARIO_CONTENT[scenario_num]['questions'][question_idx]
    except Exception:
        question_data = {
            "text": "Error: Could not load question.",
            "options": ["Continue"]
        }
        
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                          'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center',
                          'justifyContent': 'center', 'fontFamily': 'Arial'}, children=[
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                       'maxWidth': '1000px', 'margin': '0 auto', 'width': '90%'}, children=[
            html.H2(f"Scenario {scenario_num} - Question #{question_num}",
                   style={'color': '#00ff88', 'marginBottom': '40px'}),
            html.P(question_data['text'], style={'fontWeight': 'bold', 'marginBottom': '25px', 'fontSize': '18px'}),
            dcc.RadioItems(
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
# --- END NEW FUNCTION ---

# --- NEW: create_post_scenario_questionnaire ---
def create_post_scenario_questionnaire(scenario_num, run_number, total_runs):
    """
    Generates the 6-question NASA-TLX-like questionnaire for the end of a run.
    """
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
# --- END NEW FUNCTION ---


# --- MODIFIED: post_study_questionnaire ---
def post_study_questionnaire():
    questions = [
        {'text': 'How effective were the update messages in helping you understand the robots\' behavior?', 'type': 'scale', 'id': 'effectiveness', 'options': ['1 - Not at all effective', '2', '3', '4', '5 - Extremely effective']},
        {'text': 'How did this differ between demonstration types?', 'type': 'open', 'id': 'effectiveness_detail'},
        {'text': 'How easy was it to tell why a robot replanned or changed its route?', 'type': 'scale', 'id': 'replan_clarity', 'options': ['1 - Very difficult', '2', '3', '4', '5 - Very easy']},
        {'text': 'What, if anything, was confusing about the robots\' behavior or the updates you received? How did this differ between demonstration types?', 'type': 'open', 'id': 'confusion_detail'},
        {'text': 'Do you have any additional thoughts or feedback about the communication styles or the interface overall?', 'type': 'open', 'id': 'final_feedback'}
    ]
    
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                          'padding': '40px', 'fontFamily': 'Arial', 'overflowY': 'auto'}, children=[
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                       'maxWidth': '1000px', 'margin': '0 auto'}, children=[
            html.H2("Final Questionnaire", style={'color': '#00ff88', 'marginBottom': '20px'}),
            html.P("You may end the evaluation here. If you are willing to answer additional questions to assist in our understanding of your experience, please continue forward.",
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
            html.Button('Submit and Complete Study', id='submit-final-btn', n_clicks=0,
                       style={'padding': '15px 40px', 'fontSize': '18px', 'backgroundColor': '#00ff88',
                             'color': '#1e1e1e', 'border': 'none', 'borderRadius': '5px',
                             'cursor': 'pointer', 'fontWeight': 'bold', 'marginTop': '30px'})
        ])
    ])
# --- END MODIFICATION ---

# create_simulation_layout is UNCHANGED
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

# thank_you_screen is UNCHANGED
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
            html.P("You may now close this window.", style={'marginTop': '30px', 'color': '#888'})
        ])
    ])

# --- App Layout (MODIFIED to add message stores & click interval) ---
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=welcome_screen()),
    # Stores
    dcc.Store(id='participant-store', data={}),
    dcc.Store(id='study-state-store', data={}),
    dcc.Store(id='scenario-data-store'),
    dcc.Store(id='current-frame-store', data=0),
    dcc.Store(id='hmm-data-store'),
    dcc.Store(id='open-messages-store', data=[]),
    dcc.Store(id='all-messages-store', data=[]), # For Map UI log
    dcc.Store(id='responses-store', data=[]),
    dcc.Store(id='interaction-log-store', data=[]),
    dcc.Store(id='message-timestamps-store', data={}),
    
    # --- STORES FOR TEXT UI (to fix animation bug) ---
    # --- These will now store DATA (dicts), not COMPONENTS ---
    dcc.Store(id='robot-1-messages-store', data=[]),
    dcc.Store(id='robot-2-messages-store', data=[]),
    dcc.Store(id='robot-3-messages-store', data=[]),
    
    # --- NEW STORE FOR COMPREHENSIVE MESSAGE LOGGING ---
    dcc.Store(id='all-message-logs-store', data=[]),
    
    # Hidden div to capture message clicks
    html.Div(id='message-click-relay', style={'display': 'none'}),
    
    # Intervals
    dcc.Interval(id='animation-interval', interval=UPDATE_INTERVAL_MS, n_intervals=0, disabled=True),
    # --- NEW: Fast interval for reliable click logging ---
    dcc.Interval(id='click-logger-interval', interval=CLICK_POLL_INTERVAL_MS, n_intervals=0, disabled=True) 
])

# --- MODIFIED Clientside callback (to use queue and fast interval) ---
app.clientside_callback(
    """
    function(n_intervals) {
        // --- NEW: Ensure queue exists on window ---
        if (!window.messageClickQueue) {
            window.messageClickQueue = [];
        }
        
        // This function is tricky because Dash recreates the DOM.
        // We need to ensure we only attach one listener per element.
        const detailsElements = document.querySelectorAll('details[id*="status-message"]');
        
        detailsElements.forEach(function(details) {
            if (details.dataset.listenerAttached) {
                return; // Skip if listener is already attached
            }
            details.dataset.listenerAttached = 'true'; // Mark as attached
            
            details.addEventListener('toggle', function(event) {
                // Find the ID, which is a JSON string in the 'id' attribute
                const idAttr = details.getAttribute('id');
                let messageIdStr = '';
                try {
                    // Parse the JSON-like string
                    const idObj = JSON.parse(idAttr.replace(/'/g, '"'));
                    messageIdStr = idObj.id;
                } catch (e) {
                    console.error('Could not parse message ID:', idAttr);
                    // Fallback for simple string IDs (if any)
                    messageIdStr = idAttr;
                }
                
                const isOpen = details.open;
                const clickData = {
                    messageId: messageIdStr, // Use the parsed ID
                    isOpen: isOpen,
                    timestamp: Date.now()
                };
                
                // --- MODIFIED: Push to queue instead of overwriting a single var ---
                window.messageClickQueue.push(JSON.stringify(clickData));
            });
        });
        
        // --- MODIFIED: Return the entire queue and clear it ---
        if (window.messageClickQueue.length > 0) {
            const dataToReturn = JSON.stringify(window.messageClickQueue); // Send the whole queue
            window.messageClickQueue = []; // Clear the queue
            return dataToReturn;
        }
        return null; // Dash will interpret this as no_update
    }
    """,
    Output('message-click-relay', 'children'),
    Input('click-logger-interval', 'n_intervals') # --- MODIFIED: Use fast interval ---
)
# --- END MODIFICATION ---

# --- MODIFIED Server callback (logs ONLY FIRST click AND updates open-messages-store) ---
@app.callback(
    Output('interaction-log-store', 'data', allow_duplicate=True),
    Output('all-message-logs-store', 'data', allow_duplicate=True),
    Output('open-messages-store', 'data', allow_duplicate=True), # <-- ADDED OUTPUT
    Input('message-click-relay', 'children'),
    State('interaction-log-store', 'data'),
    State('all-message-logs-store', 'data'),
    State('open-messages-store', 'data'), # <-- ADDED STATE
    State('participant-store', 'data'),
    State('study-state-store', 'data'),
    State('current-frame-store', 'data'),
    prevent_initial_call=True
)
def log_message_clicks(click_data_json_array, interactions, all_message_logs, 
                             open_message_ids, # <-- ADDED STATE
                             participant_data, study_state, frame_idx):
    
    if not click_data_json_array or not all([participant_data, study_state, all_message_logs]):
        raise PreventUpdate
    
    new_interactions = interactions.copy() if interactions is not None else []
    new_all_message_logs = all_message_logs.copy()
    new_open_message_ids = set(open_message_ids.copy() if open_message_ids is not None else []) # <-- Use a set
    
    try:
        click_data_list = json.loads(click_data_json_array)
        
        for click_data in click_data_list:
            click_info = json.loads(click_data)
            is_open = click_info.get('isOpen', False)
            message_id = click_info.get('messageId', '')
            
            # --- 1. Manage UI open/closed state ---
            if is_open:
                new_open_message_ids.add(message_id) # Add to set if opened
            else:
                new_open_message_ids.discard(message_id) # Remove from set if closed
            # --- END UI LOGIC ---

            # --- 2. Log data ONLY on the first "open" event ---
            if is_open:
                message_found = False
                for entry in new_all_message_logs:
                    if entry['message_id'] == message_id:
                        message_found = True
                        
                        # --- MODIFIED LOGIC ---
                        # Only log if this is the VERY first click (clicked == 0)
                        if entry['clicked'] == 0:
                            
                            click_time_unix = click_info.get('timestamp', time.time() * 1000) / 1000.0
                            click_time_iso = datetime.fromtimestamp(click_time_unix).isoformat()
                            action = "opened"
                            
                            # --- 2a. Update the message log entry (all at once) ---
                            entry['click_timestamp_unix'] = click_time_unix
                            entry['click_timestamp_iso'] = click_time_iso
                            entry['time_to_click_seconds'] = click_time_unix - entry['appear_timestamp_unix']
                            entry['clicked'] = 1 # Set to 1, don't increment
                        
                            # --- 2b. Log to the simple interaction log (ONLY ONCE) ---
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
                        
                        # If entry['clicked'] was already 1, we do nothing.
                        # --- END MODIFIED LOGIC ---
                        break
                
                if not message_found:
                    print(f"Warning: 'Open' click logged for message_id '{message_id}' but not found in all_message_logs_store.")
            
            # --- "close" events (is_open=False) are now handled by the UI set, but not logged ---
        
    except Exception as e:
        print(f"Error logging message click: {e} | Click Data: {click_data_json_array}")
    
    return new_interactions, new_all_message_logs, list(new_open_message_ids) # <-- RETURN LIST
# --- END MODIFICATION ---
# --- Callbacks ---

# start_study is UNCHANGED
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
        return no_update, no_update, no_update, "Please enter your full name."
    
    # --- New Sequential Assignment Logic ---
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
    # --- End New Logic ---
    
    participant_id = generate_participant_id(name)
    
    participant_data = {
        'id': participant_id,
        'name': name,
        'track': assigned_track,
        'start_time': datetime.now().isoformat()
    }
    
    study_state = {
        'current_run_idx': 0,
        'current_question_idx': 0, # This now tracks pause points (0, 1, 2)
        'phase': 'briefing',
        'segment_start_time': None
    }
    
    first_run_info = assigned_track[0]
    scenario_num = first_run_info[0]
    condition_idx = first_run_info[1]
    view_type, framework_mode = get_condition_names(condition_idx)
    total_runs = len(assigned_track)
    
    return briefing_screen(1, total_runs, scenario_num, view_type, framework_mode), participant_data, study_state, ""

# begin_scenario is UNCHANGED
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

# --- MODIFIED: load_data_and_start_simulation (clears text stores) ---
@app.callback(
    Output('scenario-data-store', 'data'),
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
    # --- NEW: Clear Text UI stores on load ---
    Output('robot-1-messages-store', 'data', allow_duplicate=True),
    Output('robot-2-messages-store', 'data', allow_duplicate=True),
    Output('robot-3-messages-store', 'data', allow_duplicate=True),
    Input('simulation-layout-loaded-signal', 'children'),
    State('study-state-store', 'data'),
    State('participant-store', 'data'),
    prevent_initial_call=True
)
def load_data_and_start_simulation(layout_signal, study_state, participant_data):
    if not study_state or not participant_data or study_state.get('phase') != 'simulation':
        raise PreventUpdate
    print("load_data_and_start_simulation firing...")
    
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    
    frames = load_scenario_frames(scenario_num)
    HMM_Robot_1, HMM_Robot_2, HMM_Robot_3 = get_hmms_for_active_scenario(scenario_num)
    hmms = {
        'robot1': HMM_Robot_1,
        'robot2': HMM_Robot_2,
        'robot3': HMM_Robot_3
    }
    
    start_frame = 0
    pause_points = PAUSE_POINTS.get(scenario_num, [100, 200, 300])
    if study_state['current_question_idx'] > 0:
        # This logic resumes from the correct frame *after* a pause
        start_frame = pause_points[study_state['current_question_idx'] - 1] + 1
    
    max_frames = len(frames) - 1 if frames else 0
    mid_point = max_frames // 2
    marks = {0: 'Start', mid_point: 'Midpoint', max_frames: 'End'}
    
    # Clear all message stores for the new run
    return frames, hmms, start_frame, max_frames, max_frames, max_frames, marks, marks, marks, [], [], {}, [], [], []

# --- MODIFIED: control_animation (controls both intervals) ---
@app.callback(
    Output('animation-interval', 'disabled'),
    Output('click-logger-interval', 'disabled'), # --- ADDED ---
    Input('study-state-store', 'data'),
)
def control_animation(study_state):
    if study_state and study_state.get('phase') == 'simulation':
        # print("Enabling intervals") # Too noisy
        return False, False # --- MODIFIED: Enable both ---
    # print("Disabling intervals") # Too noisy
    return True, True # --- MODIFIED: Disable both ---
# --- END MODIFICATION ---

# --- MODIFIED: update_frame_and_check_pause ---
@app.callback(
    Output('current-frame-store', 'data', allow_duplicate=True),
    Output('page-content', 'children', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
    Input('animation-interval', 'n_intervals'),
    State('current-frame-store', 'data'),
    State('scenario-data-store', 'data'),
    State('study-state-store', 'data'),
    State('participant-store', 'data'),
    prevent_initial_call=True
)
def update_frame_and_check_pause(n_intervals, current_frame, scenario_data, study_state, participant_data):
    if not study_state or study_state.get('phase') != 'simulation' or not participant_data or not scenario_data:
        raise PreventUpdate
    
    max_frames = len(scenario_data) - 1
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    total_runs = len(participant_data['track'])
    
    # --- NEW LOGIC: Check for end of simulation FIRST ---
    if current_frame >= max_frames:
        new_state = study_state.copy()
        new_state['phase'] = 'post_scenario_questions' # <-- New phase
        print("Reached end of frames. Moving to Post-Scenario Questionnaire.")
        # Show post-scenario questionnaire
        new_page = create_post_scenario_questionnaire(scenario_num, current_run_idx + 1, total_runs)
        return no_update, new_page, new_state
    # --- END NEW LOGIC ---

    # --- Check for pause points ---
    pause_points = PAUSE_POINTS.get(scenario_num, [100, 200, 300])
    current_question_idx = study_state['current_question_idx']
    
    if current_question_idx < len(pause_points):
        current_pause_point = pause_points[current_question_idx]
        if current_frame == current_pause_point:
            # PAUSE!
            new_study_state = study_state.copy()
            new_study_state['phase'] = 'questions' # Phase is now 'questions'
            print(f"Pausing at frame {current_frame} for question set {current_question_idx + 1}")
            # Show the new pause question screen
            new_page = create_pause_question_screen(scenario_num, current_question_idx)
            return no_update, new_page, new_study_state
    
    # No pause, just advance the frame
    next_frame = current_frame + 1
    return next_frame, no_update, no_update
# --- END MODIFICATION ---

# programmatically_switch_view is UNCHANGED
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
    
    # Only show header if we are in simulation phase
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
    else:  # view_type == 'text'
        map_style['display'] = 'none'
        text_style['display'] = 'flex'
    
    header_text = f"Run: {current_run_idx + 1} / {len(participant_data['track'])} | Scenario: {scenario_num} | View: {view_name} | Framework: {framework_name}"
    return map_style, text_style, header_text

# --- *** MAJOR MODIFICATION: update_simulation_views *** ---
# --- This callback now saves DATA to stores, not components ---
@app.callback(
    Output('simulation-graph', 'figure'),
    # --- MODIFIED: Outputs are to stores, not UI ---
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
    State('scenario-data-store', 'data'),
    State('hmm-data-store', 'data'),
    State('participant-store', 'data'),
    # --- MODIFIED STATE: Use stores for Text UI history DATA ---
    [State(f'robot-{i}-messages-store', 'data') for i in range(1, 4)],
    State('open-messages-store', 'data'),
    State('all-messages-store', 'data'),
    State('message-timestamps-store', 'data'),
    State('all-message-logs-store', 'data'),
    prevent_initial_call=True
)
def update_simulation_views(frame_idx, study_state,
                            scenario_data, hmm_data,
                            participant_data, hist1, hist2, hist3,
                            open_message_ids, all_messages_history,
                            message_timestamps, all_message_logs):
    if not study_state or study_state.get('phase') != 'simulation':
        # --- MODIFIED: Return 14 no_updates ---
        return (no_update,) * 14
    
    # --- Use list(set()) to ensure open_message_ids is a list of uniques ---
    current_open_message_ids = list(set(open_message_ids)) if open_message_ids else []
    new_message_timestamps = message_timestamps.copy() if message_timestamps else {}
    new_all_message_logs = all_message_logs.copy() if all_message_logs else []
    
    # Get current run info
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    condition_idx = current_run_info[1]
    view_type, framework_mode = get_condition_names(condition_idx)
    
    if not all([scenario_data, hmm_data, study_state, participant_data]):
        print("Warning: Missing data in update_simulation_views")
        return (no_update,) * 14
    
    if frame_idx is None or frame_idx >= len(scenario_data):
        current_fig = initial_figure
        try:
            current_fig = callback_context.outputs_list[0].get('value', initial_figure)
        except Exception:
            pass
        return (
            current_fig,
            hist1 or [], hist2 or [], hist3 or [], # Return current store state
            frame_idx if frame_idx is not None else 0,
            frame_idx if frame_idx is not None else 0,
            frame_idx if frame_idx is not None else 0,
            hmm_data,
            all_messages_history or [], all_messages_history or [],
            UPDATE_INTERVAL_MS,
            current_open_message_ids,
            new_message_timestamps,
            new_all_message_logs
        )
    
    current_hmms = hmm_data.copy() if hmm_data else {}
    current_frame_data = scenario_data[frame_idx]
    fig = create_figure_for_frame(static_map_data, current_frame_data)
    
    mission_time_threshold = THRESHOLD_VALUES[framework_mode].get(scenario_num, 1)
    robots_dict = current_frame_data.get('robots', {})
    packages = current_frame_data.get('packages', [])
    
    
    
    # --- MODIFIED: hist1, hist2, hist3 now come from stores (and contain DATA, not components) ---
    histories = [hist1, hist2, hist3]
    # This will hold the new DATA lists for the stores
    new_robot_message_outputs = [histories[0] or [], histories[1] or [], histories[2] or []]
    sim_time = current_frame_data.get('simulator time', 0)
    any_sync_occurred = False
    newly_generated_messages_for_feed = []
    
    for i in range(1, 4):
        robot_id = f'robot{i}'
        if robot_id in robots_dict:
            raw_robot_data = robots_dict[robot_id]
            rmm_keys_to_select = [
                "state", "plan_index", "x", "y", "mission_time",
                "Current_weather", "Battery_status", "Momentarily_offline",
                "Replan_flag", "target_package_id", "plan", "immediate_goal_x", "immediate_goal_y"
            ]
            selected_robot_rmm_array = {'id': robot_id}
            for key in rmm_keys_to_select:
                selected_robot_rmm_array[key] = raw_robot_data.get(key)
            selected_robot_rmm_array['robot_time'] = sim_time
            
            selected_robot_hmm_array = current_hmms.get(robot_id)
            robot_info = {**robots_dict[robot_id], 'id': robot_id}
            
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
                except Exception as e:
                    print(f"Error in backend logic for {robot_id}: {e}")
                    sync_occurred = False
                    updated_hmm_array = selected_robot_hmm_array
                
                current_hmms[robot_id] = updated_hmm_array
                
                if sync_occurred:
                    any_sync_occurred = True
                    
                    # --- MODIFIED: Call new data function ---
                    new_message_data, message_type, message_text = create_rich_status_message_data(
                        robot_info,
                        sim_time,
                        packages,
                        selected_robot_hmm_array,
                        selected_robot_rmm_array,
                        scenario_num
                    )
                    
                    is_new_message = False
                    msg_id = new_message_data['message_id'] # <-- Get ID from data
                    
                    if msg_id not in new_message_timestamps:
                        appear_time = time.time()
                        new_message_timestamps[msg_id] = appear_time
                        is_new_message = True
                        
                        log_entry = create_message_log_entry(
                            message_id=msg_id,
                            robot_id=robot_id,
                            scenario_num=scenario_num,
                            condition_idx=condition_idx,
                            frame_idx=frame_idx,
                            sim_time=sim_time,
                            message_type=message_type,
                            message_text=message_text,
                            participant_id=participant_data.get('id'),
                            appear_time=appear_time,
                            robot_state=robot_info.get('state'),
                            robot_x=robot_info.get('x'),
                            robot_y=robot_info.get('y')
                        )
                        new_all_message_logs.append(log_entry)
                    
                    # --- Create the component for the Map UI (which needs 'new-message') ---
                    new_message_div = render_message_component(
                        new_message_data,
                        current_open_message_ids,
                        is_new=is_new_message # <-- Pass blink status
                    )
                    
                    newly_generated_messages_for_feed.append(new_message_div)
                    
                    # --- MODIFIED: Update the Text UI *store* with *data*, not components ---
                    
                    # 1. Start new history with new *data*
                    updated_history_data = [new_message_data]
                    
                    # 2. Get old history *data* from store
                    current_hist_data = histories[i-1] if isinstance(histories[i-1], list) else ([histories[i-1]] if histories[i-1] else [])
                    
                    # 3. Extend
                    updated_history_data.extend(current_hist_data)
                    
                    # 4. Set output to store
                    new_robot_message_outputs[i-1] = updated_history_data
                    # --- END TEXT UI STORE MODIFICATION ---
    
    updated_all_messages = newly_generated_messages_for_feed + (all_messages_history or [])
    updated_all_messages = updated_all_messages[:100]
    
    new_interval = SLOW_INTERVAL_MS if any_sync_occurred and framework_mode == 'with_framework' else UPDATE_INTERVAL_MS
    
    return (
        fig,
        # --- MODIFIED: Return new *data* history to stores ---
        new_robot_message_outputs[0],
        new_robot_message_outputs[1],
        new_robot_message_outputs[2],
        frame_idx, frame_idx, frame_idx,
        current_hmms,
        updated_all_messages, updated_all_messages,
        new_interval,
        current_open_message_ids, # Pass back the same list
        new_message_timestamps,
        new_all_message_logs
    )
# --- END MODIFICATION ---

# --- *** NEW/MODIFIED: Callbacks to link stores to Text UI *** ---
# --- These callbacks now RENDER components from DATA ---
@app.callback(
    Output('robot-1-messages', 'children'),
    Input('robot-1-messages-store', 'data'),
    State('open-messages-store', 'data') # <-- ADD STATE
)
def update_robot_1_ui(message_data_list, open_message_ids):
    if not message_data_list:
        return []
    if open_message_ids is None:
        open_message_ids = []
        
    children = []
    # Render the first (newest) message with is_new=True
    children.append(render_message_component(message_data_list[0], open_message_ids, is_new=True))
    
    # Render the rest of the messages
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
    if not message_data_list:
        return []
    if open_message_ids is None:
        open_message_ids = []
        
    children = []
    # Render the first (newest) message with is_new=True
    children.append(render_message_component(message_data_list[0], open_message_ids, is_new=True))
    
    # Render the rest of the messages
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
    if not message_data_list:
        return []
    if open_message_ids is None:
        open_message_ids = []
        
    children = []
    # Render the first (newest) message with is_new=True
    children.append(render_message_component(message_data_list[0], open_message_ids, is_new=True))
    
    # Render the rest of the messages
    if len(message_data_list) > 1:
        children.append(html.P("--- previous updates ---", className="divider"))
        for msg_data in message_data_list[1:]:
            children.append(render_message_component(msg_data, open_message_ids, is_new=False))
            
    return children
# --- END NEW/MODIFIED CALLBACKS ---

# update_snapshot is UNCHANGED
@app.callback(
    Output('simulation-map-snapshot', 'figure'),
    Input('simulation-graph', 'figure'),
    Input('study-state-store', 'data')
)
def update_snapshot(main_fig, study_state):
    if not study_state or study_state.get('phase') != 'simulation':
        return no_update
    if main_fig is None:
        return initial_figure
    snapshot_fig = go.Figure(main_fig)
    for trace in snapshot_fig.data:
        if hasattr(trace, 'marker') and trace.marker is not None:
            trace.marker.size = (
                [s * 0.5 for s in trace.marker.size]
                if isinstance(trace.marker.size, (list, tuple))
                else trace.marker.size * 0.5
                if trace.marker.size
                else 5
            )
        if hasattr(trace, 'line') and trace.line is not None:
            trace.line.width = trace.line.width * 0.5 if trace.line.width else 1
    snapshot_fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0),
        showlegend=False,
        title=None,
        font=dict(size=8),
    )
    return snapshot_fig

# log_graph_click is UNCHANGED
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
        print(f"Error parsing clickData: {e}")
        details = "graph_click_parse_error"
    
    # Get context from the current run
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

# --- NEW: submit_pause_question ---
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
        # Don't let them continue without selecting an answer
        return no_update, no_update, no_update
    
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    condition_idx = current_run_info[1]
    question_idx = study_state['current_question_idx'] # 0, 1, or 2
    
    # Get the question text for logging
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
    
    # --- Update state and return to simulation ---
    new_study_state = study_state.copy()
    new_study_state['current_question_idx'] += 1 # Move to next pause point index (e.g., 0 -> 1)
    new_study_state['phase'] = 'simulation'
    new_study_state['segment_start_time'] = datetime.now().isoformat() # Reset segment time
    
    print(f"Logged pause question {question_idx + 1}. Resuming simulation.")
    
    # Return to the simulation layout. The `load_data` callback will
    # use the new 'current_question_idx' to start from the correct frame.
    return create_simulation_layout(), new_responses, new_study_state
# --- END NEW CALLBACK ---


# --- NEW: submit_post_scenario_questions ---
@app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Output('responses-store', 'data', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
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
        
    # Check if all questions are answered
    if not all(q_values):
        print("User tried to submit post-scenario questions without answering all.")
        # We could add an error message here, but for now just prevent update
        return no_update, no_update, no_update

    # Get info for the run we *just finished*
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    condition_idx = current_run_info[1]
    view_type, framework_mode = get_condition_names(condition_idx)
    
    answer_dict = {q_id['id']: val for q_id, val in zip(q_ids, q_values)}
    
    response_entry = {
        'timestamp': datetime.now().isoformat(),
        'type': 'post_scenario', # <-- New type
        'segment_start_time': study_state.get('segment_start_time'),
        'run_number': current_run_idx + 1,
        'scenario': scenario_num,
        'condition': condition_idx,
        'view_type': view_type,
        'framework': framework_mode,
        'answers': answer_dict # Save the whole dict
    }
    
    new_responses = (responses or []) + [response_entry]
    
    try:
        print(f"Incrementally saving data for {participant_data.get('id')} after Run {current_run_idx + 1}.")
        # Save JSON (which has pause Qs) and CSV (which has post-scenario Qs)
        save_study_data(participant_data, new_responses, interactions)
        save_message_logs(participant_data, all_message_logs, study_state)
    except Exception as e:
        print(f"Error during incremental save: {e}")
    
    # --- NOW, advance to the next run or end the study ---
    new_study_state = study_state.copy()
    new_study_state['current_run_idx'] += 1
    new_study_state['current_question_idx'] = 0 # Reset for next run
    total_runs = len(participant_data['track'])
    
    if new_study_state['current_run_idx'] < total_runs:
        # Go to briefing for *next* run
        new_study_state['phase'] = 'briefing'
        next_run_idx = new_study_state['current_run_idx']
        next_run_info = participant_data['track'][next_run_idx]
        next_scenario_num = next_run_info[0]
        next_condition_idx = next_run_info[1]
        next_view_type, next_framework = get_condition_names(next_condition_idx)
        
        print(f"Moving to briefing for Run {next_run_idx + 1}")
        
        return briefing_screen(next_run_idx + 1, total_runs, next_scenario_num, next_view_type, next_framework), new_responses, new_study_state
    else:
        # Finished all runs
        new_study_state['phase'] = 'post_study'
        print("All runs complete. Moving to Post-Study Questionnaire.")
        return post_study_questionnaire(), new_responses, new_study_state
# --- END NEW CALLBACK ---


# --- MODIFIED: submit_final_questionnaire ---
@app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('submit-final-btn', 'n_clicks'),
    State('participant-store', 'data'),
    State('study-state-store', 'data'), # <-- ADDED
    State('responses-store', 'data'),
    State('interaction-log-store', 'data'),
    State('all-message-logs-store', 'data'), # <-- ADDED
    State({'type': 'post-study-question', 'id': ALL}, 'value'),
    State({'type': 'post-study-question', 'id': ALL}, 'id'),
    prevent_initial_call=True
)
def submit_final_questionnaire(n_clicks, participant_data, study_state, responses, interactions, all_message_logs, post_values, post_ids):
    if not participant_data:
        raise PreventUpdate
    
    answer_dict = {q_id['id']: val for q_id, val in zip(post_ids, post_values)}
    post_response = {
        'timestamp': datetime.now().isoformat(),
        'type': 'post_study',
        'answers': answer_dict
    }
    final_responses = (responses or []) + [post_response]
    
    print("Saving final study data...")
    try:
        # Save all data one last time
        # Note: save_study_data will just write the *last* post-scenario response
        # to the CSV, which is fine since it was already written.
        # The main thing is saving the final_responses to the JSON.
        save_study_data(participant_data, final_responses, interactions)
        save_message_logs(participant_data, all_message_logs, study_state)
    except Exception as e:
        print(f"Error during final save: {e}")

    return thank_you_screen()
# --- END MODIFICATION ---

# --- Main Execution ---
if __name__ == '__main__':
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    # --- MODIFIED: Removed all .message-box-dark-theme rules ---
    with open("assets/style.css", "w") as f:
        f.write("""
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
.robot-column { display: flex; flex-direction: column; gap: 15px; flex: 1; height: 100%; }
.robot-card-top {
    background-color: #ffffff;
    border: 1px solid #dee2e6;
    border-radius: 0.5rem;
    padding: 10px 20px;
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    flex-shrink: 0;
}

.robot-card-bottom {
    background-color: #ffffff;
    border: 1px solid #dee2e6;
    border-radius: 0.5rem;
    padding: 15px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    min-height: 0;
}

.message-box {
    height: 100%;
    overflow-y: auto;
    padding-right: 10px;
    flex-grow: 1;
}

/* This class is for the Map View's log */
.message-box-dark-theme {
    height: 100%;
    overflow-y: auto;
    padding-right: 10px;
    flex-grow: 1;
}

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
    # --- END MODIFICATION ---
    
    # Use debug=False for actual study deployment
    app.run(debug=False, host='0.0.0.0', port=9233)