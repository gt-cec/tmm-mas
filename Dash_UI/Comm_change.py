

import dash
from dash import dcc, html, Input, Output, State, callback_context, no_update
from dash.dependencies import ALL
import plotly.graph_objects as go
import json
import os
import glob
from datetime import datetime


from backend_operations import (
    dynamic_deviation_threshold_multi_logic
)


# --- Constants ---
GRID_WIDTH = 20
GRID_HEIGHT = 20
UPDATE_INTERVAL_MS = 1000


# --- Threshold values for each scenario and framework mode ---
THRESHOLD_VALUES = {
    'with_framework': {
        1: 5,
        2: 12,
        3: 15,
        4: 9
    },
    'without_framework': {
        1: 1,
        2: 1,
        3: 1,
        4: 1
    }
}


# --- Total Expected Times and Steps for Each Scenario ---
SCENARIO_CONFIG = {
    1: {'total_time': 406.0, 'total_steps': 242},
    2: {'total_time': 240.0, 'total_steps': 150},
    3: {'total_time': 190.0, 'total_steps': 180},
    4: {'total_time': 220.0, 'total_steps': 160}
}


# --- HMM Data Loading ---
try:
    with open('all_scenarios_hmm_data.json', 'r') as f:
        ALL_SCENARIOS_HMM_DATA = json.load(f)
except FileNotFoundError:
    print("FATAL ERROR: 'all_scenarios_hmm_data.json' not found. This file is required.")
    ALL_SCENARIOS_HMM_DATA = {}


def get_hmms_for_active_scenario(scenario_number):
    """
    Retrieves HMM data for the selected scenario.
    """
    scenario_key = f'scenario_{scenario_number}'
    scenario_data = ALL_SCENARIOS_HMM_DATA.get(scenario_key, {})
    
    HMM_Robot_1 = scenario_data.get('HMM_Robot_1')
    HMM_Robot_2 = scenario_data.get('HMM_Robot_2')
    HMM_Robot_3 = scenario_data.get('HMM_Robot_3')
    
    return HMM_Robot_1, HMM_Robot_2, HMM_Robot_3


# --- Data Loading ---
def load_static_data(filepath):
    """Load static map data from JSON file."""
    try:
        with open(filepath, 'r') as f: return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Will use data from frame files.")
        return {"walls": [], "zones": [], "nodes": [], "edges": []}


def load_scenario_frames(scenario_id):
    """Load all frame_X.json files in proper numerical order."""
    folder = f"scenarios_with_graphs/scenario_{scenario_id}/"
    frames = []
    if not os.path.isdir(folder):
        print(f"Scenario folder {folder} does not exist.")
        return frames
    frame_files = sorted(glob.glob(os.path.join(folder, "frame_*.json")), key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))
    for frame_file in frame_files:
        try:
            with open(frame_file, "r") as f: data = json.load(f); frames.append(data)
        except Exception as e: print(f"Error loading {frame_file}: {e}")
    print(f"Loaded {len(frames)} frames for scenario_{scenario_id}")
    return frames


