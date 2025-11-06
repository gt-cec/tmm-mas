import dash
from dash import dcc, html, Input, Output, State
from dash.dependencies import ALL
from dash.exceptions import PreventUpdate
import os
import time

# Import all modules
import constants
from ui_components import welcome_screen, thank_you_screen
from data_loaders import load_static_data
from map_callbacks import (
    update_simulation_views,
    log_message_clicks,
    update_robot_1_ui,
    update_robot_2_ui,
    update_robot_3_ui,
    update_snapshot,
    log_graph_click
)
from control_callbacks import (
    start_study,
    begin_scenario,
    load_data_and_start_simulation,
    control_animation,
    programmatically_switch_view,
    update_frame_and_check_pause,
    submit_pause_question,
    submit_post_scenario_questions,
    submit_final_questionnaire
)


# --- App Initialization ---
app = dash.Dash(__name__, update_title=None, suppress_callback_exceptions=True)
server = app.server

# Load initial static data for the placeholder figure
static_map_data = load_static_data('static_map_data.json')
# Need to import and use the function from ui_components
from ui_components import create_figure_for_frame
initial_figure = create_figure_for_frame(static_map_data, None)

# --- App Layout (MODIFIED to reference initial_figure) ---
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
    
    # Stores for Text UI
    dcc.Store(id='robot-1-messages-store', data=[]),
    dcc.Store(id='robot-2-messages-store', data=[]),
    dcc.Store(id='robot-3-messages-store', data=[]),
    
    # Store for Comprehensive Message Logging
    dcc.Store(id='all-message-logs-store', data=[]),
    
    # Hidden div to capture message clicks
    html.Div(id='message-click-relay', style={'display': 'none'}),
    
    # Intervals
    dcc.Interval(id='animation-interval', interval=constants.UPDATE_INTERVAL_MS, n_intervals=0, disabled=True),
    dcc.Interval(id='click-logger-interval', interval=constants.CLICK_POLL_INTERVAL_MS, n_intervals=0, disabled=True) 
])

# --- Clientside Callback for Message Clicks ---
# Copied directly from original file to maintain functionality
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
    Input('click-logger-interval', 'n_intervals')
)

# --- Attach all callbacks ---

# Callbacks for Flow Control
app.callback(
    Output('page-content', 'children'), Output('participant-store', 'data'),
    Output('study-state-store', 'data'), Output('name-error', 'children'),
    Input('start-study-btn', 'n_clicks'), State('participant-name-input', 'value'),
    prevent_initial_call=True
)(start_study)

app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
    Input('begin-scenario-btn', 'n_clicks'),
    State('study-state-store', 'data'), State('participant-store', 'data'),
    prevent_initial_call=True
)(begin_scenario)

app.callback(
    Output('scenario-data-store', 'data'), Output('hmm-data-store', 'data'),
    Output('current-frame-store', 'data', allow_duplicate=True),
    Output('robot-1-timeline', 'max'), Output('robot-2-timeline', 'max'),
    Output('robot-3-timeline', 'max'), Output('robot-1-timeline', 'marks'),
    Output('robot-2-timeline', 'marks'), Output('robot-3-timeline', 'marks'),
    Output('all-messages-store', 'data', allow_duplicate=True),
    Output('open-messages-store', 'data', allow_duplicate=True),
    Output('message-timestamps-store', 'data', allow_duplicate=True),
    Output('robot-1-messages-store', 'data', allow_duplicate=True),
    Output('robot-2-messages-store', 'data', allow_duplicate=True),
    Output('robot-3-messages-store', 'data', allow_duplicate=True),
    Input('simulation-layout-loaded-signal', 'children'),
    State('study-state-store', 'data'), State('participant-store', 'data'),
    prevent_initial_call=True
)(load_data_and_start_simulation)

app.callback(
    Output('animation-interval', 'disabled'), Output('click-logger-interval', 'disabled'),
    Input('study-state-store', 'data'),
)(control_animation)

app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Output('responses-store', 'data', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
    Input('submit-pause-question-btn', 'n_clicks'),
    State('study-state-store', 'data'), State('participant-store', 'data'),
    State('responses-store', 'data'), State('pause-question-radio', 'value'),
    prevent_initial_call=True
)(submit_pause_question)

app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Output('responses-store', 'data', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
    Input('submit-post-scenario-btn', 'n_clicks'),
    State('study-state-store', 'data'), State('participant-store', 'data'),
    State('responses-store', 'data'),
    State({'type': 'post-scenario-question', 'id': ALL}, 'value'),
    State({'type': 'post-scenario-question', 'id': ALL}, 'id'),
    State('interaction-log-store', 'data'), State('all-message-logs-store', 'data'),
    prevent_initial_call=True
)(submit_post_scenario_questions)

