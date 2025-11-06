from dash import dcc, html, Input, Output, State, no_update
from dash.dependencies import ALL
from dash.exceptions import PreventUpdate
from datetime import datetime
from filelock import FileLock
import os

# Import modules
import constants
from data_loaders import load_scenario_frames, get_hmms_for_active_scenario
from ui_components import briefing_screen, create_simulation_layout, create_pause_question_screen, create_post_scenario_questionnaire, post_study_questionnaire, thank_you_screen
from utils import generate_participant_id, get_condition_names, save_study_data, save_message_logs


# --- START/END STUDY FLOW ---
def start_study(n_clicks, name):
    if not name or len(name.strip()) < 2:
        return no_update, no_update, no_update, "Please enter your full name."
    
    os.makedirs('study_data', exist_ok=True)
    lock = FileLock(constants.PARTICIPANT_COUNT_LOCK, timeout=10)
    try:
        with lock:
            try:
                with open(constants.PARTICIPANT_COUNT_FILE, 'r') as f:
                    current_count = int(f.read().strip())
            except (FileNotFoundError, ValueError):
                current_count = 0
            
            track_idx = current_count % len(constants.STUDY_DESIGN_TABLE)
            assigned_track = constants.STUDY_DESIGN_TABLE[track_idx]
            
            with open(constants.PARTICIPANT_COUNT_FILE, 'w') as f:
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
        'phase': 'briefing',
        'segment_start_time': None
    }
    
    first_run_info = assigned_track[0]
    scenario_num = first_run_info[0]
    condition_idx = first_run_info[1]
    view_type, framework_mode = get_condition_names(condition_idx)
    total_runs = len(assigned_track)
    
    return briefing_screen(1, total_runs, scenario_num, view_type, framework_mode), participant_data, study_state, ""

def begin_scenario(n_clicks, study_state, participant_data):
    if n_clicks == 0 or not study_state or not participant_data:
        raise PreventUpdate
    new_study_state = study_state.copy()
    new_study_state['phase'] = 'simulation'
    new_study_state['segment_start_time'] = datetime.now().isoformat()
    return create_simulation_layout(), new_study_state

def load_data_and_start_simulation(layout_signal, study_state, participant_data):
    if not study_state or not participant_data or study_state.get('phase') != 'simulation':
        raise PreventUpdate
    print("load_data_and_start_simulation firing...")
    
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    
    frames = load_scenario_frames(scenario_num)
    HMM_R1, HMM_R2, HMM_R3 = get_hmms_for_active_scenario(scenario_num)
    hmms = {'robot1': HMM_R1, 'robot2': HMM_R2, 'robot3': HMM_R3}
    
    start_frame = 0
    pause_points = constants.PAUSE_POINTS.get(scenario_num, [])
    if study_state['current_question_idx'] > 0:
        start_frame = pause_points[study_state['current_question_idx'] - 1] + 1
    
    max_frames = len(frames) - 1 if frames else 0
    mid_point = max_frames // 2
    marks = {0: 'Start', mid_point: 'Midpoint', max_frames: 'End'}
    
    # Return 14 values: frames, hmms, start_frame (x1), max_frames (x3), marks (x3), 
    # clear all messages/timestamps (x5)
    return (
        frames, hmms, start_frame, 
        max_frames, max_frames, max_frames, 
        marks, marks, marks, 
        [], [], {}, # all_messages_store, open_messages_store, message_timestamps_store
        [], [], [] # robot-x-messages-store (data)
    )

def control_animation(study_state):
    if study_state and study_state.get('phase') == 'simulation':
        return False, False
    return True, True

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

# --- SIMULATION AND PAUSE POINTS ---
def update_frame_and_check_pause(n_intervals, current_frame, scenario_data, study_state, participant_data):
    if not study_state or study_state.get('phase') != 'simulation' or not participant_data or not scenario_data:
        raise PreventUpdate
    
    max_frames = len(scenario_data) - 1
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    total_runs = len(participant_data['track'])
    
    # Check for end of simulation FIRST
    if current_frame >= max_frames:
        new_state = study_state.copy()
        new_state['phase'] = 'post_scenario_questions'
        print("Reached end of frames. Moving to Post-Scenario Questionnaire.")
        new_page = create_post_scenario_questionnaire(scenario_num, current_run_idx + 1, total_runs)
        return no_update, new_page, new_state

    # Check for pause points
    pause_points = constants.PAUSE_POINTS.get(scenario_num, [])
    current_question_idx = study_state['current_question_idx']
    
    if current_question_idx < len(pause_points):
        current_pause_point = pause_points[current_question_idx]
        if current_frame == current_pause_point:
            # PAUSE!
            new_study_state = study_state.copy()
            new_study_state['phase'] = 'questions'
            print(f"Pausing at frame {current_frame} for question set {current_question_idx + 1}")
            new_page = create_pause_question_screen(scenario_num, current_question_idx)
            return no_update, new_page, new_study_state
    
    # No pause, just advance the frame
    next_frame = current_frame + 1
    return next_frame, no_update, no_update

# --- QUESTIONNAIRE SUBMISSION ---
def submit_pause_question(n_clicks, study_state, participant_data, responses, answer_value):
    if n_clicks == 0 or not study_state or not participant_data or not answer_value:
        return no_update, no_update, no_update
    
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    condition_idx = current_run_info[1]
    question_idx = study_state['current_question_idx']
    
    try:
        question_text = constants.SCENARIO_CONTENT[scenario_num]['questions'][question_idx]['text']
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
    
    print(f"Logged pause question {question_idx + 1}. Resuming simulation.")
    
    return create_simulation_layout(), new_responses, new_study_state

def submit_post_scenario_questions(n_clicks, study_state, participant_data, responses, q_values, q_ids, interactions, all_message_logs):
    if n_clicks == 0 or not study_state or not participant_data:
        raise PreventUpdate
        
    if not all(q_values):
        print("User tried to submit post-scenario questions without answering all.")
        return no_update, no_update, no_update

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
        print(f"Incrementally saving data for {participant_data.get('id')} after Run {current_run_idx + 1}.")
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
        
        print(f"Moving to briefing for Run {next_run_idx + 1}")
        
        return briefing_screen(next_run_idx + 1, total_runs, next_scenario_num, next_view_type, next_framework), new_responses, new_study_state
    else:
        new_study_state['phase'] = 'post_study'
        print("All runs complete. Moving to Post-Study Questionnaire.")
        return post_study_questionnaire(), new_responses, new_study_state

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
        save_study_data(participant_data, final_responses, interactions)
        save_message_logs(participant_data, all_message_logs, study_state)
    except Exception as e:
        print(f"Error during final save: {e}")

    return thank_you_screen()