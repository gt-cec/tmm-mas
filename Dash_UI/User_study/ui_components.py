import dash
from dash import dcc, html
import plotly.graph_objects as go
from datetime import datetime
import constants
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


# --- Figure and Component Creation ---
def create_figure_for_frame(static_data, frame_data):
    """Generates the main Plotly figure for the simulation."""
    fig = go.Figure()
    
    fig.update_layout(
        xaxis=dict(range=[0, constants.GRID_WIDTH], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False, dtick=10),
        yaxis=dict(range=[0, constants.GRID_HEIGHT], autorange=True, showgrid=True, gridcolor='rgba(100,100,100,0.3)', zeroline=False),
        plot_bgcolor='#ffffff', paper_bgcolor='#ffffff', font=dict(color='black'),
        showlegend=False, margin=dict(l=0, r=0, t=0, b=0), uirevision='constant',
        
        # Quadrant Annotations
        annotations=[
            go.layout.Annotation(
                x=2.5, y=17.5, text="<b>NW</b>", showarrow=False,
                font=dict(size=24, color="rgba(0, 0, 0, 0.20)"),
            ),
            go.layout.Annotation(
                x=17.5, y=17.5, text="<b>NE</b>", showarrow=False,
                font=dict(size=24, color="rgba(0, 0, 0, 0.20)"),
            ),
            go.layout.Annotation(
                x=2.5, y=2.5, text="<b>SW</b>", showarrow=False,
                font=dict(size=24, color="rgba(0, 0, 0, 0.20)"),
            ),
            go.layout.Annotation(
                x=17.5, y=2.5, text="<b>SE</b>", showarrow=False,
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

        if packages:
            pkg_x = []
            pkg_y = []
            pkg_texts = []
            pkg_hovers = []
            pkg_colors = []
            pkg_symbols = []
            robot_pos = {r['id']: (r['x'], r['y']) for r in robots}
            
            for p in packages:
                carried_by_robot = p.get('carried_by')
                is_discovered = p.get('Discovered', 1) == 1 
                is_carried = carried_by_robot is not None and carried_by_robot != "Null"
                is_d_package = p['id'].startswith('d')

                px, py = robot_pos.get(carried_by_robot, (p.get('x', 0), p.get('y', 0)))
                pkg_x.append(px)
                pkg_y.append(py)
                pkg_texts.append(p['id'][-1])

                if is_carried:
                    pkg_colors.append('gold')
                    pkg_symbols.append('square')
                    pkg_hovers.append(f"Package {p['id']}, Carried by {carried_by_robot}")
                
                elif is_d_package:
                    if is_discovered:
                        pkg_colors.append('gold')
                        pkg_symbols.append('triangle-up')
                        pkg_hovers.append(f"Package {p['id']}, On Ground (Discovered 'd' package)")
                    else:
                        pkg_colors.append('lightgreen')
                        pkg_symbols.append('triangle-up')
                        pkg_hovers.append(f"Package {p['id']}, On Ground (Undiscovered)")
                
                elif is_discovered:
                    pkg_colors.append('gold')
                    pkg_symbols.append('square')
                    pkg_hovers.append(f"Package {p['id']}, On Ground (Discovered 'p' package)")
                
                else:
                    pkg_colors.append('lightgreen')
                    pkg_symbols.append('triangle-up')
                    pkg_hovers.append(f"Package {p['id']}, On Ground (Unknown State)")

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
    """
    Computes and returns the data dictionary for a robot status message.
    Used for both Map Log and Text UI message rendering.
    """
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
    scenario_config = constants.SCENARIO_CONFIG.get(scenario_id, {'total_time': 300.0, 'total_steps': 100})
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
    elif state == 'all_tasks_complete':
        status_key = 'on_track'
        details_msg = f"All tasks complete. Robot is at Position (X{x:.0f}, Y{y:.0f}). {feature_text}".strip()
    else:
        status_key = 'stationary'
        details_msg = f"Robot in unknown state '{state}' at Position (X{x:.0f}, Y{y:.0f}). {combined_info}".strip()

    status_info = status_map[status_key]
    
    final_status_text = status_info['text']
    final_status_icon = status_info['icon']
    if state == 'all_tasks_complete':
        final_status_text = 'TASKS COMPLETE'
        final_status_icon = '🎉'

    return {
        'message_id': message_id,
        'robot_id_title': robot_id.title(),
        'status_icon': final_status_icon,
        'status_text': final_status_text,
        'status_class_suffix': status_info['class_suffix'],
        'time_str': time_str,
        'details_msg': details_msg
    }, status_key, details_msg


def render_message_component(message_data, open_message_ids, is_new=False):
    """
    Takes a message_data dict and renders the html.Details component.
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

# --- Study Screen Layouts ---
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

def briefing_screen(run_number, total_runs, scenario_num, view_type, framework_mode):
    view_name = "Simulator View (Map + Log)" if view_type == 'map' else "Textual Overview"
    framework_name = "WITH Communication Framework" if framework_mode == 'with_framework' else "WITHOUT Communication Framework"
    
    scenario_briefing = constants.SCENARIO_CONTENT.get(scenario_num, {}).get('briefing', "No briefing text found for this scenario.")
    
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
    """
    Generates the layout for a single pause-point question.
    question_idx is 0-based (0, 1, or 2).
    """
    question_num = question_idx + 1
    try:
        question_data = constants.SCENARIO_CONTENT[scenario_num]['questions'][question_idx]
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

def create_simulation_layout():
    # Placeholder figure is needed in app.py to initialize, here we define the structure
    # We pass None for the initial figure, and app.py will inject the actual initial_figure
    return html.Div(style={'backgroundColor': '#1e1e1e', 'color': 'white', 'fontFamily': 'Arial', 'height': '100vh', 'display': 'flex', 'flexDirection': 'column'}, children=[
        html.H1("Multi-Agent Task Planner Simulation",
               style={'textAlign': 'center', 'color': '#00ff88', 'flexShrink': 0}),
        html.Div(id='study-context-header', style={'textAlign': 'center', 'padding': '5px', 'backgroundColor': '#2b2b2b', 'borderBottom': '2px solid #444'}),
        html.Div(id='main-content-area', style={'flexGrow': 1, 'overflow': 'hidden', 'padding': '20px'}, children=[
            html.Div(id='simulation-layout-loaded-signal', style={'display': 'none'}),
            
            # MAP VIEW
            html.Div(id='map-view-container', style={'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'height': '100%'}, children=[
                html.Div(style={'width': '70%', 'height': '100%'}, children=[dcc.Graph(id='simulation-graph', figure=go.Figure())]), # Figure is set in app.py's layout
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
                    figure=go.Figure(), # Figure is set in app.py's layout
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