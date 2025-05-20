export function renderPlaceholderRobots(count = 3) {
  const panelContainer = document.getElementById('robotStatus');
  panelContainer.innerHTML = "";

  for (let i = 0; i < count; i++) {
    const placeholderCard = document.createElement('div');
    placeholderCard.className = "flex justify-between items-center px-4 py-2 mb-2 border shadow-md rounded-xl";

    const info = document.createElement('span');
    info.textContent = `Robot ${i + 1} - No Status`

    const status = document.createElement('span');
    status.textContent = "No Status";
    status.className = "bg-gray-300 text-sm px-3 py-1 rounded-full";

    placeholderCard.appendChild(info);
    placeholderCard.appendChild(status);
    panelContainer.appendChild(placeholderCard);
  }
}

export function renderRobotStatus(robots) {
  const panelContainer = document.getElementById('robotStatus');
  panelContainer.innerHTML = "";

  const robotEntries = Object.values(robots);

  robotEntries.forEach(({ jsonX, jsonY }, index) => {
    const card = document.createElement('div');
    card.className = "flex justify-between items-center px-4 py-2 mb-2 border shadow-md rounded-xl";

    const info = document.createElement('span');
    const x = jsonX ?? "—";
    const y = jsonY ?? "—";
    info.textContent = `Robot ${index + 1} - (${x}, ${y})`;

    const status = document.createElement('span');
    status.textContent = "On Track";
    status.className = "bg-green-500 text-white text-sm px-3 py-1 rounded-full";

    card.appendChild(info);
    card.appendChild(status);
    panelContainer.appendChild(card);
  });
}

export function renderRobotAlert({ time, robotName, status, message }) {
  const container = document.getElementById('robotAlerts');

  const wrapper = document.createElement('div');
  wrapper.className = "flex flex-col";

  const timeElem = document.createElement('span');
  timeElem.className = "text-sm text-gray-700 mb-2";
  timeElem.textContent = time;



  const card = document.createElement('div');
  card.className = "bg-white shadow-md rounded-xl p-4 border w-full";

  card.innerHTML = `
    <p class="font-medium text-sm text-gray-800 mb-2">${robotName}: <span class="font-bold">${status}</span></p>
    <p class="text-sm text-gray-600">${message}</p>
  `;

  wrapper.appendChild(timeElem);
  wrapper.appendChild(card);
  container.appendChild(wrapper);
}