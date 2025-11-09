Here's a complete, production-ready README.md file for your HRI study that covers local installation, development testing, and ngrok production deployment:

```markdown
# HRI Multi-Agent Task Planner Study

This repository contains the Dash application for the Human-Robot Interaction user study on task planning and mental models.

## Project Structure

```
├── updated_user_study.py          # Main Dash application
├── backend_operations.py          # Backend logic for HMM/RMM
├── all_scenarios_hmm_data.json    # HMM data for all scenarios
├── static_map_data.json           # Static map (walls, zones)
├── requirements.txt               # All required Python packages
├── assets/                        # Folder for Dash CSS
├── scenarios_with_graphs/         # Directory containing all frame-by-frame JSON data
└── study_data/                    # Participant data directory (created automatically)
```

---

## 1. Local Installation & Setup

These are **one-time setup steps** required before running the app locally or in production.

### Prerequisites

- Python 3.8 or higher
- pip package manager
- ngrok executable (for production hosting)
- ngrok paid account with reserved domain (for production hosting)

### Installation Steps

```
# 1. Navigate to your project directory
cd /path/to/your-project

# 2. Create a Python virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# 4. Install all required packages
pip install -r requirements.txt

# 5. Verify installation
python3 -c "import dash; import gunicorn; print('Installation successful')"
```

Your virtual environment is now set up. You'll need to activate it (`source venv/bin/activate`) every time you open a new terminal session.

---

## 2. Local Development & Testing

**Use this for development and testing only.** This runs a simple development server suitable for one user at a time.

### Running the Development Server

```
# 1. Navigate to your project directory
cd /path/to/your-project

# 2. Activate the virtual environment
source venv/bin/activate

# 3. Run the development server
python3 updated_user_study.py
```

The app will start on `http://127.0.0.1:9761`

### Accessing the App

Open your web browser and navigate to:
```
http://127.0.0.1:9761
```

### Stopping the Server

Press `Ctrl+C` in the terminal to stop the development server.

---

## 3. Production Deployment (For Prolific Study)

**Use this for the actual study with multiple participants.** This uses gunicorn (production server) and ngrok (public tunnel) to handle concurrent users reliably.

### Prerequisites for Production

1. Complete Section 1 (Local Installation & Setup)
2. Install `screen` if not already available:
   ```
   # Ubuntu/Debian
   sudo apt-get install screen
   
   # CentOS/Fedora
   sudo yum install screen
   
   # Mac (usually pre-installed)
   # If needed: brew install screen
   ```
3. Download ngrok executable from https://ngrok.com/download
4. Have your ngrok authtoken ready (from your paid account)
5. Have your reserved ngrok domain (e.g., `your-stable-hri-domain.ngrok-free.app`)

### One-Time Ngrok Configuration

```
# Navigate to where your ngrok executable is located
cd /path/to/ngrok

# Authenticate ngrok with your authtoken (only needed once)
./ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

### Launching the Production Study

You need **two persistent terminal sessions** running simultaneously. We use `screen` to keep them running even if you disconnect from SSH or close your terminal.

#### Terminal 1: Start the Gunicorn Server

```
# 1. Create a persistent screen session named "study_server"
screen -S study_server

# --- You are now inside the screen session ---

# 2. Navigate to your project directory
cd /path/to/your-project

# 3. Activate the virtual environment
source venv/bin/activate

# 4. Start gunicorn with 4 worker processes
# This binds to localhost:9761 (matching your app configuration)
gunicorn -w 4 -b localhost:9761 --timeout 120 updated_user_study:server

# 5. Detach from the screen session (keeps it running in background)
# Press: Ctrl+A, then press D
```

You'll see gunicorn start with output like:
```
[INFO] Starting gunicorn 20.1.0
[INFO] Listening at: http://127.0.0.1:9761
[INFO] Using worker: sync
[INFO] Booting worker with pid: XXXX
```

#### Terminal 2: Start the Ngrok Tunnel

```
# 1. Create a persistent screen session named "ngrok_tunnel"
screen -S ngrok_tunnel

# --- You are now inside the screen session ---

# 2. Navigate to where your ngrok executable is located
cd /path/to/ngrok

# 3. Start the tunnel using your reserved domain
# Replace 'your-stable-hri-domain' with your actual reserved domain
./ngrok http --domain=your-stable-hri-domain.ngrok-free.app 9761

# 4. Detach from the screen session
# Press: Ctrl+A, then press D
```

You'll see ngrok start with output showing your public URL:
```
Session Status                online
Account                       Your Name (Plan: Paid)
Forwarding                    https://your-stable-hri-domain.ngrok-free.app -> http://localhost:9761
```

### Your Study is Now Live! 🎉

Participants can access your study at:
```
https://your-stable-hri-domain.ngrok-free.app
```

All participant data will be saved to `study_data/` directory on your server.

---

## 4. Managing Production Sessions

### Checking Session Status

To view the gunicorn server logs:
```
screen -r study_server
# Press Ctrl+A, then D to detach again
```

To view the ngrok tunnel status:
```
screen -r ngrok_tunnel
# Press Ctrl+A, then D to detach again
```

### Listing All Screen Sessions

```
screen -ls
```

You should see:
```
There are screens on:
    12345.study_server    (Detached)
    12346.ngrok_tunnel    (Detached)
