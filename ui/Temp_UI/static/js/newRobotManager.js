import { drawWall } from './newPixiApp.js';
import { renderRobotSpecificAlerts } from './newInfoPanel.js';

const robots = {};
const prevRobotPositions = {};
const exploredPositions = new Set();
let robotTexture = null;
let exploredTileLayer = null;

export async function loadRobotImage(path = '/static/img/triangle.png') {
  robotTexture = await PIXI.Assets.load(path);
  return robotTexture;
}

export function updateRobotsOnMap(app, robotData, cellWidth, cellHeight, mapHeight) {
  if (!robotTexture) return;

  if (!exploredTileLayer) {
    exploredTileLayer = new PIXI.Container();
    app.stage.addChildAt(exploredTileLayer, 0);
  }

  Object.values(robotData).forEach(({ robot_id, jsonX, jsonY }, index) => {
    const x = (jsonX - 0.5) * cellWidth;
    const y = mapHeight - (jsonY - 0.5) * cellHeight;

    if (!robots[robot_id]) {
      robots[robot_id] = createRobotSprite(index, x, y, robot_id);
      app.stage.addChild(robots[robot_id]);
      prevRobotPositions[robot_id] = { x, y };
      return;
    }

    const container = robots[robot_id];
    const { x: startX, y: startY } = prevRobotPositions[robot_id];

    animateRobotMovement(app, container, startX, startY, x, y, () => {
      const gridX = jsonX - 1;
      const gridY = jsonY - 1;
      const gridKey = `${gridX},${gridY}`;
      if (!exploredPositions.has(gridKey)) {
        exploredPositions.add(gridKey);
        drawExploredSquare(gridX, gridY, cellWidth, cellHeight, mapHeight);
        revealWall(app, gridX, gridY);
      }
    });

    prevRobotPositions[robot_id] = { x, y };
  });
}

function createRobotSprite(index, x, y) {
  const container = new PIXI.Container();
  container.interactive = true;
  container.cursor = 'pointer';
  container.robot_id = index + 1;
  const sprite = PIXI.Sprite.from(robotTexture);
  sprite.anchor.set(0.5);
  sprite.scale.set(0.2);

  const robotLabel = new PIXI.Text(`R${index + 1}`, {
    fontFamily: 'Arial',
    fontSize: 12,
    fill: 0xFFFFFF,
  });
  robotLabel.anchor.set(0.5);
  robotLabel.y = sprite.height / 2 + 10;

  container.addChild(sprite);
  container.addChild(robotLabel);
  container.position.set(x, y);
  container.on('pointerdown', () => onRobotClick(container, robotLabel));
  return container;
}

let activeRobotContainer = null;
let activeLabel = null;
let activeTimeout = null;
export let activeRobotID = null;

function onRobotClick(container, label) {
  clearTimeout(activeTimeout);
  if (activeRobotContainer && activeRobotContainer !== container) {
    activeRobotContainer.scale.set(1, 1);
    activeLabel.style.fill = 0xFFFFFF;
    if (activeRobotID !== null) {
      const prevDOM = document.getElementById(`simulatorRobotStatusContainer${activeRobotID}`);
      if (prevDOM) prevDOM.classList.remove('border-black');
    }
  }
  activeRobotContainer = container;
  activeLabel = label;
  activeRobotID = container.robot_id;
  renderRobotSpecificAlerts(activeRobotID);
  container.scale.set(1.5);
  label.style.fill = 0x000000;
  const selectedRobotStatusContainer = document.getElementById(`simulatorRobotStatusContainer${activeRobotID}`);
  if (selectedRobotStatusContainer) selectedRobotStatusContainer.classList.add('border-black');
  const selectedRobotAlertContainer = document.getElementById('simulatorRobotAlertsContainer');
  if (selectedRobotAlertContainer) selectedRobotAlertContainer.classList.add('opacity-50');
  activeTimeout = setTimeout(() => {
    container.scale.set(1, 1);
    label.style.fill = 0xFFFFFF;
    if (selectedRobotStatusContainer) selectedRobotStatusContainer.classList.remove('border-black');
    if (selectedRobotAlertContainer) selectedRobotAlertContainer.classList.remove('opacity-50');
    document.getElementById('robotSpecificAlert1')?.classList.add('hidden');
    document.getElementById('robotSpecificAlert2')?.classList.add('hidden');
    document.getElementById('robotSpecificHeader')?.classList.add('hidden');
    activeRobotContainer = null;
    activeLabel = null;
    activeTimeout = null;
    activeRobotID = null;
  }, 10000);
}

function animateRobotMovement(app, container, startX, startY, endX, endY, onCompleteCallback) {
  const line = new PIXI.Graphics();
  line.lineStyle(2, 0x000000, 1);
  app.stage.addChild(line);

  app.stage.setChildIndex(container, app.stage.children.length - 1);
  app.stage.setChildIndex(line, app.stage.children.length - 2);

  gsap.to(container, {
    x: endX,
    y: endY,
    duration: 0.5,
    ease: "linear",
    onUpdate: () => {
      line.clear();
      line.lineStyle(2, 0x000000, 1);
      line.moveTo(startX, startY);
      line.lineTo(container.x, container.y);
    },
    onComplete: () => {
      onCompleteCallback?.();

      gsap.to(line, {
        alpha: 0,
        duration: 0.5,
        onComplete: () => {
          line.destroy();
        }
      });
    }
  });
}

function drawExploredSquare(gridX, gridY, cellWidth, cellHeight, mapHeight) {
  const x = gridX * cellWidth;
  const y = mapHeight - (gridY + 1) * cellHeight;

  const square = new PIXI.Graphics();
  square.beginFill(0xA6A09E);
  square.drawRect(x, y, cellWidth, cellHeight);
  square.endFill();

  exploredTileLayer.addChild(square);
  gsap.to(square, { alpha: 1, duration: 0.3 });
}

function revealWall(app, gridX, gridY) {
  const hiddenWalls = app._hiddenWalls;
  const wallLayer = app._wallLayer;

  for (let i = hiddenWalls.length - 1; i >= 0; i--) {
    const { x, y, dir, isDoor } = hiddenWalls[i];

    if (x === gridX && y === gridY) {
      drawWall(wallLayer, x, y, dir, isDoor);

      hiddenWalls.splice(i, 1);
    }
  }
}