# --- Figure and Component Creation ---
def create_figure_for_frame(static_data, frame_data):
    """Creates the complete figure for a single frame."""
    fig = go.Figure()
    fig.update_layout(
        xaxis=dict(range=[0, GRID_WIDTH], autorange=False, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False, dtick=10, scaleanchor="y", scaleratio=1),
        yaxis=dict(range=[0, GRID_HEIGHT], autorange=False, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False),
        plot_bgcolor='#ffffff', paper_bgcolor='#f5f5f5', font=dict(color='black'),
        showlegend=False, margin=dict(l=20, r=20, t=20, b=20), uirevision='constant'
    )
    walls_data = frame_data.get('walls', []) if frame_data else []
    if not walls_data: walls_data = static_data.get('walls', [])
    zones_data = frame_data.get('zones', []) if frame_data else []
    if not zones_data: zones_data = static_data.get('zones', [])
    nodes_data = frame_data.get('nodes', []) if frame_data else []
    if not nodes_data: nodes_data = static_data.get('nodes', [])
    edges_data = frame_data.get('edges', []) if frame_data else []
    if not edges_data: edges_data = static_data.get('edges', [])


    for wall in walls_data:
        wall_coords = sorted(wall.items())
        wall_x = [v for k, v in wall_coords if k.startswith('x')]
        wall_y = [v for k, v in wall_coords if k.startswith('y')]
        fig.add_trace(go.Scatter(
            x=wall_x, y=wall_y, mode='lines',
            line=dict(color='black', width=2),
            hoverinfo='none'
        ))


    for zone in zones_data:
        color_str = zone.get('color', 'rgba(0,0,0,0)')
        if color_str.startswith('('):
            color_str = f"rgb{color_str}"
        zone_coords = sorted(zone.items())
        zone_x = [v for k, v in zone_coords if k.startswith('x')]
        zone_y = [v for k, v in zone_coords if k.startswith('y')]
        fig.add_trace(go.Scatter(
            x=zone_x, y=zone_y,
            fill="toself",
            fillcolor=color_str,
            line=dict(width=0),
            mode='lines',
            hoverinfo='none'
        ))
    
    edge_x, edge_y = [], []
    for edge in edges_data:
        edge_x.extend([edge['x0'], edge['x1'], None]); edge_y.extend([edge['y0'], edge['y1'], None])
    if edge_x:
        fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(width=0.5, color='rgba(50, 50, 50, 0.75)'), hoverinfo='none'))
    if nodes_data:
        node_x = [node[0] for node in nodes_data]; node_y = [node[1] for node in nodes_data]
        fig.add_trace(go.Scatter(x=node_x, y=node_y, mode='markers', marker=dict(size=4, color='rgba(50, 50, 150, 0.8)'), hoverinfo='none'))


    if frame_data:
        robots = [{'id': rid, **rdata} for rid, rdata in frame_data.get('robots', {}).items()]
        packages = frame_data.get('packages', [])
        if robots:
            traces = {'x': [], 'y': [], 'colors': [], 'texts': [], 'hovers': []}
            for r in robots:
                traces['x'].append(r['x']); traces['y'].append(r['y']); traces['texts'].append(r['id'][-1])
                traces['hovers'].append(f"{r['id']} State: {r['state']} Pos: ({r['x']:.1f}, {r['y']:.1f})")
                traces['colors'].append({'moving': 'red', 'carrying': 'orange', 'waiting': 'blue'}.get(r['state'], 'grey'))
            fig.add_trace(go.Scatter(x=traces['x'], y=traces['y'], mode='markers+text', marker=dict(size=30, color=traces['colors'], line=dict(width=2, color='white')),
                                      text=traces['texts'], textposition='middle center', textfont=dict(color='white', size=12, family="Arial Black"),
                                      hovertext=traces['hovers'], hoverinfo='text'))
        if packages:
            traces = {'x': [], 'y': [], 'texts': [], 'hovers': []}
            robot_pos = {r['id']: (r['x'], r['y']) for r in robots}
            for p in packages:
                px, py = robot_pos.get(p.get('carried_by'), (p.get('x', 0), p.get('y', 0)))
                traces['x'].append(px); traces['y'].append(py); traces['texts'].append(p['id'][-1])
                traces['hovers'].append(f"Package {p['id']}, {'Carried' if p.get('carried_by') else 'On Ground'}")
            fig.add_trace(go.Scatter(x=traces['x'], y=traces['y'], mode='markers+text', marker=dict(size=20, color='gold', symbol='square', line=dict(width=1, color='black')),
                                      text=traces['texts'], textposition='middle center', textfont=dict(color='black', size=10, family="Arial Black"),
                                      hovertext=traces['hovers'], hoverinfo='text'))
    return fig


