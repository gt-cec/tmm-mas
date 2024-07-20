from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# pull the index page
@app.route('/')
def index():
    return render_template('index.html')

# get an image via SocketIO, this could be from another process (the sim) or replaced by the feed from the sim
# run python send_image.py to send an email (the CEC logo)
@socketio.on('cam')
def handle_image(data):
    # send to all clients
    emit("sim_stream", {"image": data["image"]}, broadcast=True)  # data["image"] is a Base64 encoded image
    return

# start the server
if __name__ == '__main__':
    socketio.run(app, debug=True)
