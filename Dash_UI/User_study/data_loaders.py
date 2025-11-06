import json
import os
import glob

# --- HMM Data Loading ---
try:
    with open('all_scenarios_hmm_data.json', 'r') as f:
        ALL_SCENARIOS_HMM_DATA = json.load(f)
except FileNotFoundError:
    print("FATAL ERROR: 'all_scenarios_hmm_data.json' not found.")
    ALL_SCENARIOS_HMM_DATA = {}

def get_hmms_for_active_scenario(scenario_number):
    """Retrieves HMM data for the three robots in the given scenario."""
    scenario_key = f'scenario_{scenario_number}'
    scenario_data = ALL_SCENARIOS_HMM_DATA.get(scenario_key, {})
    return scenario_data.get('HMM_Robot_1'), scenario_data.get('HMM_Robot_2'), scenario_data.get('HMM_Robot_3')

# --- Data Loading ---
def load_static_data(filepath):
    """Loads static map features (walls, zones, nodes, edges) from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Will use data from frame files.")
        return {"walls": [], "zones": [], "nodes": [], "edges": []}

def load_scenario_frames(scenario_id):
    """Loads all frame data for a given scenario ID."""
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