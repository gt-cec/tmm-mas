import { renderMapRobotStatus, renderMapRobotAlert} from './newInfoPanel.js';
import { initPixiMap, mapHeight, cellWidth, cellHeight } from './newPixiApp.js';
import { loadRobotImage, updateRobotsOnMap, activeRobotID } from './newRobotManager.js';
import { createSocket } from './newSocket.js';
import { onFileReceived, renderRobotStatus1, renderRobotAlert1 } from './newText.js';
import { robotAlerts, renderRobotSpecificAlerts } from './newInfoPanel.js';

let socket = null;
let app = initPixiMap();

loadRobotImage().then(() => {
  socket = createSocket(processAndSendData);
})

function processAndSendData(data) {
  const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  updateRobotsOnMap(app, data.robots, cellWidth, cellHeight, mapHeight);
  renderMapRobotStatus(data.robots);
  renderRobotStatus1(data.robots);
  Object.entries(data.robots).forEach(([id, robot]) => {
    if (robot.message.length > 0) {
      const alertData = {
        time: currentTime,
        robotName: `Robot ${id}`,
        status: getRobotStatus(robot.message),
        message: robot.message,
        robotId: id
      };
      renderMapRobotAlert(alertData);
      renderRobotAlert1(alertData);
      if (!robotAlerts[id]) robotAlerts[id] = [];
      robotAlerts[id].unshift(alertData);
      if (robotAlerts[id].length > 2) robotAlerts[id].pop();
      if (activeRobotID && activeRobotID == id) {
        renderRobotSpecificAlerts(id);
      }
    }
  });
  Object.keys(data.robots).forEach(robotId => onFileReceived(`bar${robotId}`));
}

function getRobotStatus(message) {
  if (message.includes("replanning")) return "Replanning";
  if (message.includes("behind")) return "Delay";
  return "On Track";
}

let isPlaying = false;
const playStopButton = document.getElementById('playStopButton');
playStopButton.addEventListener("click", () => {
  if (!socket) return;
  isPlaying = !isPlaying;
  playStopButton.textContent = isPlaying ? 'Stop' : 'Play';
  socket.send(isPlaying);
})

const toggleScreenButton = document.getElementById('toggleScreenButton');
const toggleLabelSimulator = document.getElementById('toggleLabelSimulator');
const toggleLabelTextual = document.getElementById('toggleLabelTextual');
const simulatorScreen = document.getElementById('simulatorScreen');
const overviewScreen = document.getElementById('overviewScreen');

toggleScreenButton.addEventListener("click", function () {
  onToggle(this.checked);
})

function onToggle(isChecked) {
  toggleLabelSimulator.classList.toggle('text-white', !isChecked);
  toggleLabelSimulator.classList.toggle('text-gray-400', isChecked);
  toggleLabelTextual.classList.toggle('text-white', isChecked);
  toggleLabelTextual.classList.toggle('text-gray-400', !isChecked);
  simulatorScreen.classList.toggle('hidden', isChecked);
  overviewScreen.classList.toggle('hidden', !isChecked);
}