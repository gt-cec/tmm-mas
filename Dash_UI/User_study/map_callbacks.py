import dash
from dash import dcc, html, Input, Output, State, callback_context, no_update
from dash.exceptions import PreventUpdate
import json
import time
from datetime import datetime


import copy # <-- 1. ADD THIS IMPORT
import plotly.graph_objects as go
# ... (all other imports)

# ... (other functions)

# --- MAP SNAPSHOT CALLBACK (FIXED LOGIC) ---
def update_snapshot(main_fig, study_state):
    if not study_state or study_state.get('phase') != 'simulation':
        return no_update
    if main_fig is None:
        return go.Figure() # Return empty figure
    
    # 2. THIS IS THE FIXED LINE
    snapshot_fig = copy.deepcopy(go.Figure(main_fig)) 
    
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



# Import modules
import constants
from data_loaders import load_static_data
from ui_components import create_figure_for_frame, create_rich_status_message_data, render_message_component
from utils import create_message_log_entry, get_condition_names

# Try importing the backend logic (required for simulation loop)
try:
    from backend_operations import dynamic_deviation_threshold_multi_logic
except ImportError:
    print("WARNING: Using dummy backend function in map_callbacks.py.")
    def dynamic_deviation_threshold_multi_logic(**kwargs):
        hmm_array = kwargs.get('hmm_array', {})
        rmm_array = kwargs.get('rmm_array', {})
        sync_occurred = rmm_array.get('Replan_flag', False)
        return rmm_array if sync_occurred else hmm_array, sync_occurred


# ... (log_message_clicks, update_simulation_views, update_robot_x_ui functions are unchanged) ...


# --- MAP SNAPSHOT CALLBACK (FIXED LOGIC) ---
def update_snapshot(main_fig, study_state):
    if not study_state or study_state.get('phase') != 'simulation':
        return no_update
    if main_fig is None:
        return go.Figure() # Return empty figure
    # FIX: Use Python's standard copy module instead of the internal dash.copy
    snapshot_fig = copy.deepcopy(go.Figure(main_fig)) # <-- FIXED LINE
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

# ... (log_graph_click function is unchanged) ...


# --- MESSAGE CLICK LOGGING CALLBACK ---
def log_message_clicks(click_data_json_array, interactions, all_message_logs, 
                             open_message_ids, participant_data, study_state, frame_idx):
    
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
            
            # 1. Manage UI open/closed state
            if is_open:
                new_open_message_ids.add(message_id)
            else:
                new_open_message_ids.discard(message_id)

            # 2. Log data ONLY on the first "open" event
            if is_open:
                message_found = False
                for entry in new_all_message_logs:
                    if entry['message_id'] == message_id:
                        message_found = True
                        
                        if entry['clicked'] == 0:
                            
                            click_time_unix = click_info.get('timestamp', time.time() * 1000) / 1000.0
                            click_time_iso = datetime.fromtimestamp(click_time_unix).isoformat()
                            action = "opened"
                            
                            # 2a. Update the message log entry
                            entry['click_timestamp_unix'] = click_time_unix
                            entry['click_timestamp_iso'] = click_time_iso
                            entry['time_to_click_seconds'] = click_time_unix - entry['appear_timestamp_unix']
                            entry['clicked'] = 1
                        
                            # 2b. Log to the simple interaction log
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
                
                if not message_found:
                    print(f"Warning: 'Open' click logged for message_id '{message_id}' but not found in all_message_logs_store.")
        
    except Exception as e:
        print(f"Error logging message click: {e} | Click Data: {click_data_json_array}")
    
    return new_interactions, new_all_message_logs, list(new_open_message_ids)


