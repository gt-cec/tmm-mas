

-----

````md
# HRI Multi-Agent Task Planner Study

This repository contains the Dash application for the Human-Robot Interaction user study on task planning and mental models.

## Project Structure

* `updated_user_study.py` - Main Dash application
* `backend_operations.py` - Backend logic for HMM/RMM
* `all_scenarios_hmm_data.json` - HMM data for all scenarios
* `static_map_data.json` - Static map (walls, zones)
* `requirements.txt` - All required Python packages
* `assets/` - Folder for Dash CSS
* `scenarios_with_graphs/` - Directory containing all frame-by-frame JSON data

---

## 1. Local Installation & Testing
**(For Development / Testing Only)**

These steps allow you to run the app on your local machine for testing. This uses a simple development server and is **not** suitable for the real study.

### Setup
```bash
# 1. Go to your project directory
cd /path/to/your-project

# 2. Create a Python virtual environment
python3 -m venv venv

# 3. Activate the environment
source venv/bin/activate

# 4. Install all required packages
pip install -r requirements.txt
````

### Run for Local Testing

```bash
# 1. Make sure your virtual environment is active
source venv/bin/activate

# 2. Run the app using the simple development server
python3 user_study.py

# 3. Open your web browser and go to:
#    [http://127.0.0.1:8033](http://127.0.0.1:9761)
```

To stop the server, just press `Ctrl+C` in your terminal.

-----

## 2\. Production Hosting (for Prolific Study)

**(For the Real Study / Multiple Participants)**

These steps use a robust server (`gunicorn`) and a public tunnel (`ngrok`) to handle all your study participants.

### One-Time Setup

  * Follow **Section 1 (Local Installation & Setup)** one time to install all the requirements.
  * Make sure you have your `ngrok` executable and your paid authtoken.

### Launching the Study

This requires two separate, persistent terminal sessions. We use `screen` to ensure the app and tunnel keep running even after you log out.

#### Terminal 1: Run the Gunicorn Server (The "Bus")

```bash
# 1. Start a persistent session named "server"
screen -S study_server

# --- You are now in a new screen session ---

# 2. Activate the environment
cd /path/to/your-project
source venv/bin/activate

# 3. Start Gunicorn (the production server)
# This binds to port 9761, which your app is set to
gunicorn -w 4 -b localhost:9761 updated_user_study:server

# 4. Detach from the session (it will keep running)
#    Press: Ctrl+A , then press d
```

#### Terminal 2: Run the ngrok Tunnel (The "Tunnel")

```bash
# 1. Start a persistent session named "tunnel"
screen -S ngrok_tunnel

# --- You are now in a new screen session ---

# 2. Navigate to where your ngrok executable is
cd /path/to/ngrok

# 3. Start the tunnel, pointing to your app and using your reserved domain
./ngrok http --domain=your-stable-hri-domain.ngrok.io 9761

# 4. Detach from the session
#    Press: Ctrl+A , then press d
```

Your study is now **LIVE** at `https://your-stable-hri-domain.ngrok.io`. All data will be saved to the `study_data/` directory on this machine.

### 3\. Monitoring and Stopping

  * **To check the app logs:** `screen -r study_server`
  * **To check the ngrok status:** `screen -r ngrok_tunnel`
  * **To stop the study:** Re-attach to each screen (`screen -r ...`) and press `Ctrl+C` to stop the process, then type `exit`.

<!-- end list -->

```
```


