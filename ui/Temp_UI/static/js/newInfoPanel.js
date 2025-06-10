export function renderMapRobotStatus(robots) {
  const robotEntries = Object.values(robots);
  const panelContainer = document.getElementById('simulatorRobotStatusContainer');
  const robotCards = panelContainer.getElementsByClassName('simulatorRobotStatus');

  robotEntries.forEach(({ jsonX, jsonY, message }, index) => {
    const card = robotCards[index];
    const robotID = card.querySelector('.robotName');
    robotID.textContent =  `Robot ${index + 1}: (X${jsonX}, Y${jsonY})`;

    const statusText = card.querySelector('.robotStatusText');
    const commonStyle = "robotStatusText text-white text-sm px-3 py-1 rounded-full";
    if (message && message.includes("behind")) {
      statusText.textContent = "Delay";
      statusText.className = `${commonStyle} bg-blue-500`;
    } else if (message && message.includes("replanning")) {
      statusText.textContent = "Replanning";
      statusText.className = `${commonStyle} bg-red-500`;
    } else {
      statusText.textContent = "On Track";
      statusText.className = `${commonStyle} bg-green-500`;
    }
  });
}

let alertSlots = [];

const statusImgMapping = {
  "Replanning": "/static/img/replanning.png",
  "Delay": "/static/img/delay.png",
  "On Track": "/static/img/ontrack.png",
};

const statusBgMapping = {
  "Replanning": "bg-red-100",
  "Delay": "bg-blue-100",
  "On Track": "bg-green-100",
};

function cleanMessage(message) {
  return (message || "").replace(/^["']|["']$/g, '');
}

function updateAlertSlot(alertSlot, alert) {
  const alertSlotCard = alertSlot.getElementsByClassName(`alertBox`)[0];
  alertSlot.style.display = 'block';

  Object.values(statusBgMapping).forEach(bg => alertSlotCard.classList.remove(bg));
  alertSlotCard.classList.add(alert.bgColor);

  alertSlot.querySelector('.alertTime').textContent = alert.time;
  alertSlotCard.querySelector('.alertStatus').innerHTML = alert.status;
  alertSlotCard.querySelector('.alertMessage').textContent = alert.message;
  alertSlotCard.querySelector('.alertStatusIcon').src = alert.image;

  alert.isNew = false;
}

export function renderMapRobotAlert({ time, robotName, status, message }) {
  const prevUpdateContainer = document.getElementById('simulatorPrevUpdateContainer');
  prevUpdateContainer.classList.remove('hidden');
  const reformattedMessage = cleanMessage(message);
  alertSlots.unshift({
    time,
    status: `${robotName}: <span class="font-bold">${status}</span>`,
    message: reformattedMessage,
    image: statusImgMapping[status],
    isNew: true,
    bgColor: statusBgMapping[status]
  });

  if (alertSlots.length > 2) {
    alertSlots.pop();
  }

  alertSlots.forEach((alert, index) => {
    const alertSlot = document.getElementById(`simulatorRobotAlert${index + 1}`);
    if (alertSlot) {
      updateAlertSlot(alertSlot, alert);
    }
  });
}

export const robotAlerts = {};

export function renderRobotSpecificAlerts(robotId) {
  const header = document.getElementById('robotSpecificHeader');
  header.textContent = `Robot ${robotId} Updates`;
  header.classList.remove('hidden');
  const alerts = robotAlerts[robotId] || [];
  for (let i = 0; i < 2; i++) {
    const alertSlot = document.getElementById(`robotSpecificAlert${i + 1}`);
    if (alerts[i]) {
      const alert = alerts[i];
      const alertBox = alertSlot.querySelector('.alertBox');
      alertSlot.classList.remove('hidden');

      Object.values(statusBgMapping).forEach(bg => alertBox.classList.remove(bg));
      alertBox.classList.add(statusBgMapping[alert.status]);

      alertSlot.querySelector('.alertTime').textContent = alert.time;
      alertBox.querySelector('.alertStatus').innerHTML = `${alert.robotName}: <span class="font-bold">${alert.status}</span>`;
      alertBox.querySelector('.alertMessage').textContent = cleanMessage(alert.message);
      alertBox.querySelector('.alertStatusIcon').src = statusImgMapping[alert.status];
    } else {
      alertSlot.classList.add('hidden');
    }
  }
}