# --- CORE SIMULATION UPDATE CALLBACK ---
def update_simulation_views(frame_idx, study_state,
                            scenario_data, hmm_data,
                            participant_data, hist1, hist2, hist3,
                            open_message_ids, all_messages_history,
                            message_timestamps, all_message_logs):
    
    if not study_state or study_state.get('phase') != 'simulation':
        return (no_update,) * 14
    
    current_open_message_ids = list(set(open_message_ids)) if open_message_ids else []
    new_message_timestamps = message_timestamps.copy() if message_timestamps else {}
    new_all_message_logs = all_message_logs.copy() if all_message_logs else []
    
    current_run_idx = study_state['current_run_idx']
    current_run_info = participant_data['track'][current_run_idx]
    scenario_num = current_run_info[0]
    condition_idx = current_run_info[1]
    view_type, framework_mode = get_condition_names(condition_idx)
    
    # Placeholder for static data, which needs to be loaded by main script or from a store
    # Since we don't have a static data store here, we rely on the figure creation function
    # which is designed to handle this by taking `static_map_data` which is an import from the context.
    # We must ensure to get a reference to the static data or use a fallback.
    from data_loaders import load_static_data
    static_map_data = load_static_data('static_map_data.json')

    if not all([scenario_data, hmm_data, study_state, participant_data]):
        print("Warning: Missing data in update_simulation_views")
        return (no_update,) * 14
    
    if frame_idx is None or frame_idx >= len(scenario_data):
        # Handle end of simulation frame updates gracefully
        return (no_update,) * 14 # The frame check in control_callbacks handles page transition
    
    current_hmms = hmm_data.copy() if hmm_data else {}
    current_frame_data = scenario_data[frame_idx]
    fig = create_figure_for_frame(static_map_data, current_frame_data)
    
    mission_time_threshold = constants.THRESHOLD_VALUES[framework_mode].get(scenario_num, 1)
    robots_dict = current_frame_data.get('robots', {})
    packages = current_frame_data.get('packages', [])
    
    
    histories = [hist1, hist2, hist3]
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
                    
                    new_message_data, message_type, message_text = create_rich_status_message_data(
                        robot_info,
                        sim_time,
                        packages,
                        selected_robot_hmm_array,
                        selected_robot_rmm_array,
                        scenario_num
                    )
                    
                    is_new_message = False
                    msg_id = new_message_data['message_id']
                    
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
                    
                    # Create the component for the Map UI
                    new_message_div = render_message_component(
                        new_message_data,
                        current_open_message_ids,
                        is_new=is_new_message
                    )
                    
                    newly_generated_messages_for_feed.append(new_message_div)
                    
                    # Update the Text UI *store* with *data*
                    updated_history_data = [new_message_data]
                    current_hist_data = histories[i-1] if isinstance(histories[i-1], list) else ([] if not histories[i-1] else [histories[i-1]])
                    updated_history_data.extend(current_hist_data)
                    
                    new_robot_message_outputs[i-1] = updated_history_data
    
    updated_all_messages = newly_generated_messages_for_feed + (all_messages_history or [])
    updated_all_messages = updated_all_messages[:100]
    
    new_interval = constants.SLOW_INTERVAL_MS if any_sync_occurred and framework_mode == 'with_framework' else constants.UPDATE_INTERVAL_MS
    
    return (
        fig,
        new_robot_message_outputs[0], new_robot_message_outputs[1], new_robot_message_outputs[2],
        frame_idx, frame_idx, frame_idx,
        current_hmms,
        updated_all_messages, updated_all_messages,
        new_interval,
        current_open_message_ids,
        new_message_timestamps,
        new_all_message_logs
    )

# --- TEXT UI RENDERING CALLBACKS (Render Components from Data) ---
def update_robot_1_ui(message_data_list, open_message_ids):
    if not message_data_list:
        return []
    if open_message_ids is None:
        open_message_ids = []
        
    children = []
    children.append(render_message_component(message_data_list[0], open_message_ids, is_new=True))
    
    if len(message_data_list) > 1:
        children.append(html.P("--- previous updates ---", className="divider"))
        for msg_data in message_data_list[1:]:
            children.append(render_message_component(msg_data, open_message_ids, is_new=False))
            
    return children

def update_robot_2_ui(message_data_list, open_message_ids):
    if not message_data_list:
        return []
    if open_message_ids is None:
        open_message_ids = []
        
    children = []
    children.append(render_message_component(message_data_list[0], open_message_ids, is_new=True))
    
    if len(message_data_list) > 1:
        children.append(html.P("--- previous updates ---", className="divider"))
        for msg_data in message_data_list[1:]:
            children.append(render_message_component(msg_data, open_message_ids, is_new=False))
            
    return children

def update_robot_3_ui(message_data_list, open_message_ids):
    if not message_data_list:
        return []
    if open_message_ids is None:
        open_message_ids = []
        
    children = []
    children.append(render_message_component(message_data_list[0], open_message_ids, is_new=True))
    
    if len(message_data_list) > 1:
        children.append(html.P("--- previous updates ---", className="divider"))
        for msg_data in message_data_list[1:]:
            children.append(render_message_component(msg_data, open_message_ids, is_new=False))
            
    return children




# --- GRAPH CLICK LOGGING CALLBACK (UNCHANGED LOGIC) ---
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