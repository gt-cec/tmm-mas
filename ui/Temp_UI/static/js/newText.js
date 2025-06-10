const expandCollapseButton = document.getElementsByClassName('expandCollapseButton');
const expandSrc = '/static/img/expand.png';
const collapseSrc = '/static/img/collapse.png';
const filledFlagSrc = '/static/img/filledFlag.png';

const progressBars = {
  bar1: { total: 61, received: 1, elementId: 'progressBar1', midPoint: Math.ceil(61 / 2) },
  bar2: { total: 62, received: 1, elementId: 'progressBar2', midPoint: Math.ceil(62 / 2) },
  bar3: { total: 61, received: 1, elementId: 'progressBar3', midPoint: Math.ceil(61 / 2) }
};

Array.from(expandCollapseButton).forEach((button, index) => {
  button.addEventListener('click', () => {
    const img = button.querySelector('img');
    img.src = img.src.includes('expand.png') ? collapseSrc : expandSrc;
    const parentBox = document.getElementById(`overviewContainer${index + 1}`);
    const robotMessages = parentBox.querySelector(`#robot${index + 1}Messages`);
    robotMessages.classList.toggle('hidden');
  });
});

export function onFileReceived(barId) {
  const bar = progressBars[barId];
  if (!bar || bar.received >= bar.total) return;
  bar.received++;
  const percent = (bar.received / bar.total) * 100;
  document.getElementById(bar.elementId).style.width = percent + '%';
  const flagBase = bar.elementId + '-flag';
  if (bar.received === 2) {
    document.getElementById(`${flagBase}-start`).src = filledFlagSrc;
  }
  if (bar.received >= bar.midPoint) {
    document.getElementById(`${flagBase}-mid`).src = filledFlagSrc;
  }
  if (bar.received >= bar.total) {
    document.getElementById(`${flagBase}-end`).src = filledFlagSrc;
  }
}

export function renderRobotStatus1(robots) {
  Object.values(robots).forEach(({ message }, index) => {
    const container = document.getElementById(`overviewContainer${index + 1}`);
    const statusText = container.querySelector("span");
    const alertIcon = container.getElementsByClassName('alertIcon')[0];

    const barId = `bar${index + 1}`;
    const bar = progressBars[barId];
    const barElement = document.getElementById(bar.elementId);

    statusText.textContent = "On Track";
    statusText.className = "bg-green-500 text-white text-sm px-3 py-1 rounded-full";
    alertIcon.classList.add("hidden");

    const totalPercent = (bar.received / bar.total) * 100;
    barElement.style.width = `${totalPercent}%`;

    const markerContainer = barElement.parentNode;

    const createDot = (color, percent) => {
      const dot = document.createElement('div');
      dot.className = `absolute w-3 h-3 rounded-full ${color}`;
      dot.style.left = `calc(${percent}% - 6px)`;
      dot.style.top = '-4px';
      return dot;
    };

    if (message && message.includes("behind")) {
      statusText.textContent = "Delay";
      statusText.className = "bg-blue-500 text-white text-sm px-3 py-1 rounded-full";
      alertIcon.classList.remove("hidden");
      const delayPercent = (bar.received / bar.total) * 100;
      markerContainer.appendChild(createDot('bg-blue-500', delayPercent));
    }

    if (message && message.includes("replanning")) {
      statusText.textContent = "Replanning";
      statusText.className = "bg-red-500 text-white text-sm px-3 py-1 rounded-full";
      alertIcon.classList.remove("hidden");
      const replanningPercent = (bar.received / bar.total) * 100;
      markerContainer.appendChild(createDot('bg-red-500', replanningPercent));
    }
  });
}

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

export function renderRobotAlert1({ time, robotName, status, message, robotId }) {
  const cleanMessage = message.replace(/^["']|["']$/g, '');
  const newAlert = document.createElement('div');
  newAlert.classList.add('flex', 'flex-col', 'pr-2');
  newAlert.innerHTML = `
    <span class="text-gray-700 text-sm">${time}</span>
    <div class="relative border rounded-xl shadow-md p-4 ${statusBgMapping[status]}">
      <img class="w-5 h-5 absolute top-4 right-4" src="${statusImgMapping[status]}" alt="alert status icon" />
      <p class="text-gray-800 text-sm font-medium mb-2">${robotName}: <span class="font-bold">${status}</span></p>
      <p class="text-gray-600 text-sm">${cleanMessage}</p>
    </div>
  `;

  const messagesContainer = document.getElementById(`robot${robotId}Messages`);
  if (messagesContainer) {
    messagesContainer.prepend(newAlert);
  }

  const previousUpdatesDivider = messagesContainer.querySelector('.previous-updates-divider');

  if (messagesContainer.children.length > 1 && !previousUpdatesDivider) {
    const divider = document.createElement('div');
    divider.classList.add('previous-updates-divider', 'flex', 'items-center', 'my-4');
    divider.innerHTML = `
      <hr class="flex-grow border-gray-300">
      <span class="text-gray-500 text-sm mx-4">previous updates</span>
      <hr class="flex-grow border-gray-300">
    `;
    messagesContainer.insertBefore(divider, messagesContainer.children[1]);
  } else if (messagesContainer.children.length > 1 && previousUpdatesDivider) {
    messagesContainer.insertBefore(previousUpdatesDivider, messagesContainer.children[1]);
  }
}