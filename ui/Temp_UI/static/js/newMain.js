import { initPixiApp, widthSize, heightSize, width, height } from './newPixiApp.js';
import { loadRobotTexture, updateRobots } from './newRobotManager.js';
import { createSocket } from './newSocket.js';
import { renderRobotStatus, renderPlaceholderRobots, renderRobotAlert} from './newInfoPanel.js';

let socket = null;
let app = initPixiApp();
renderPlaceholderRobots();
renderRobotAlert({
  time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
  robotName: "Robot 1",
  status: "Replanning",
  message: "Robot has replanned 5 times in the last minute, suggesting a persistent blockage."
});


loadRobotTexture().then(() => {
  socket = createSocket((data) => {
    updateRobots(app, data.robots, widthSize, heightSize, width, height);
    renderRobotStatus(data.robots);
    console.log(data.robots[3].message);
  });
});

let isPlaying = false;
const playStopButton = document.getElementById('playStopButton');
playStopButton.addEventListener("click", () => {
  if (!socket) return;
  isPlaying = !isPlaying;
  playStopButton.textContent = isPlaying ? 'Stop' : 'Play';
  socket.send(isPlaying);
})

const toggleScreenButton = document.getElementById('toggleScreenButton');
const simToggleText = document.getElementById('simToggleText');
const textToggleText = document.getElementById('textToggleText');
const simView = document.getElementById('simulatorView');
const textualView = document.getElementById('textualView');

toggleScreenButton.addEventListener("click", function () {
  const isChecked = this.checked;
  simToggleText.classList.toggle('text-white', !isChecked);
  simToggleText.classList.toggle('text-gray-400', isChecked);
  textToggleText.classList.toggle('text-white', isChecked);
  textToggleText.classList.toggle('text-gray-400', !isChecked);
  simView.classList.toggle('hidden', isChecked);
  textualView.classList.toggle('hidden', !isChecked);
});