def create_rich_status_message(robot_data, sim_time, all_packages, open_message_ids, selected_robot_hmm_array, selected_robot_rmm_array, scenario_id):
    """
    Creates rich status messages with X/Y coordinate format, time differential analysis,
    and HMM/RMM feature comparisons.
    """
    if open_message_ids is None:
        open_message_ids = []
    
    time_str = datetime.now().strftime('%I:%M:%S %p')
    robot_id = robot_data.get('id', 'N/A')
    x, y = float(robot_data.get('x', 0)), float(robot_data.get('y', 0))
    
    status_map = {
        'replan': {'text': 'REPLANNING', 'color': '#ffdede', 'icon': '🔄'},
        'on_track': {'text': 'ON TRACK', 'color': '#e0f5e1', 'icon': '✅'},
        'stationary': {'text': 'STATIONARY', 'color': '#fff9c4', 'icon': '⏸️'}
    }
    
    # Calculate expected time based on plan_index
    plan_index = selected_robot_rmm_array.get('plan_index', 0)
    scenario_config = SCENARIO_CONFIG.get(scenario_id, {'total_time': 300.0, 'total_steps': 100})
    total_expected_time = scenario_config['total_time']
    total_steps = scenario_config['total_steps']
    
    # Calculate time per step
    time_per_step = total_expected_time / total_steps if total_steps > 0 else 0
    
    # Calculate expected time at current index
    if plan_index > 0:
        expected_time = plan_index * time_per_step
        time_difference = expected_time - sim_time
    else:
        time_difference = 0
    
    # Determine if ahead or behind
    time_status_text = ""
    if abs(time_difference) > 0.1:
        if time_difference > 0:
            time_status_text = f"Robot is {int(abs(time_difference))} seconds ahead of schedule."
        else:
            time_status_text = f"Robot is {int(abs(time_difference))} seconds behind schedule."
    
        
        
    # Compare HMM and RMM features - FIXED with type conversion
    feature_alerts = []

    # Weather comparison - show ANY change
    hmm_weather = int(selected_robot_hmm_array.get('Current_weather', 1)) if selected_robot_hmm_array else 1
    rmm_weather = int(selected_robot_rmm_array.get('Current_weather', 1))

    # Print HMM and RMM weather values
    print(f"[{robot_id}] Weather - HMM: {hmm_weather} (type: {type(hmm_weather)}), RMM: {rmm_weather} (type: {type(rmm_weather)})")

    if hmm_weather != rmm_weather:
        if rmm_weather == 0:
            feature_alerts.append("Weather has turned bad.")
        elif rmm_weather == 1:
            feature_alerts.append("Weather has improved.")

    # Battery comparison - show ANY change
    hmm_battery = int(selected_robot_hmm_array.get('Battery_status', 1)) if selected_robot_hmm_array else 1
    rmm_battery = int(selected_robot_rmm_array.get('Battery_status', 1))

    # Print HMM and RMM battery values
    print(f"[{robot_id}] Battery - HMM: {hmm_battery} (type: {type(hmm_battery)}), RMM: {rmm_battery} (type: {type(rmm_battery)})")

    if hmm_battery != rmm_battery:
        if rmm_battery == 0:
            feature_alerts.append("Battery is low (<40%).")
        elif rmm_battery == 2:
            feature_alerts.append("Battery is dead.")
        elif rmm_battery == 1:
            feature_alerts.append("Battery is good (>40%).")

    # Connectivity comparison - show ANY change
    hmm_offline = int(selected_robot_hmm_array.get('Momentarily_offline', 0)) if selected_robot_hmm_array else 0
    rmm_offline = int(selected_robot_rmm_array.get('Momentarily_offline', 0))

    # Print HMM and RMM offline values
    print(f"[{robot_id}] Offline - HMM: {hmm_offline} (type: {type(hmm_offline)}), RMM: {rmm_offline} (type: {type(rmm_offline)})")

    if hmm_offline != rmm_offline:
        if rmm_offline == 1:
            feature_alerts.append("Robot is momentarily offline.")
        elif rmm_offline == 0:
            feature_alerts.append("Robot is back online.")

    # Build feature alert text
    feature_text = " ".join(feature_alerts) if feature_alerts else ""

    print(f"[{robot_id}] Feature alerts: {feature_alerts}")  # DEBUG
        
        
        
        
    # # Compare HMM and RMM features
    # feature_alerts = []
    
    # # Weather comparison
    # hmm_weather = selected_robot_hmm_array.get('Current_weather', 1) if selected_robot_hmm_array else 1
    # rmm_weather = selected_robot_rmm_array.get('Current_weather', 1)
    
    # # Print HMM and RMM weather values
    # print(f"[{robot_id}] Weather - HMM: {hmm_weather}, RMM: {rmm_weather}")
    
    # if hmm_weather != rmm_weather and rmm_weather == 0:
    #     feature_alerts.append("Weather has turned bad.")
    
    # # Battery comparison
    # hmm_battery = selected_robot_hmm_array.get('Battery_status', 1) if selected_robot_hmm_array else 1
    # rmm_battery = selected_robot_rmm_array.get('Battery_status', 1)
    
    # # Print HMM and RMM battery values
    # print(f"[{robot_id}] Battery - HMM: {hmm_battery}, RMM: {rmm_battery}")
    
    # if hmm_battery != rmm_battery:
    #     if rmm_battery == 0:
    #         feature_alerts.append("Battery is low (<40%).")
    #     elif rmm_battery == 2:
    #         feature_alerts.append("Battery is dead.")
    #     elif rmm_battery == 1:
    #         feature_alerts.append("Battery is good (>40%).")
    
    # # Connectivity comparison
    # hmm_offline = selected_robot_hmm_array.get('Momentarily_offline', 0) if selected_robot_hmm_array else 0
    # rmm_offline = selected_robot_rmm_array.get('Momentarily_offline', 0)
    
    # # Print HMM and RMM offline values
    # print(f"[{robot_id}] Offline - HMM: {hmm_offline}, RMM: {rmm_offline}")
    
    # if hmm_offline != rmm_offline and rmm_offline == 1:
    #     feature_alerts.append("Robot is momentarily offline.")
    
    # # Build feature alert text
    # feature_text = " ".join(feature_alerts) if feature_alerts else ""
    
    
    
    
    # Check for replan flag FIRST (highest priority)
    state = robot_data.get('state')
    if robot_data.get('replan_flag') == True:
        message_id = f"{robot_id}-{sim_time}"
        
        # Build details message with time and features for replanning
        time_and_features = []
        if time_status_text:
            time_and_features.append(time_status_text)
        if feature_text:
            time_and_features.append(feature_text)
        
        combined_info = " ".join(time_and_features) if time_and_features else ""
        
        if state == 'moving':
            details_msg = f"Route recalculated. Heading to Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()
        elif state == 'waiting':
            details_msg = f"Route recalculated. Waiting at Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()
        elif state == 'carrying':
            pkg_id = next((p['id'] for p in all_packages if p.get('carried_by') == robot_id), "N/A")
            details_msg = f"Route recalculated. Carrying {pkg_id} to Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()
        else:
            details_msg = f"Route recalculated. Status: {state} at Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()
        
        summary = html.Summary(
            html.Div([
                html.Span(status_map['replan']['icon'], style={'marginRight': '10px', 'fontSize': '1.5em'}),
                html.Strong(f"{robot_id.title()}: {status_map['replan']['text']}")
            ], style={'display': 'flex', 'alignItems': 'center', 'fontSize': '1.2em'})
        )
        
        details_content = html.Div([
            html.P(time_str, style={'fontSize': '0.9em', 'color': '#555', 'margin': '10px 0 5px 0'}),
            html.P(details_msg, style={'fontSize': '1.1em', 'margin': '5px 0 0 0'})
        ], style={'paddingLeft': '45px', 'paddingTop': '10px'})
        
        return html.Details([summary, details_content],
                            className='replan-message-container',
                            id={'type': 'replan-message', 'id': message_id},
                            open=(message_id in open_message_ids))
    
    # If not replanning, determine status based on robot state
    status_key = ''
    details_text = ''
    
    if state == 'carrying':
        status_key = 'on_track'
        pkg_id = next((p['id'] for p in all_packages if p.get('carried_by') == robot_id), "N/A")
        # Extract destination from plan
        plan = robot_data.get('plan', [])
        if plan and len(plan) > 0:
            dest_x, dest_y = plan[-1][0], plan[-1][1]
            details_text = f"Transporting {pkg_id} to Position (X{dest_x:.0f}, Y{dest_y:.0f}). Currently at Position (X{x:.0f}, Y{y:.0f}). {feature_text}".strip()
        else:
            details_text = f"Transporting {pkg_id}. Currently at Position (X{x:.0f}, Y{y:.0f}). {feature_text}".strip()
    
    elif state == 'moving':
        status_key = 'on_track'
        pkg_id = robot_data.get('target_package_id', "package")
        # Extract immediate goal
        goal_x = robot_data.get('immediate_goal_x', x)
        goal_y = robot_data.get('immediate_goal_y', y)
        details_text = f"Moving to acquire {pkg_id} at Position (X{goal_x:.0f}, Y{goal_y:.0f}). {feature_text}".strip()
    
    elif state == 'waiting':
        status_key = 'stationary'
        # For stationary, include time deviation
        time_and_features = []
        if time_status_text:
            time_and_features.append(time_status_text)
        if feature_text:
            time_and_features.append(feature_text)
        
        combined_info = " ".join(time_and_features) if time_and_features else ""
        details_text = f"Robot is awaiting task at Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()
    
    return html.Div([
        html.P(time_str, style={'fontSize': '0.9em', 'color': '#555', 'margin': '0 0 5px 0'}),
        html.Div([
            html.Span(status_map[status_key]['icon'], style={'marginRight': '10px', 'fontSize': '1.5em'}),
            html.Strong(f"{robot_id.title()}: {status_map[status_key]['text']}")
        ], style={'display': 'flex', 'alignItems': 'center', 'fontSize': '1.2em'}),
        html.P(details_text, style={'fontSize': '1.1em', 'margin': '5px 0 0 0'})
    ], style={
        'backgroundColor': status_map[status_key]['color'], 
        'padding': '15px', 
        'borderRadius': '5px',
        'marginBottom': '13px', 
        'border': '1px solid #ddd', 
        'color': '#212529'
    })


