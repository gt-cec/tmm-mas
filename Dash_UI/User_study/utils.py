from datetime import datetime
import hashlib
import csv
import os
import json
from filelock import FileLock
import constants

# --- HELPER FUNCTION ---
def get_condition_names(condition_idx):
    """Translates a condition index (0-3) into names."""
    view_type = 'map' if condition_idx < 2 else 'text'
    framework_mode = 'with_framework' if condition_idx % 2 == 0 else 'without_framework'
    return view_type, framework_mode

def generate_participant_id(name):
    """Generates a unique participant ID based on name and timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    name_hash = hashlib.md5(name.encode()).hexdigest()[:6]
    return f"P{timestamp}_{name_hash}"

# --- Message Log Creation Function ---
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

# --- Message Log Saving Function ---
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
            fieldnames = [
                'message_id', 'participant_id', 'scenario', 'condition', 'run_number',
                'frame', 'sim_time', 'robot_id', 'robot_state', 'robot_x', 'robot_y',
                'message_type', 'message_text', 
                'appear_timestamp_iso',
                'clicked',
                'click_timestamp_iso', 
                'time_to_click_seconds', 
            ]

            existing_fieldnames = [fn for fn in fieldnames if fn in all_message_logs[0]]
            
            writer = csv.DictWriter(f, fieldnames=existing_fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(all_message_logs)
        print(f"Saved {len(all_message_logs)} message log entries for {participant_id}")

# --- Data Saving Function ---
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
    
    # --- CSV logic for POST-SCENARIO questions ---
    csv_file = 'study_data/master_post_scenario_responses.csv'
    file_exists = os.path.isfile(csv_file)
    
    post_scenario_responses = [r for r in responses if r.get('type') == 'post_scenario']
    
    if not post_scenario_responses:
        print("No post-scenario responses to save to CSV yet.")
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