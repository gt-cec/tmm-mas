

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

LATIN_SQUARE = [
    [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
    [2, 3], [2, 4], [2, 5], [2, 6],
    [3, 4], [3, 5], [3, 6],
    [4, 5], [4, 6],
    [5, 6]
]

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

def assign_participant_scenarios(name):
    name_hash = int(hashlib.md5(name.encode()).hexdigest(), 16)
    group_idx = name_hash % len(LATIN_SQUARE)
    assigned_scenarios = LATIN_SQUARE[group_idx]
    return assigned_scenarios

def generate_participant_id(name):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    name_hash = hashlib.md5(name.encode()).hexdigest()[:6]
    return f"P{timestamp}_{name_hash}"

def save_study_data(participant_data, responses, interactions):
    os.makedirs('study_data', exist_ok=True)
    participant_id = participant_data['id']

    with open(f'study_data/{participant_id}_responses.json', 'w') as f:
        json.dump(responses, f, indent=2)

    # <--- MODIFIED: Ensure interactions is a list, not None, when saving
    with open(f'study_data/{participant_id}_interactions.json', 'w') as f:
        json.dump(interactions if interactions is not None else [], f, indent=2)

    csv_file = 'study_data/master_data.csv'
    file_exists = os.path.isfile(csv_file)

    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                'ParticipantID', 'Name', 'ParticipantStartTime', 'Scenario', 'ConditionIndex',
                'ViewType', 'Framework', 'QuestionSet', 'SegmentStartTime', 'ResponseTimestamp',
                'Q1_MentalDemand', 'Q2_PhysicalDemand', 'Q3_TemporalDemand', 'Q4_Performance',
                'Q5_Effort', 'Q6_Frustration', 'Q7_SitAwareness', 'Q8_ReplanCount',
                'Q9_CognitiveLoad', 'Q10_OpenResponse'
            ])

        for resp in responses:
            if resp.get('type') == 'post_study': continue
            q_answers = resp.get('answers', [None]*10)
            writer.writerow([
                participant_id,
                participant_data['name'],
                participant_data['start_time'],
                resp.get('scenario'),
                resp.get('condition'),
                resp.get('view_type'),
                resp.get('framework'),
                resp.get('question_set'),
                resp.get('segment_start_time'),
                resp.get('timestamp'),
                *q_answers
            ])