# --- App Initialization & Global Data ---
app = dash.Dash(__name__, update_title=None)
server = app.server
static_map_data = load_static_data('static_map_data.json')
initial_figure = create_figure_for_frame(static_map_data, None)
current_frame_data = {}


# --- App Layout ---
app.layout = html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'fontFamily': 'Arial', 'height': '100vh', 'display': 'flex', 'flexDirection': 'column'}, children=[
    html.H1("Multi-Agent Task Planner Simulation", style={'textAlign': 'center', 'padding': '10px 0', 'color': '#00ff88', 'flexShrink': 0}),
    
    html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'gap': '20px', 'padding': '10px', 'backgroundColor': '#2b2b2b', 'borderTop': '2px solid #444', 'borderBottom': '2px solid #444'}, children=[
        html.Div([
            html.Label("Scenario:", style={'marginRight': '10px', 'color': '#00ff88'}),
            dcc.Dropdown(id='scenario-dropdown', options=[{'label': f'Scenario {i}', 'value': i} for i in range(1, 5)], value=1, style={'width': '150px', 'color': 'black', 'display': 'inline-block'})
        ]),
        html.Div([
            html.Button('▶️ Play/Pause', id='play-pause-button', n_clicks=0, style={'marginRight': '10px'}),
            html.Button('🔄 Restart', id='restart-button', n_clicks=0),
        ]),
        html.Div([
            html.Button('Simulator View', id='map-view-btn', n_clicks=0, className='active-view'),
            html.Button('Textual Overview', id='text-view-btn', n_clicks=0),
        ]),
        html.Div([
            html.Button('With Framework', id='with-framework-btn', n_clicks=0, className='active-view'),
            html.Button('Without Framework', id='without-framework-btn', n_clicks=0),
        ]),         
    ]),
    
    html.Div(id='main-content-area', style={'flexGrow': 1, 'overflow': 'hidden', 'padding': '20px'}, children=[
        html.Div(id='map-view-container', style={'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}, children=[
            html.Div(style={'width': '70%', 'height': '100%'}, children=[dcc.Graph(id='simulation-graph', figure=initial_figure, style={'height': '100%', 'width': '100%'})]),
            html.Div(style={'width': '30%', 'height': '100%', 'display': 'flex', 'flexDirection': 'column', 'gap': '10px'}, children=[
                html.H3("Simulation Log", style={'color': '#00ff88', 'textAlign': 'center'}),
                html.Pre(id='text-ui-output', style={'backgroundColor': '#1a1a1a', 'border': '1px solid #666', 'padding': '15px', 'overflowY': 'auto', 'whiteSpace': 'pre-wrap', 'color': '#ddd', 'fontSize': '12px', 'borderRadius': '3px', 'flexGrow': 1})
            ])
        ]),
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
                figure=initial_figure,  # initialize empty or same figure
                config={'staticPlot': True, 'displayModeBar': False},
                style={'width': '300px', 'height': '200px', 'border': '1px solid #666'}
            )
        ]),
    ]),


    dcc.Store(id='open-messages-store', data=[]),
    dcc.Store(id='scenario-data-store'), 
    dcc.Store(id='current-frame-store', data=0),
    dcc.Store(id='is-playing-store', data=False),
    dcc.Store(id='hmm-data-store'),
    dcc.Store(id='framework-mode-store', data='with_framework'),    
    dcc.Interval(id='animation-interval', interval=UPDATE_INTERVAL_MS, n_intervals=0, disabled=True)
])