```

### Stopping the Study

To completely shut down the study:

```
# 1. Stop the gunicorn server
screen -r study_server
# Press Ctrl+C to stop gunicorn
# Type: exit
# Press Enter

# 2. Stop the ngrok tunnel
screen -r ngrok_tunnel
# Press Ctrl+C to stop ngrok
# Type: exit
# Press Enter
```

### Restarting After a Crash

If either process crashes, re-attach to the screen and restart:

```
# For gunicorn
screen -r study_server
cd /path/to/your-project
source venv/bin/activate
gunicorn -w 4 -b localhost:9761 --timeout 120 updated_user_study:server
# Press Ctrl+A, then D

# For ngrok
screen -r ngrok_tunnel
cd /path/to/ngrok
./ngrok http --domain=your-stable-hri-domain.ngrok-free.app 9761
# Press Ctrl+A, then D
```

---

## 5. Data Collection

### Participant Data Location

All study data is saved in:
```
study_data/
├── participant_XXXX_session_YYYY.csv
├── participant_XXXX_session_YYYY.csv
└── ...
```

### Data Backup

It's recommended to periodically back up the `study_data/` directory:

```
# Create a timestamped backup
tar -czf study_data_backup_$(date +%Y%m%d_%H%M%S).tar.gz study_data/

# Or use rsync to sync to another location
rsync -av study_data/ /path/to/backup/location/
```

---

## 6. Troubleshooting

### Port Already in Use

If port 9761 is already in use:
```
# Find what's using the port
lsof -i :9761

# Kill the process (replace PID with actual process ID)
kill -9 PID
```

### Gunicorn Workers Timing Out

If you see timeout errors, increase the timeout value:
```
gunicorn -w 4 -b localhost:9761 --timeout 300 updated_user_study:server
```

### Screen Session Lost

If you lose track of your sessions:
```
# List all sessions
screen -ls

# Reattach to a specific session
screen -r study_server

# Force reattach if session shows as "Attached"
screen -d -r study_server
```

### Ngrok Tunnel Disconnected

If ngrok disconnects (rare with paid plans):
```
# Reattach to the ngrok screen
screen -r ngrok_tunnel

# Restart ngrok
./ngrok http --domain=your-stable-hri-domain.ngrok-free.app 9761
```

### Checking if Everything is Running

```
# Check if gunicorn is running
ps aux | grep gunicorn

# Check if ngrok is running
ps aux | grep ngrok

# Check if port 9761 is listening
netstat -tuln | grep 9761
```

---

## 7. Production Best Practices

1. **Monitor disk space** - Participant data can accumulate quickly
   ```
   df -h
   ```

2. **Set up log rotation** - Prevent log files from consuming too much space

3. **Test thoroughly** - Run through the entire study flow locally before going live

4. **Have a backup plan** - Know how to quickly restart services if needed

5. **Monitor participant progress** - Periodically check that data is being saved correctly

6. **Keep the URL stable** - Using a reserved ngrok domain ensures participants always use the same URL

---

## 8. Quick Reference Commands

### Local Development
```
cd /path/to/your-project
source venv/bin/activate
python3 updated_user_study.py
```

### Production Launch
```
# Terminal 1
screen -S study_server
cd /path/to/your-project && source venv/bin/activate
gunicorn -w 4 -b localhost:9761 --timeout 120 updated_user_study:server
# Ctrl+A, D

# Terminal 2
screen -S ngrok_tunnel
cd /path/to/ngrok
./ngrok http --domain=your-stable-hri-domain.ngrok-free.app 9761
# Ctrl+A, D
```

### Check Status
```
screen -ls
screen -r study_server  # View server logs
screen -r ngrok_tunnel  # View tunnel status
```

### Stop Everything
```
screen -r study_server  # Ctrl+C, then exit
screen -r ngrok_tunnel  # Ctrl+C, then exit
```

---

## Support

For Dash-specific issues, consult the [Dash documentation](https://dash.plotly.com/).

For deployment issues, refer to the [Gunicorn documentation](https://docs.gunicorn.org/).

For tunneling issues, refer to the [ngrok documentation](https://ngrok.com/docs).
```

This complete README provides everything you need from initial setup through production deployment and monitoring. You can copy and paste this entire file as your `README.md`.[2][5][7][10]

[1](https://stackoverflow.com/questions/67138641/not-able-to-deploy-dash-application-on-gunicorn)
[2](https://github.com/plotly/dash/issues/85)
[3](https://www.linode.com/docs/guides/using-gnu-screen-to-manage-persistent-terminal-sessions/)
[4](https://cat.pdx.edu/platforms/linux/remote-access/persistent-screen/)
[5](https://community.plotly.com/t/deploying-dash-app-to-aws-server-using-gunicorn/81009)
[6](https://fizzy.cc/deploy-dash-on-server/)
[7](https://community.plotly.com/t/dash-plotly-in-production-with-nginx-gunicorn/82863)
[8](https://www.outrightcrm.com/blog/ngrok-securely-share-localhost/)
[9](https://explainerdashboard.readthedocs.io/en/latest/deployment.html)
[10](https://instatunnel.my/blog/bypassing-the-ngrok-2-hour-limit-a-comprehensive-guide-featuring-instatunnelmy)