# --- Figure and Component Creation ---
def create_figure_for_frame(static_data, frame_data):
    fig = go.Figure()
    fig.update_layout(
        xaxis=dict(range=[0, GRID_WIDTH], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False, dtick=10),
        yaxis=dict(range=[0, GRID_HEIGHT], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False),
        plot_bgcolor='#ffffff', paper_bgcolor='#ffffff', font=dict(color='black'),
        showlegend=False, margin=dict(l=0, r=0, t=0, b=0), uirevision='constant'
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




    # edge_x, edge_y = [], []
    # for edge in edges_data:
    #     # Handle both old format (x0, y0, x1, y1) and new format (start_pos, end_pos)
    #     if 'start_pos' in edge and 'end_pos' in edge:
    #         # New format
    #         edge_x.extend([edge['start_pos'][0], edge['end_pos'][0], None])
    #         edge_y.extend([edge['start_pos'][1], edge['end_pos'][1], None])
    #     elif 'x0' in edge:
    #         # Old format (backwards compatibility)
    #         edge_x.extend([edge['x0'], edge['x1'], None])
    #         edge_y.extend([edge['y0'], edge['y1'], None])

        
        
    # if edge_x:
    #     fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines',
    #                             line=dict(width=0.5, color='rgba(50, 50, 50, 0.75)'), hoverinfo='none'))
    
    
    edge_x, edge_y = [], []
    for edge in edges_data:
        edge_x.extend([edge['x0'], edge['x1'], None]); edge_y.extend([edge['y0'], edge['y1'], None])
        
                
            
    
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
                traces['colors'].append({'moving': 'red', 'carrying': 'orange', 'waiting': 'blue'}.get(r['state'], 'grey'))
            fig.add_trace(go.Scatter(x=traces['x'], y=traces['y'], mode='markers+text',
                                     marker=dict(size=30, color=traces['colors'], line=dict(width=2, color='white')),
                                     text=traces['texts'], textposition='middle center',
                                     textfont=dict(color='white', size=12, family="Arial Black"),
                                     hovertext=traces['hovers'], hoverinfo='text'))
            
            
            

        
        if packages:
            
            
            
            
            
            # traces = {'x': [], 'y': [], 'texts': [], 'hovers': []}
            # robot_pos = {r['id']: (r['x'], r['y']) for r in robots}
            # for p in packages:
            #     px, py = robot_pos.get(p.get('carried_by'), (p.get('x', 0), p.get('y', 0)))
            #     traces['x'].append(px); traces['y'].append(py); traces['texts'].append(p['id'][-1])
            #     traces['hovers'].append(f"Package {p['id']}, {'Carried' if p.get('carried_by') else 'On Ground'}")
            # fig.add_trace(go.Scatter(x=traces['x'], y=traces['y'], mode='markers+text', marker=dict(size=20, color='gold', symbol='square', line=dict(width=1, color='black')),
            #                          text=traces['texts'], textposition='middle center', textfont=dict(color='black', size=10, family="Arial Black"),
            #                          hovertext=traces['hovers'], hoverinfo='text'))
            
            
            # --- NEW DYNAMIC PACKAGE DRAWING ---
            pkg_x = []
            pkg_y = []
            pkg_texts = []
            pkg_hovers = []
            pkg_colors = []
            pkg_symbols = []
            
            # Get a dictionary of all current robot positions from the 'robots' list
            robot_pos = {r['id']: (r['x'], r['y']) for r in robots}

            for p in packages:
                carried_by_robot = p.get('carried_by')
                # Default to 1 (discovered) if 'Discovered' key is missing
                is_discovered = p.get('Discovered', 1) == 1 
                # A package is carried if 'carried_by' is not None AND not the string "Null"
                is_carried = carried_by_robot is not None and carried_by_robot != "Null"

                # 1. Get position: 
                # If carried, use the robot's position.
                # If not carried, use the package's own (x, y) coordinates.
                px, py = robot_pos.get(carried_by_robot, (p.get('x', 0), p.get('y', 0)))
                
                # 2. Add to basic lists
                pkg_x.append(px)
                pkg_y.append(py)
                pkg_texts.append(p['id'][-1])
                
                # 3. Determine marker properties and hover text based on state
                if is_carried:
                    # State 1: Carried by a robot
                    pkg_colors.append('gold')
                    pkg_symbols.append('square')
                    pkg_hovers.append(f"Package {p['id']}, Carried by {carried_by_robot}")
                elif is_discovered:
                    # State 2: On the ground and Discovered (Discovered == 1)
                    pkg_colors.append('gold')
                    pkg_symbols.append('square')
                    pkg_hovers.append(f"Package {p['id']}, On Ground (Discovered)")
                else: 
                    # State 3: On the ground and Undiscovered (Discovered == 0)
                    pkg_colors.append('lightgreen')
                    pkg_symbols.append('triangle-up') # This is the Plotly name for a triangle
                    pkg_hovers.append(f"Package {p['id']}, On Ground (Undiscovered)")

            # 4. Create the new trace using these dynamic lists
            fig.add_trace(go.Scatter(
                x=pkg_x, 
                y=pkg_y, 
                mode='markers+text', 
                marker=dict(
                    size=20, 
                    color=pkg_colors,     # Use the list of colors
                    symbol=pkg_symbols,   # Use the list of symbols
                    line=dict(width=1, color='black')
                ),
                text=pkg_texts, 
                textposition='middle center', 
                textfont=dict(color='black', size=10, family="Arial Black"),
                hovertext=pkg_hovers, 
                hoverinfo='text'
            ))
            # --- END OF NEW CODE ---            
            
            
    return fig





# MODIFIED: Refactored to always return html.Details and use generic ID/class
def create_rich_status_message(robot_data, sim_time, all_packages, open_message_ids, selected_robot_hmm_array, selected_robot_rmm_array, scenario_id):
    if open_message_ids is None:
        open_message_ids = []

    time_str = datetime.now().strftime('%I:%M:%S %p')
    robot_id = robot_data.get('id', 'N/A')
    x, y = float(robot_data.get('x', 0)), float(robot_data.get('y', 0))
    state = robot_data.get('state')
    message_id = f"{robot_id}-{sim_time:.2f}" # Use sim_time with decimals for uniqueness

    status_map = {
        'replan': {'text': 'REPLANNING', 'color': '#ffdede', 'icon': '🔄', 'class_suffix': 'replan'},
        'on_track': {'text': 'ON TRACK', 'color': '#e0f5e1', 'icon': '✅', 'class_suffix': 'on-track'},
        'stationary': {'text': 'STATIONARY', 'color': '#fff9c4', 'icon': '⏸️', 'class_suffix': 'stationary'}
    }

    # --- Calculate Time Difference ---
    plan_index = selected_robot_rmm_array.get('plan_index', 0)
    scenario_config = SCENARIO_CONFIG.get(scenario_id, {'total_time': 300.0, 'total_steps': 100})
    total_expected_time = scenario_config['total_time']
    total_steps = scenario_config['total_steps']

    time_per_step = total_expected_time / total_steps if total_steps > 0 else 0
    time_difference = (plan_index * time_per_step) - sim_time if plan_index > 0 else 0

    time_status_text = ""
    if abs(time_difference) > 0.1:
        time_status_text = f"Robot is {int(abs(time_difference))} seconds {'ahead' if time_difference > 0 else 'behind'} of schedule."

    # --- Calculate Feature Alerts ---
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

    # --- Determine Status and Details Text ---
    status_key = 'stationary' # Default
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

    else: # Fallback for unknown states
        status_key = 'stationary' # Treat unknown as stationary
        details_msg = f"Robot in unknown state '{state}' at Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()

    # --- Build Component ---
    status_info = status_map[status_key]
    component_class = f"message-container-details {status_info['class_suffix']}" # Generic class + specific class

    summary = html.Summary(
        html.Div([
            html.Span(status_info['icon'], style={'marginRight': '10px', 'fontSize': '1.5em'}),
            html.Strong(f"{robot_id.title()}: {status_info['text']}")
        ], style={'display': 'flex', 'alignItems': 'center', 'fontSize': '1.2em'})
    )

    details_content = html.Div([
        html.P(time_str, style={'fontSize': '0.9em', 'color': '#555', 'margin': '10px 0 5px 0'}),
        html.P(details_msg, style={'fontSize': '1.1em', 'margin': '5px 0 0 0'})
    ], style={'paddingLeft': '45px', 'paddingTop': '10px'})

    return html.Details([summary, details_content],
                        className=component_class, # Use combined class
                        id={'type': 'status-message', 'id': message_id}, # Use generic type
                        open=(message_id in open_message_ids),
                        # Background color is now handled by CSS
                       )

# --- App Initialization ---
app = dash.Dash(__name__, update_title=None, suppress_callback_exceptions=True)
server = app.server
static_map_data = load_static_data('static_map_data.json')
initial_figure = create_figure_for_frame(static_map_data, None)

# --- Study Screen Layouts ---
# ... (welcome_screen, briefing_screen, question_screen, post_study_questionnaire remain unchanged) ...
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



def briefing_screen(scenario_num, view_type, framework_mode):
    view_name = "Simulator View (Map + Log)" if view_type == 'map' else "Textual Overview"
    framework_name = "WITH Communication Framework" if framework_mode == 'with_framework' else "WITHOUT Communication Framework"

    briefing_text = f"""
    You are about to begin a segment for Scenario {scenario_num}.

    You will be using the:
    - {view_name}
    - {framework_name}

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
            html.H2(f"Scenario {scenario_num} - Briefing",
                    style={'color': '#00ff88', 'marginBottom': '30px'}),
            html.Pre(briefing_text, style={'whiteSpace': 'pre-wrap', 'lineHeight': '1.8',
                                           'fontSize': '16px'}),
            html.Button('Begin Scenario', id='begin-scenario-btn', n_clicks=0,
                        style={'padding': '15px 40px', 'fontSize': '18px',
                               'backgroundColor': '#00ff88', 'color': '#1e1e1e', 'border': 'none',
                               'borderRadius': '5px', 'cursor': 'pointer', 'fontWeight': 'bold', 'marginTop': '30px'})
        ])
    ])














def question_screen(scenario_num, question_num):
    questions = [
        {'text': '1. Mental Demand: How mentally demanding was monitoring the robots during this segment?', 'type': 'slider', 'id': 'mental-demand', 'min': 0, 'max': 20, 'marks': {0: 'Very Low', 10: 'Moderate', 20: 'Very High'}},
        {'text': '2. Physical Demand: How physically demanding was the task?', 'type': 'slider', 'id': 'physical-demand', 'min': 0, 'max': 20, 'marks': {0: 'Very Low', 10: 'Moderate', 20: 'Very High'}},
        {'text': '3. Temporal Demand: How hurried or rushed was the pace of the task?', 'type': 'slider', 'id': 'temporal-demand', 'min': 0, 'max': 20, 'marks': {0: 'Very Low', 10: 'Moderate', 20: 'Very High'}},
        {'text': '4. Performance: How successful were you in accomplishing what you were asked to do?', 'type': 'slider', 'id': 'performance', 'min': 0, 'max': 20, 'marks': {0: 'Perfect', 10: 'Moderate', 20: 'Failure'}},
        {'text': '5. Effort: How hard did you have to work to accomplish your level of performance?', 'type': 'slider', 'id': 'effort', 'min': 0, 'max': 20, 'marks': {0: 'Very Low', 10: 'Moderate', 20: 'Very High'}},
        {'text': '6. Frustration: How insecure, discouraged, irritated, stressed, and annoyed did you feel?', 'type': 'slider', 'id': 'frustration', 'min': 0, 'max': 20, 'marks': {0: 'Very Low', 10: 'Moderate', 20: 'Very High'}},
        {'text': '7. Situation Awareness: How well did you understand what was happening with the robots?', 'type': 'scale', 'id': 'situation-awareness', 'options': ['1 - Very Poor', '2 - Poor', '3 - Fair', '4 - Good', '5 - Excellent']},
        {'text': '8. How many robots did you observe replanning their routes during this segment? (This includes explicit "REPLANNING" messages or new routes being taken)', 'type': 'mcq', 'id': 'replan-count', 'options': ['0', '1', '2', '3', 'Not sure']},
        {'text': '9. Cognitive Load: How difficult was it to keep track of all three robots simultaneously?', 'type': 'scale', 'id': 'cognitive-load', 'options': ['1 - Very Easy', '2 - Easy', '3 - Moderate', '4 - Difficult', '5 - Very Difficult']},
        {'text': '10. Please describe any challenges, observations, or notable events from this segment:', 'type': 'open', 'id': 'open-response'}
    ]

    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                           'padding': '40px', 'fontFamily': 'Arial', 'overflowY': 'auto'}, children=[
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                        'maxWidth': '1000px', 'margin': '0 auto'}, children=[
            html.H2(f"Scenario {scenario_num} - Questionnaire #{question_num}",
                    style={'color': '#00ff88', 'marginBottom': '40px'}),
            html.Div([
                html.Div([
                    html.P(q['text'], style={'fontWeight': 'bold', 'marginBottom': '15px', 'fontSize': '16px', 'marginTop': '25px'}),
                    dcc.Slider(
                        id={'type': 'question', 'id': q['id']}, min=q['min'], max=q['max'], value=q['min'],
                        marks=q['marks'], step=1, tooltip={"placement": "bottom", "always_visible": False}
                    ) if q['type'] == 'slider' else (
                        dcc.RadioItems(
                            id={'type': 'question', 'id': q['id']},
                            options=[{'label': opt, 'value': opt} for opt in q['options']],
                            labelStyle={'display': 'block', 'marginBottom': '10px', 'cursor': 'pointer'},
                            style={'marginBottom': '20px'}
                        ) if q['type'] in ['scale', 'mcq'] else dcc.Textarea(
                            id={'type': 'question', 'id': q['id']}, placeholder='Type your response here...',
                            style={'width': '100%', 'minHeight': '100px', 'padding': '10px', 'fontSize': '14px',
                                   'borderRadius': '5px', 'marginBottom': '20px', 'border': '1px solid #444',
                                   'backgroundColor': '#1a1a1a', 'color': 'white'}
                        )
                    )
                ], style={'marginBottom': '20px'}) for q in questions
            ]),
            html.Button('Continue', id='submit-questions-btn', n_clicks=0,
                        style={'padding': '15px 40px', 'fontSize': '18px', 'backgroundColor': '#00ff88',
                               'color': '#1e1e1e', 'border': 'none', 'borderRadius': '5px',
                               'cursor': 'pointer', 'fontWeight': 'bold', 'marginTop': '30px'})
        ])
    ])












def post_study_questionnaire():
    questions = [
        {'text': '1. Which view mode did you find more helpful for monitoring the robots?', 'type': 'mcq', 'id': 'preferred-view', 'options': ['Simulator View (Map + Log)', 'Textual Overview', 'Both Equally', 'Neither']},
        {'text': '2. How helpful was the assistance framework (which provided richer "REPLANNING" alerts and status messages) in understanding robot behavior?', 'type': 'scale', 'id': 'framework-helpfulness', 'options': ['1 - Not Helpful', '2 - Slightly Helpful', '3 - Moderately Helpful', '4 - Very Helpful', '5 - Extremely Helpful']},
        {'text': '3. Overall Mental Workload: How would you rate the overall mental workload of this study?', 'type': 'slider', 'id': 'overall-workload', 'min': 0, 'max': 20, 'marks': {0: 'Very Low', 10: 'Moderate', 20: 'Very High'}},
        {'text': '4. How stressed did you feel during the study overall?', 'type': 'scale', 'id': 'overall-stress', 'options': ['1 - Not at all', '2 - Slightly', '3 - Moderately', '4 - Very', '5 - Extremely']},
        {'text': '5. Did you find the replanning notifications (the "REPLANNING" messages) useful when they appeared?', 'type': 'scale', 'id': 'notification-usefulness', 'options': ['1 - Not Useful', '2 - Slightly Useful', '3 - Moderately Useful', '4 - Very Useful', '5 - Extremely Useful']},
        {'text': '6. How confident were you in your understanding of the robot states throughout the study?', 'type': 'scale', 'id': 'confidence-level', 'options': ['1 - Not Confident', '2 - Slightly Confident', '3 - Moderately Confident', '4. Very Confident', '5 - Extremely Confident']},
        {'text': '7. What was the most challenging aspect of monitoring the multi-agent system?', 'type': 'open', 'id': 'challenging-aspect'},
        {'text': '8. What improvements would you suggest for the monitoring interface?', 'type': 'open', 'id': 'improvements'},
        {'text': '9. Any additional comments or feedback about the study:', 'type': 'open', 'id': 'additional-comments'}
    ]

    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'minHeight': '100vh',
                           'padding': '40px', 'fontFamily': 'Arial', 'overflowY': 'auto'}, children=[
        html.Div(style={'backgroundColor': '#2b2b2b', 'padding': '40px', 'borderRadius': '10px',
                        'maxWidth': '1000px', 'margin': '0 auto'}, children=[
            html.H2("Final Questionnaire", style={'color': '#00ff88', 'marginBottom': '20px'}),
            html.P("Thank you for completing all scenarios! Please answer these final questions about your overall experience.",
                   style={'marginBottom': '40px', 'fontSize': '16px'}),
            html.Div([
                html.Div([
                    html.P(q['text'], style={'fontWeight': 'bold', 'marginBottom': '15px', 'fontSize': '16px', 'marginTop': '25px'}),
                    dcc.Slider(
                        id={'type': 'post-question', 'id': q['id']}, min=q['min'], max=q['max'], value=q['min'],
                        marks=q['marks'], step=1, tooltip={"placement": 'bottom', "always_visible": False}
                    ) if q['type'] == 'slider' else (
                        dcc.RadioItems(
                            id={'type': 'post-question', 'id': q['id']},
                            options=[{'label': opt, 'value': opt} for opt in q['options']],
                            labelStyle={'display': 'block', 'marginBottom': '10px', 'cursor': 'pointer'},
                            style={'marginBottom': '20px'}
                        ) if q['type'] in ['scale', 'mcq'] else dcc.Textarea(
                            id={'type': 'post-question', 'id': q['id']}, placeholder='Type your response here...',
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
                        # <--- MODIFIED: Removed the html.Pre() for text-ui-output
                        html.Div(id='all-messages-feed', className='message-box-dark-theme')
                    ]),
                ])
            ]),

            # TEXT VIEW
            html.Div(id='text-view-container', style={'display': 'none', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}, children=[
                *[html.Div(className='robot-column', children=[
                    html.Div(className='robot-card-top', children=[dcc.Slider(id=f'robot-{i}-timeline', min=0, max=49, value=0, disabled=True, marks={} , tooltip={"always_visible": False})]),
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
            html.P("You may now close this window.", style={'marginTop': '30px', 'color': '#888'})
        ])
    ])

# --- App Layout ---
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
    dcc.Store(id='all-messages-store', data=[]),
    dcc.Store(id='responses-store', data=[]),
    dcc.Store(id='interaction-log-store', data=[]),
    # MODIFIED: Add store for message appearance timestamps
    dcc.Store(id='message-timestamps-store', data={}),
    dcc.Interval(id='animation-interval', interval=UPDATE_INTERVAL_MS, n_intervals=0, disabled=True)
])

# --- Callbacks ---
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

    participant_id = generate_participant_id(name)
    assigned_scenarios = assign_participant_scenarios(name)

    participant_data = {
        'id': participant_id,
        'name': name,
        'scenarios': assigned_scenarios,
        'start_time': datetime.now().isoformat()
    }

    study_state = {
        'current_scenario_idx': 0,
        'current_condition_idx': 0,
        'current_question_idx': 0,
        'phase': 'briefing',
        'segment_start_time': None
    }

    scenario_num = assigned_scenarios[0]
    # Start with first condition (map, with framework)
    return briefing_screen(scenario_num, 'map', 'with_framework'), participant_data, study_state, ""

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

    # Create a new copy to trigger the store update
    new_study_state = study_state.copy()
    new_study_state['phase'] = 'simulation'
    new_study_state['segment_start_time'] = datetime.now().isoformat()

    return create_simulation_layout(), new_study_state

# MODIFIED: Added Outputs to reset message stores
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
    Output('all-messages-store', 'data', allow_duplicate=True), # <-- Added Reset
    Output('open-messages-store', 'data', allow_duplicate=True), # <-- Added Reset
    Output('message-timestamps-store', 'data', allow_duplicate=True), # <-- Added Reset
    Input('simulation-layout-loaded-signal', 'children'),
    State('study-state-store', 'data'),
    State('participant-store', 'data'),
    prevent_initial_call=True
)
def load_data_and_start_simulation(layout_signal, study_state, participant_data):
    if not study_state or not participant_data or study_state.get('phase') != 'simulation':
        raise PreventUpdate

    print("load_data_and_start_simulation firing...")

    scenario_num = participant_data['scenarios'][study_state['current_scenario_idx']]
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
        # Resume from *after* the last pause point
        start_frame = pause_points[study_state['current_question_idx'] - 1] + 1

    max_frames = len(frames) - 1 if frames else 0
    mid_point = max_frames // 2
    marks = {0: 'Start', mid_point: 'Midpoint', max_frames: 'End'}

    # Return empty lists/dict to reset message stores
    return frames, hmms, start_frame, max_frames, max_frames, max_frames, marks, marks, marks, [], [], {}

@app.callback(
    Output('animation-interval', 'disabled'),
    Input('study-state-store', 'data'),
)
def control_animation(study_state):
    if study_state and study_state.get('phase') == 'simulation':
        print("Enabling animation interval")
        return False
    print("Disabling animation interval")
    return True

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

    next_frame = current_frame + 1 # Calculate potential next frame
    max_frames = len(scenario_data) - 1

    # Stop if past the end
    if current_frame >= max_frames:
        # This will be handled by the submit_questions logic after the last question pause
        # Need to ensure the interval stops
        new_state = study_state.copy()
        new_state['phase'] = 'paused_at_end' # Use a temporary state to stop interval
        print("Reached end of frames, pausing.")
        return no_update, no_update, new_state


    scenario_num = participant_data['scenarios'][study_state['current_scenario_idx']]
    pause_points = PAUSE_POINTS.get(scenario_num, [100, 200, 300])

    if study_state['current_question_idx'] < len(pause_points):
        current_pause_point = pause_points[study_state['current_question_idx']]

        # Check if the *current* frame is the pause point (pause happens *after* rendering the pause frame)
        if current_frame == current_pause_point:
            # PAUSE!
            new_study_state = study_state.copy()
            new_study_state['phase'] = 'questions'
            # Update frame to the pause point, then change page and state
            print(f"Pausing at frame {current_frame} for question set {study_state['current_question_idx'] + 1}")
            # Don't update frame here, stay on the pause frame
            return no_update, question_screen(scenario_num, study_state['current_question_idx'] + 1), new_study_state

    # No pause, just advance the frame
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
        # Keep layout hidden if not in simulation phase
        return {'display': 'none'}, {'display': 'none'}, ""

    condition_idx = study_state['current_condition_idx']
    scenario_num = participant_data['scenarios'][study_state['current_scenario_idx']]

    map_style = {'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}
    text_style = {'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}

    view_name, framework_name = "", ""

    if condition_idx < 2: # Conditions 0 and 1 are Map view
        view_name = "Simulator View (Map + Log)"
        map_style['display'] = 'flex'
        text_style['display'] = 'none'
    else: # Conditions 2 and 3 are Text view
        view_name = "Textual Overview"
        map_style['display'] = 'none'
        text_style['display'] = 'flex'

    if condition_idx % 2 == 0: # Conditions 0 and 2 are With Framework
        framework_name = "WITH Communication Framework"
    else: # Conditions 1 and 3 are Without Framework
        framework_name = "WITHOUT Communication Framework"

    header_text = f"Scenario: {scenario_num} | View: {view_name} | Framework: {framework_name}"

    return map_style, text_style, header_text

# MODIFIED: Changed Input for clicks, added Input for study_state
@app.callback(
    Output('simulation-graph', 'figure'),
    # <--- MODIFIED: Removed 'text-ui-output'
    Output('robot-1-messages', 'children'),
    Output('robot-2-messages', 'children'),
    Output('robot-3-messages', 'children'),
    Output('robot-1-timeline', 'value'),
    Output('robot-2-timeline', 'value'),
    Output('robot-3-timeline', 'value'),
    Output('hmm-data-store', 'data', allow_duplicate=True),
    Output('all-messages-feed', 'children'),
    Output('all-messages-store', 'data', allow_duplicate=True),
    Output('animation-interval', 'interval'),
    Output('interaction-log-store', 'data', allow_duplicate=True), # <--- MODIFIED: Added allow_duplicate
    Output('open-messages-store', 'data'),
    Output('message-timestamps-store', 'data'), # Added output for timestamps
    Input('current-frame-store', 'data'),
    Input({'type': 'status-message', 'id': ALL}, 'open'), # MODIFIED: Listen to generic type
    Input('study-state-store', 'data'), # MODIFIED: Added Input
    State('scenario-data-store', 'data'),
    State('hmm-data-store', 'data'),
    # State('study-state-store', 'data'), # Now an Input
    State('participant-store', 'data'),
    [State(f'robot-{i}-messages', 'children') for i in range(1, 4)],
    State('open-messages-store', 'data'),
    State('all-messages-store', 'data'),
    State('interaction-log-store', 'data'),
    State('message-timestamps-store', 'data'), # Added state for timestamps
    prevent_initial_call=True
)
def update_simulation_views(frame_idx, message_opens, study_state, # Added study_state
                            scenario_data, hmm_data,
                            participant_data, hist1, hist2, hist3,
                            open_message_ids, all_messages_history, interactions,
                            message_timestamps): # Added message_timestamps

    # Guard clause: Only run if in simulation phase
    if not study_state or study_state.get('phase') != 'simulation':
        # <--- MODIFIED: Return 14 no_updates
        return (no_update,) * 14 # Match number of outputs

    # <--- MODIFIED: Make copies of data from State to ensure Dash detects changes
    new_interactions = interactions.copy() if interactions is not None else []
    new_open_message_ids = set(open_message_ids) if open_message_ids else set()
    new_message_timestamps = message_timestamps.copy() if message_timestamps else {} # Handle initial state

    triggered = callback_context.triggered

    # Handle message click interactions
    if triggered:
        for item in triggered:
            prop_id = item['prop_id']
            # Check if the trigger was a message being opened/closed
            if '.open' in prop_id:
                try:
                    component_id_str = prop_id.split('.')[0]
                    component_id_dict = json.loads(component_id_str)

                    # Check if it's the right type
                    if component_id_dict.get('type') == 'status-message':
                        message_id = component_id_dict['id']
                        is_open = item['value']
                        action = "opened" if is_open else "closed"
                        click_time = time.time()
                        appear_time = new_message_timestamps.get(message_id)
                        time_to_click = (click_time - appear_time) if appear_time else -1.0


                        interaction_entry = {
                            'timestamp_iso': datetime.now().isoformat(),
                            'timestamp_unix': click_time,
                            'participant': participant_data.get('id'),
                            'scenario': participant_data['scenarios'][study_state['current_scenario_idx']],
                            'condition': study_state['current_condition_idx'],
                            'frame': frame_idx,
                            'type': 'message_click',
                            'message_id': message_id,
                            'action': action,
                            'time_since_appear_s': time_to_click
                        }
                        
                        # <--- MODIFIED: Append to the *copy* of the list
                        new_interactions.append(interaction_entry)

                        if is_open:
                            new_open_message_ids.add(message_id)
                        else:
                            new_open_message_ids.discard(message_id)
                except Exception as e:
                    print(f"Error parsing interaction: {e}, prop_id: {prop_id}")

    open_message_ids = list(new_open_message_ids) # <--- MODIFIED: Convert new set back to list

    # --- Standard Simulation Update Logic ---

    if not all([scenario_data, hmm_data, study_state, participant_data]):
         # This should ideally not happen due to the guard clause, but added robustness
         print("Warning: Missing data in update_simulation_views")
         # <--- MODIFIED: Return 14 no_updates
         return (no_update,) * 14


    # Handle potential race condition where frame_idx is updated before scenario_data
    if frame_idx is None or frame_idx >= len(scenario_data):
         print(f"Warning: frame_idx ({frame_idx}) out of bounds or None for scenario_data length ({len(scenario_data)})")
         # Try returning current state if possible, else initial figure
         current_fig = initial_figure
         try:
              current_fig = callback_context.outputs_list[0].get('value', initial_figure) # Safer access
         except Exception as e:
              print(f"Error accessing previous figure state: {e}")
              pass # Use initial_figure
         
         # <--- MODIFIED: Return 14 values
         return (
              current_fig, 
              hist1, hist2, hist3, # Keep current messages
              frame_idx if frame_idx is not None else 0, # Keep current frame
              frame_idx if frame_idx is not None else 0,
              frame_idx if frame_idx is not None else 0,
              hmm_data, # Keep current HMM
              all_messages_history or [], all_messages_history or [], # Keep current messages
              UPDATE_INTERVAL_MS, 
              new_interactions, # <--- MODIFIED: Return the (empty) new list
              open_message_ids or [], 
              new_message_timestamps or {}
         )


    condition_idx = study_state['current_condition_idx']
    scenario_num = participant_data['scenarios'][study_state['current_scenario_idx']]
    framework_mode = 'with_framework' if condition_idx % 2 == 0 else 'without_framework'

    current_hmms = hmm_data.copy() if hmm_data else {} # Ensure it's a dict
    current_frame_data = scenario_data[frame_idx]
    fig = create_figure_for_frame(static_map_data, current_frame_data)

    mission_time_threshold = THRESHOLD_VALUES[framework_mode].get(scenario_num, 1)

    robots_dict = current_frame_data.get('robots', {})
    packages = current_frame_data.get('packages', [])

    # <--- MODIFIED: log_text is no longer needed
    histories = [hist1, hist2, hist3]
    # Initialize with current histories or empty lists
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
                try: # Add error handling around backend call
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
                    sync_occurred = False # Prevent message generation on error
                    updated_hmm_array = selected_robot_hmm_array # Keep old HMM


                current_hmms[robot_id] = updated_hmm_array

                # --- MODIFICATION START ---
                # Generate message if sync occurred, regardless of framework
                if sync_occurred:
                    any_sync_occurred = True
                    new_message_div = create_rich_status_message(
                        robot_info,
                        sim_time,
                        packages,
                        open_message_ids,
                        selected_robot_hmm_array, # Pass HMM *before* update
                        selected_robot_rmm_array,
                        scenario_num
                    )

                    # <--- MODIFIED: Logic to add flash animation class
                    # Log appearance time and check if new
                    is_new_message = False
                    msg_id = new_message_div.id['id']
                    if msg_id not in new_message_timestamps:
                         new_message_timestamps[msg_id] = time.time()
                         is_new_message = True # It's brand new

                    # Add flash class if new
                    if is_new_message:
                        current_class = new_message_div.className or ""
                        new_message_div.className = current_class + " new-message"
                    # <--- END MODIFICATION

                    # Add to lists - these will be used or cleared based on framework later
                    newly_generated_messages_for_feed.append(new_message_div)

                    updated_history = [new_message_div]
                    # Ensure histories[i-1] is treated as a list
                    current_hist = histories[i-1] if isinstance(histories[i-1], list) else ([histories[i-1]] if histories[i-1] else [])

                    if current_hist:
                        updated_history.append(html.P("--- previous updates ---", className="divider"))
                        updated_history.extend(current_hist)
                    new_robot_message_outputs[i-1] = updated_history
                # --- MODIFICATION END ---


    # --- MODIFICATION START ---
    # Combine messages based on generated messages, DON'T explicitly clear based on framework here.
    # The reset happens in load_data_and_start_simulation
    updated_all_messages = newly_generated_messages_for_feed + (all_messages_history or [])
    updated_all_messages = updated_all_messages[:100] # Limit length

    # Determine interval based on whether sync occurred and framework is on
    new_interval = SLOW_INTERVAL_MS if any_sync_occurred and framework_mode == 'with_framework' else UPDATE_INTERVAL_MS
    # --- MODIFICATION END ---

    # <--- MODIFIED: Return 14 items, including new_interactions
    return (
        fig,
        *new_robot_message_outputs, # Unpack the list (3 items)
        frame_idx, frame_idx, frame_idx,
        current_hmms,
        updated_all_messages, updated_all_messages, # Send the potentially populated list
        new_interval,
        new_interactions, # <-- Return the modified COPY
        open_message_ids,
        new_message_timestamps # Return updated timestamps
    )
    
    
@app.callback(
    Output('simulation-map-snapshot', 'figure'),
    Input('simulation-graph', 'figure'),
    Input('study-state-store', 'data') # Add dependency
)
def update_snapshot(main_fig, study_state): # Add argument
    # Guard clause
    if not study_state or study_state.get('phase') != 'simulation':
        return no_update # Don't update if not in simulation

    if main_fig is None:
        return initial_figure # Or no_update? Initial is safer.

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

# <--- NEW CALLBACK TO LOG MAP CLICKS ---
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

    # Make a copy to ensure Dash detects the change
    new_interactions = interactions.copy() if interactions is not None else []
    
    # Try to get useful info from the click
    try:
        clicked_point_info = clickData['points'][0]
        # Get hovertext, or text, or just the point index as a fallback
        details = clicked_point_info.get('hovertext', clicked_point_info.get('text', f"point_index_{clicked_point_info.get('pointIndex')}"))
    except Exception as e:
        print(f"Error parsing clickData: {e}")
        details = "graph_click_parse_error"

    interaction_entry = {
        'timestamp_iso': datetime.now().isoformat(),
        'timestamp_unix': time.time(),
        'participant': participant_data.get('id'),
        'scenario': participant_data.get('scenarios', [])[study_state.get('current_scenario_idx', 0)],
        'condition': study_state.get('current_condition_idx'),
        'frame': frame_idx,
        'type': 'graph_click',
        'click_details': details
    }
    
    new_interactions.append(interaction_entry)
    
    return new_interactions
# <--- END OF NEW CALLBACK ---

@app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Output('responses-store', 'data', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
    Input('submit-questions-btn', 'n_clicks'),
    State('study-state-store', 'data'),
    State('participant-store', 'data'),
    State('responses-store', 'data'),
    State({'type': 'question', 'id': ALL}, 'value'),
    State({'type': 'question', 'id': ALL}, 'id'),
    State('interaction-log-store', 'data'), # <--- MODIFIED: Get interaction data
    prevent_initial_call=True
)
def submit_questions(n_clicks, study_state, participant_data, responses, q_values, q_ids, interactions): # <--- MODIFIED: Add interactions
    if n_clicks == 0 or not study_state or not participant_data:
        raise PreventUpdate

    scenario_num = participant_data['scenarios'][study_state['current_scenario_idx']]
    condition_idx = study_state['current_condition_idx']
    view_type = 'map' if condition_idx < 2 else 'text'
    framework = 'with_framework' if condition_idx % 2 == 0 else 'without_framework'

    answer_dict = {q_id['id']: val for q_id, val in zip(q_ids, q_values)}
    ordered_answers = [
        answer_dict.get('mental-demand'), answer_dict.get('physical-demand'),
        answer_dict.get('temporal-demand'), answer_dict.get('performance'),
        answer_dict.get('effort'), answer_dict.get('frustration'),
        answer_dict.get('situation-awareness'), answer_dict.get('replan-count'),
        answer_dict.get('cognitive-load'), answer_dict.get('open-response')
    ]

    response_entry = {
        'timestamp': datetime.now().isoformat(),
        'segment_start_time': study_state.get('segment_start_time'),
        'scenario': scenario_num,
        'condition': condition_idx,
        'view_type': view_type,
        'framework': framework,
        'question_set': study_state['current_question_idx'] + 1,
        'answers': ordered_answers
    }
    responses.append(response_entry)

    # <--- MODIFIED: Save data incrementally after each questionnaire
    try:
        print(f"Incrementally saving data for {participant_data.get('id')}. Responses: {len(responses)}, Interactions: {len(interactions if interactions else [])}")
        save_study_data(participant_data, responses, interactions)
    except Exception as e:
        print(f"Error during incremental save: {e}")
    # <--- END MODIFICATION

    new_study_state = study_state.copy()
    new_study_state['current_question_idx'] += 1

    pause_points = PAUSE_POINTS.get(scenario_num, [100, 200, 300])

    if new_study_state['current_question_idx'] < len(pause_points):
        # Go back to simulation
        new_study_state['phase'] = 'simulation'
        return create_simulation_layout(), responses, new_study_state
    else:
        # Finished all segments for this condition
        new_study_state['current_condition_idx'] += 1
        new_study_state['current_question_idx'] = 0 # Reset for next condition/scenario

        if new_study_state['current_condition_idx'] >= 4:
            # Finished all 4 conditions for this scenario
            new_study_state['current_scenario_idx'] += 1
            new_study_state['current_condition_idx'] = 0 # Reset for next scenario

            if new_study_state['current_scenario_idx'] >= len(participant_data['scenarios']):
                # Finished all scenarios
                new_study_state['phase'] = 'post_study'
                return post_study_questionnaire(), responses, new_study_state
            else:
                # Go to briefing for next scenario
                new_study_state['phase'] = 'briefing'
                next_scenario_num = participant_data['scenarios'][new_study_state['current_scenario_idx']]
                # Determine view/framework for the *first* condition of the next scenario
                next_condition_idx = 0
                next_view_type = 'map' if next_condition_idx < 2 else 'text'
                next_framework = 'with_framework' if next_condition_idx % 2 == 0 else 'without_framework'
                return briefing_screen(next_scenario_num, next_view_type, next_framework), responses, new_study_state
        else:
            # Go to briefing for next condition
            new_study_state['phase'] = 'briefing'
            current_scenario_num = participant_data['scenarios'][new_study_state['current_scenario_idx']]
            next_condition_idx = new_study_state['current_condition_idx']
            next_view_type = 'map' if next_condition_idx < 2 else 'text'
            next_framework = 'with_framework' if next_condition_idx % 2 == 0 else 'without_framework'
            return briefing_screen(current_scenario_num, next_view_type, next_framework), responses, new_study_state


@app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('submit-final-btn', 'n_clicks'),
    State('participant-store', 'data'),
    State('responses-store', 'data'),
    State('interaction-log-store', 'data'),
    State({'type': 'post-question', 'id': ALL}, 'value'),
    State({'type': 'post-question', 'id': ALL}, 'id'),
    prevent_initial_call=True
)
def submit_final_questionnaire(n_clicks, participant_data, responses, interactions, post_values, post_ids):
    if not participant_data:
        raise PreventUpdate

    answer_dict = {q_id['id']: val for q_id, val in zip(post_ids, post_values)}
    post_response = {
        'timestamp': datetime.now().isoformat(),
        'type': 'post_study',
        'answers': answer_dict
    }
    responses.append(post_response)

    # <--- MODIFIED: Final save call
    print("Saving final study data...")
    save_study_data(participant_data, responses, interactions)

    return thank_you_screen()

# --- Main Execution ---
if __name__ == '__main__':
    if not os.path.exists("assets"):
        os.makedirs("assets")
    # MODIFIED: Updated CSS for generic message container styling and added animation
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
.divider { text-align: center; color: #aaa; font-size: 0.9em; margin: 15px 0; }
.divider::before, .divider::after { content: ' ― '; }
.robot-card-top .rc-slider-track { background-color: #007bff !important; height: 12px;}
.robot-card-top .rc-slider-rail { background-color: #e9ecef !important; height: 12px;}
.robot-card-top .rc-slider-mark-text { color: #555; font-weight: bold; }
.robot-card-top .rc-slider-disabled .rc-slider-handle { display: none; }

/* --- MODIFIED CSS START --- */
/* Base style for all message containers */
.message-container-details {
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 13px;
    border: 1px solid #ddd;
    color: #212529;
    /* Background color set by specific class below */
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
}
.message-container-details.on-track {
    background-color: #e0f5e1; /* Green for on-track */
}
.message-container-details.stationary {
    background-color: #fff9c4; /* Yellow for stationary */
}
/* --- MODIFIED CSS END --- */

/* --- NEW: Animation for new messages --- */
@keyframes flash-border {
    0% { box-shadow: 0 0 10px 3px #00ff88; }
    100% { box-shadow: none; }
}
.message-container-details.new-message {
    animation: flash-border 1.2s ease-out;
}
/* --- END OF NEW CSS --- */
        """)
    # Use debug=False for actual study deployment
    # app.run(debug=True, host='0.0.0.0', port=1091) # Keep debug=True for testing
    app.run(debug=False, host='0.0.0.0', port=1049)