# --- Callbacks ---
@app.callback(
    Output('scenario-data-store', 'data'),
    Output('current-frame-store', 'data', allow_duplicate=True),
    [Output(f'robot-{i}-timeline', 'max') for i in range(1,4)],
    [Output(f'robot-{i}-timeline', 'marks') for i in range(1,4)],
    Input('scenario-dropdown', 'value'),
    prevent_initial_call='initial_duplicate'
)
def load_data_from_scenario(scenario_id):
    if not scenario_id:
        empty_marks = {0: 'Start', 24: 'Midpoint', 49: 'End'}
        return [], 0, 49, 49, 49, empty_marks, empty_marks, empty_marks


    frames = load_scenario_frames(scenario_id)
    max_frames = len(frames) - 1 if frames else 0
    mid_point = max_frames // 2
    marks = {0: 'Start', mid_point: 'Midpoint', max_frames: 'End'}
    
    return frames, 0, max_frames, max_frames, max_frames, marks, marks, marks


@app.callback(
    Output('is-playing-store', 'data'),
    Output('animation-interval', 'disabled'),
    Input('play-pause-button', 'n_clicks'),
    State('is-playing-store', 'data')
)
def toggle_play_pause(n_clicks, is_playing):
    if n_clicks is None or n_clicks == 0: return False, True
    return not is_playing, is_playing