app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('submit-final-btn', 'n_clicks'),
    State('participant-store', 'data'), State('study-state-store', 'data'),
    State('responses-store', 'data'), State('interaction-log-store', 'data'),
    State('all-message-logs-store', 'data'),
    State({'type': 'post-study-question', 'id': ALL}, 'value'),
    State({'type': 'post-study-question', 'id': ALL}, 'id'),
    prevent_initial_call=True
)(submit_final_questionnaire)

# Callbacks for Map/Text View and Animation
app.callback(
    Output('map-view-container', 'style'), Output('text-view-container', 'style'),
    Output('study-context-header', 'children'),
    Input('study-state-store', 'data'), State('participant-store', 'data'),
)(programmatically_switch_view)

app.callback(
    Output('current-frame-store', 'data', allow_duplicate=True),
    Output('page-content', 'children', allow_duplicate=True),
    Output('study-state-store', 'data', allow_duplicate=True),
    Input('animation-interval', 'n_intervals'),
    State('current-frame-store', 'data'), State('scenario-data-store', 'data'),
    State('study-state-store', 'data'), State('participant-store', 'data'),
    prevent_initial_call=True
)(update_frame_and_check_pause)

app.callback(
    Output('simulation-graph', 'figure'),
    Output('robot-1-messages-store', 'data', allow_duplicate=True),
    Output('robot-2-messages-store', 'data', allow_duplicate=True),
    Output('robot-3-messages-store', 'data', allow_duplicate=True),
    Output('robot-1-timeline', 'value'), Output('robot-2-timeline', 'value'),
    Output('robot-3-timeline', 'value'),
    Output('hmm-data-store', 'data', allow_duplicate=True),
    Output('all-messages-feed', 'children'),
    Output('all-messages-store', 'data', allow_duplicate=True),
    Output('animation-interval', 'interval'),
    Output('open-messages-store', 'data', allow_duplicate=True),
    Output('message-timestamps-store', 'data', allow_duplicate=True),
    Output('all-message-logs-store', 'data', allow_duplicate=True),
    Input('current-frame-store', 'data'), Input('study-state-store', 'data'),
    State('scenario-data-store', 'data'), State('hmm-data-store', 'data'),
    State('participant-store', 'data'),
    [State(f'robot-{i}-messages-store', 'data') for i in range(1, 4)],
    State('open-messages-store', 'data'), State('all-messages-store', 'data'),
    State('message-timestamps-store', 'data'), State('all-message-logs-store', 'data'),
    prevent_initial_call=True
)(update_simulation_views)

# Callbacks for Interaction Logging
app.callback(
    Output('interaction-log-store', 'data', allow_duplicate=True),
    Output('all-message-logs-store', 'data', allow_duplicate=True),
    Output('open-messages-store', 'data', allow_duplicate=True),
    Input('message-click-relay', 'children'),
    State('interaction-log-store', 'data'), State('all-message-logs-store', 'data'),
    State('open-messages-store', 'data'), State('participant-store', 'data'),
    State('study-state-store', 'data'), State('current-frame-store', 'data'),
    prevent_initial_call=True
)(log_message_clicks)

app.callback(
    Output('interaction-log-store', 'data', allow_duplicate=True),
    Input('simulation-graph', 'clickData'),
    State('interaction-log-store', 'data'), State('participant-store', 'data'),
    State('study-state-store', 'data'), State('current-frame-store', 'data'),
    prevent_initial_call=True
)(log_graph_click)


# Callbacks to Render Text UI from Stores
app.callback(
    Output('robot-1-messages', 'children'), Input('robot-1-messages-store', 'data'),
    State('open-messages-store', 'data')
)(update_robot_1_ui)

app.callback(
    Output('robot-2-messages', 'children'), Input('robot-2-messages-store', 'data'),
    State('open-messages-store', 'data')
)(update_robot_2_ui)

app.callback(
    Output('robot-3-messages', 'children'), Input('robot-3-messages-store', 'data'),
    State('open-messages-store', 'data')
)(update_robot_3_ui)

app.callback(
    Output('simulation-map-snapshot', 'figure'),
    Input('simulation-graph', 'figure'),
    Input('study-state-store', 'data')
)(update_snapshot)


# --- Main Execution ---
if __name__ == '__main__':
    if not os.path.exists("assets"):
        os.makedirs("assets")
    
    # Save the CSS content
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
    
    # Use debug=False for actual study deployment
    app.run(debug=False, host='0.0.0.0', port=9214)