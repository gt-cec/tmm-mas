import { drawGridWall } from './newPixiApp.js';

const robots = {};
const prevRobotPositions = {};
const exploredPositions = new Set();

let robotTexture = null;
let exploredTileLayer = null;

export async function loadRobotTexture(path = '/static/img/triangle.png') {
  robotTexture = await PIXI.Assets.load(path);
  return robotTexture;
}

export function updateRobots(app, robotData, widthSize, heightSize, width, height) {
  if (!robotTexture) return;

  if (!exploredTileLayer) {
    exploredTileLayer = new PIXI.Container();
    app.stage.addChildAt(exploredTileLayer, 0);
  }

  Object.values(robotData).forEach(({ robot_id, jsonX, jsonY }, index) => {
    const x = (jsonX - 0.5) * widthSize;
    const y = height - (jsonY - 0.5) * heightSize;

    if (!robots[robot_id]) {
      const container = new PIXI.Container();
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
      container.x = x;
      container.y = y;
      app.stage.addChild(container);
      // Store the container in the robots object
      robots[robot_id] = container;
      prevRobotPositions[robot_id] = { x, y };
      return;
    }

    // Get the container for this robot
    const container = robots[robot_id];
    const { x: startX, y: startY } = prevRobotPositions[robot_id];

    const line = new PIXI.Graphics();
    line.lineStyle(2, 0x000000, 1);
    app.stage.addChild(line);

    // Animate the container (which includes the sprite and text)
    gsap.to(container, {
      x,
      y,
      duration: 2,
      ease: "linear",
      onUpdate: () => {
        line.clear();
        line.lineStyle(2, 0x000000, 1);
        line.moveTo(startX, startY);
        line.lineTo(container.x, container.y);
      },
      onComplete: () => {
        const gridX = jsonX - 1;
        const gridY = jsonY - 1;
        const gridKey = `${gridX},${gridY}`;
        if (!exploredPositions.has(gridKey)) {
          exploredPositions.add(gridKey);
          drawExploredSquare(app, gridX, gridY, widthSize, heightSize, height);
          revealTileWall(app, gridX, gridY, widthSize, heightSize);
        }

        gsap.to(line, {
          alpha: 0,
          duration: 1,
          onComplete: () => {
            app.stage.removeChild(line);
            line.destroy();
          }
        });
      }
    });

    prevRobotPositions[robot_id] = { x, y };
  });
}

function drawExploredSquare(app, gridX, gridY, widthSize, heightSize, height) {
  const x = gridX * widthSize;
  const y = height - (gridY + 1) * heightSize;

  const square = new PIXI.Graphics();
  square.beginFill(0xA6A09E);
  square.drawRect(x, y, widthSize, heightSize);
  square.endFill();

  exploredTileLayer.addChild(square);
}

function revealTileWall(app, gridX, gridY, widthSize, heightSize) {
  const hiddenWalls = app._hiddenWalls;
  const wallLayer = app._wallLayer;

  // Loop through all hidden walls
  for (let i = hiddenWalls.length - 1; i >= 0; i--) {
    const { x, y, dir } = hiddenWalls[i];

    // Check if the wall's position matches the given grid (gridX, gridY)
    if (x === gridX && y === gridY) {
      // If it matches, draw the wall at this position
      drawGridWall(wallLayer, x, y, dir, widthSize, heightSize);

      // Remove the wall from the hiddenWalls array (so it doesn't get revealed again)
      hiddenWalls.splice(i, 1);
    }
  }
}