@app.callback(
    Output('is-playing-store', 'data', allow_duplicate=True),
    Input('current-frame-store', 'data'),
    State('scenario-data-store', 'data'),
    prevent_initial_call=True
)
def auto_pause_at_end(current_frame, scenario_data):
    """Pauses the simulation when it reaches the final frame."""
    if not scenario_data:
        return no_update
        
    max_frames = len(scenario_data) - 1
    if current_frame >= max_frames:
        return False
    return no_update


@app.callback(
    Output('current-frame-store', 'data'),
    [Output(f'robot-{i}-timeline', 'value') for i in range(1,4)],
    Input('animation-interval', 'n_intervals'),
    Input('restart-button', 'n_clicks'),
    State('is-playing-store', 'data'),
    State('current-frame-store', 'data'),
    State('scenario-data-store', 'data')
)
def update_current_frame(n_intervals, n_restarts, is_playing, current_frame, scenario_data):
    ctx = callback_context.triggered_id
    max_frames = len(scenario_data) - 1 if scenario_data else 0
    if ctx == 'restart-button': return 0, 0, 0, 0
    if is_playing and ctx == 'animation-interval':
        if current_frame < max_frames:
            next_frame = current_frame + 1
        else:
            next_frame = max_frames
        return next_frame, next_frame, next_frame, next_frame
    return no_update, no_update, no_update, no_update


@app.callback(
    Output('map-view-container', 'style'),
    Output('text-view-container', 'style'),
    Output('map-view-btn', 'className'),
    Output('text-view-btn', 'className'),
    Input('map-view-btn', 'n_clicks'),
    Input('text-view-btn', 'n_clicks')
)
def switch_view(map_clicks, text_clicks):
    ctx = callback_context.triggered_id
    map_style = {'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}
    text_style = {'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}
    if ctx == 'text-view-btn': return {**map_style, 'display': 'none'}, text_style, '', 'active-view'
    return map_style, {**text_style, 'display': 'none'}, 'active-view', ''


@app.callback(
    Output('with-framework-btn', 'className'),
    Output('without-framework-btn', 'className'),
    Output('framework-mode-store', 'data'),
    Input('with-framework-btn', 'n_clicks'),
    Input('without-framework-btn', 'n_clicks'),
    prevent_initial_call=True
)
def switch_framework_mode(with_clicks, without_clicks):
    """Handles the active state of framework buttons and stores the current mode."""
    triggered_id = callback_context.triggered_id
    if triggered_id == 'without-framework-btn':
        return '', 'active-view', 'without_framework'
    else:
        return 'active-view', '', 'with_framework'


@app.callback(
    [Output(f'robot-{i}-messages', 'children', allow_duplicate=True) for i in range(1, 4)],
    Output('hmm-data-store', 'data'),
    Input('scenario-dropdown', 'value'), 
    Input('restart-button', 'n_clicks'),
    prevent_initial_call='initial_duplicate'
)
def reset_histories_and_load_initial_hmms(scenario_id, n_restarts):
    """
    This callback clears message logs and loads the initial HMM data 
    from the JSON file into the hmm-data-store when a scenario starts.
    """
    cleared_messages = [[] for _ in range(3)]
    
    initial_hmms = {}
    if scenario_id:
        HMM_Robot_1, HMM_Robot_2, HMM_Robot_3 = get_hmms_for_active_scenario(scenario_id)
        initial_hmms = {
            'robot1': HMM_Robot_1,
            'robot2': HMM_Robot_2,
            'robot3': HMM_Robot_3
        }
    return *cleared_messages, initial_hmms


@app.callback(
    Output('simulation-map-snapshot', 'figure'),
    Input('simulation-graph', 'figure')
)
def update_snapshot(main_fig):
    snapshot_fig = go.Figure(main_fig)

    # Scale down markers, lines, and fonts for the smaller view
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
        font=dict(size=8),  # smaller font for axis and annotations
    )
    return snapshot_fig



@app.callback(
    Output('open-messages-store', 'data'),
    Input({'type': 'replan-message', 'id': ALL}, 'open'),
    State('open-messages-store', 'data'),
    prevent_initial_call=True
)
def update_open_messages_state(open_states, current_open_ids):
    """
    This callback updates the list of which replan messages are currently open.
    """
    triggered_id = callback_context.triggered_id
    
    if not isinstance(triggered_id, dict):
        return no_update


    is_open = callback_context.triggered[0]['value']
    message_id = triggered_id['id']


    open_ids_set = set(current_open_ids)


    if is_open:
        open_ids_set.add(message_id)
    else:
        open_ids_set.discard(message_id)


    return list(open_ids_set)


@app.callback(
    Output('simulation-graph', 'figure'),
    Output('text-ui-output', 'children'),
    [Output(f'robot-{i}-messages', 'children') for i in range(1, 4)],
    Output('hmm-data-store', 'data', allow_duplicate=True),
    Output('animation-interval', 'interval'),
    Input('current-frame-store', 'data'),
    State('scenario-dropdown', 'value'),
    State('scenario-data-store', 'data'),
    State('hmm-data-store', 'data'),
    State('framework-mode-store', 'data'),
    [State(f'robot-{i}-messages', 'children') for i in range(1, 4)],
    State('open-messages-store', 'data'),
    prevent_initial_call=True
)
def update_all_outputs(frame_idx, scenario_id, scenario_data, hmm_data, framework_mode, hist1, hist2, hist3, open_message_ids):
    global current_frame_data
    if not all([scenario_data, hmm_data, scenario_id, framework_mode]) or frame_idx is None or frame_idx >= len(scenario_data):
        return initial_figure, "Select a scenario and press Play.", [], [], [], no_update, UPDATE_INTERVAL_MS
    
    current_hmms = hmm_data.copy()
    current_frame_data = scenario_data[frame_idx]
    fig = create_figure_for_frame(static_map_data, current_frame_data)
    mission_time_threshold = THRESHOLD_VALUES[framework_mode][scenario_id]
    robots_dict = current_frame_data.get('robots', {})
    packages = current_frame_data.get('packages', [])
    
    # Build log text
    log_text = f"🎬 Frame: {frame_idx} / {len(scenario_data)-1}\n"
    log_text += f"⏰ Timestamp: {current_frame_data.get('simulator time', 'N/A'):.2f}s\n" + "="*30 + "\n\n"
    log_text += "🤖 ROBOTS:\n" + "-"*20 + "\n"
    if not robots_dict:
        log_text += "(No robot data)\n"
    else:
        for r_id, r_data in robots_dict.items():
            state, x, y = r_data.get('state', '?'), r_data.get('x', 0), r_data.get('y', 0)
            log_text += f"- {r_id}: {state.upper()} @ ({x:.1f}, {y:.1f})\n"
    log_text += "\n📦 PACKAGES:\n" + "-"*20 + "\n"
    if not packages:
        log_text += "(No package data)\n"
    else:
        for p in packages:
            status = f"CARRIED by {p['carried_by']}" if p.get('carried_by') else f"ON GROUND @ ({p.get('x', 0):.1f}, {p.get('y', 0):.1f})"
            log_text += f"- {p['id']}: {status}\n"
    
    histories = [hist1, hist2, hist3]
    new_messages = []
    sim_time = current_frame_data.get('simulator time', 0)
    any_sync_occurred = False
    
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
            selected_robot_rmm_array['robot_time'] = current_frame_data.get('simulator time')
            
            selected_robot_hmm_array = current_hmms.get(robot_id)
            robot_info = {**robots_dict[robot_id], 'id': robot_id}
            
            if selected_robot_hmm_array:
                updated_hmm_array, sync_occurred = dynamic_deviation_threshold_multi_logic(
                    hmm_array=selected_robot_hmm_array,
                    rmm_array=selected_robot_rmm_array,
                    update_logic_functions={},
                    uncertainty_factor_pos=0.1,
                    uncertainty_factor_time=0.1,
                    dynamic_threshold_mission_time=mission_time_threshold,
                    robot_id=robot_id
                )
                
                current_hmms[robot_id] = updated_hmm_array
                
                if sync_occurred:
                    any_sync_occurred = True
                    new_message_div = create_rich_status_message(
                        robot_info, 
                        sim_time, 
                        packages, 
                        open_message_ids,
                        selected_robot_hmm_array,
                        selected_robot_rmm_array,
                        scenario_id
                    )
                    
                    updated_history = [new_message_div]
                    if histories[i-1]:
                        updated_history.append(html.P("--- previous updates ---", className="divider"))
                        updated_history.extend(histories[i-1])
                    new_messages.append(updated_history)
                else:
                    new_messages.append(histories[i-1])
            else:
                new_messages.append(histories[i-1])
        else:
            new_messages.append(histories[i-1])
    
    new_interval = 2000 if any_sync_occurred else UPDATE_INTERVAL_MS
    
    return fig, log_text, *new_messages, current_hmms, new_interval


# --- Main Execution ---
if __name__ == '__main__':
    if not os.path.exists("assets"): os.makedirs("assets")
    with open("assets/style.css", "w") as f:
        f.write("""
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }
#map-view-btn, #text-view-btn, #with-framework-btn, #without-framework-btn { 
    background-color: #555; 
    color: white; 
    border: 1px solid #777; 
    padding: 5px 10px; 
    cursor: pointer; 
}
#map-view-btn.active-view, #text-view-btn.active-view, #with-framework-btn.active-view, #without-framework-btn.active-view { 
    background-color: #007bff; 
    color: white; 
    border-color: #007bff; 
}
.robot-column { display: flex; flex-direction: column; gap: 15px; flex: 1; }
.robot-card-top {
    background-color: #ffffff;
    border: 1px solid #dee2e6;
    border-radius: 0.5rem;
    padding: 10px 20px;
    width: 90%;
    margin-left: auto;
    margin-right: auto;
}
.robot-card-bottom { background-color: #ffffff; border: 1px solid #dee2e6; border-radius: 0.5rem; padding: 15px; display: flex; flex-direction: column; }
.message-box {
    height: 750px;
    overflow-y: auto;
    padding-right: 10px;
}
.divider { text-align: center; color: #aaa; font-size: 0.9em; margin: 15px 0; }
.divider::before, .divider::after { content: ' ― '; }
.robot-card-top .rc-slider-track { background-color: #007bff !important; height: 12px;}
.robot-card-top .rc-slider-rail { background-color: #e9ecef !important; height: 12px;}
.robot-card-top .rc-slider-mark-text { color: #555; font-weight: bold; }
.robot-card-top .rc-slider-disabled .rc-slider-handle { display: none; }
.replan-message-container {
    background-color: #ffdede;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 13px;
    border: 1px solid #ddd;
    color: #212529;
}
.replan-message-container summary {
    cursor: pointer;
    outline: none;
    display: block;
}
.replan-message-container summary::-webkit-details-marker {
  display: none;
}
        """)
    app.run(debug=True, host='0.0.0.0', port=7030)

