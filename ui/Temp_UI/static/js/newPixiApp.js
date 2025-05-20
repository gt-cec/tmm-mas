const gridSize = 6;
const width = 800;
const height = 500;
const widthSize = width / gridSize;
const heightSize = height / gridSize;

const staticWalls = [
  { x: 0, y: 0, dir: "right" },
  { x: 0, y: 1, dir: "top" },
  { x: 0, y: 3, dir: "right" },
  { x: 0, y: 3, dir: "top" },
  { x: 0, y: 4, dir: "right", isDoor: true },
  { x: 0, y: 5, dir: "right" },
  { x: 2, y: 3, dir: "top" },
  { x: 2, y: 2, dir: "left" },
  { x: 2, y: 3, dir: "left" },
  { x: 2, y: 2, dir: "bottom", isDoor: true },
  { x: 3, y: 2, dir: "bottom" },
  { x: 3, y: 3, dir: "right" },
  { x: 3, y: 2, dir: "right" },
  { x: 5, y: 0, dir: "left" },
  { x: 5, y: 1, dir: "left" },
  { x: 5, y: 4, dir: "left" },
  { x: 5, y: 5, dir: "left" }
];

export { gridSize, width, height, widthSize, heightSize, drawGridWall };

// Utility to split visible/hidden walls
function splitWalls(walls, visibleRatio = 0.6) {
  const shuffled = [...walls].sort(() => Math.random() - 0.5);
  const cutoff = Math.floor(walls.length * visibleRatio);
  return {
    visibleWalls: shuffled.slice(0, cutoff),
    hiddenWalls: shuffled.slice(cutoff)
  };
}

// Reusable wall drawer
function drawGridWall(wallLayer, gridX, gridY, direction, isDoor = false, widthSize, heightSize) {
  const x = gridX * widthSize;
  const y = (gridSize - gridY - 1) * heightSize;  // Adjust y for the robot grid

  const wall = new PIXI.Graphics();
  isDoor ? wall.lineStyle(10, 0xD3D3D3) : wall.lineStyle(10, 0x000000); // Wall thickness

  // Draw the wall based on the direction
  switch (direction) {
    case 'left':
      wall.moveTo(x + 5, y); // Add offset to center the line
      wall.lineTo(x + 5, y + heightSize);
      break;
    case 'right':
      wall.moveTo(x + widthSize - 5, y);
      wall.lineTo(x + widthSize - 5, y + heightSize);
      break;
    case 'top':
      wall.moveTo(x, y + 5); // Add offset to center the line
      wall.lineTo(x + widthSize, y + 5);
      break;
    case 'bottom':
      wall.moveTo(x, y + heightSize - 5);
      wall.lineTo(x + widthSize, y + heightSize - 5);
      break;
    default:
      console.warn(`Invalid wall direction: ${direction}`);
      return;
  }

  wallLayer.addChild(wall);
}


export function initPixiApp() {
  const app = new PIXI.Application({
    width: width,
    height: height,
    backgroundColor: 0xB6B0AD
  });

  const appContainer = document.getElementById("pixiApp");
  if (!appContainer) {
    console.error("❌ Could not find the #pixiApp div to attach PixiJS canvas");
    return null;
  }

  appContainer.appendChild(app.view);

  // Draw grid
  const grid = new PIXI.Graphics();
  grid.lineStyle(1, 0xA3A3A3);
  for (let i = 0; i <= gridSize; i++) {
    grid.moveTo(i * widthSize, 0);
    grid.lineTo(i * widthSize, height);
    grid.moveTo(0, i * heightSize);
    grid.lineTo(width, i * heightSize);
  }
  app.stage.addChild(grid);

  // Wall container
  const wallLayer = new PIXI.Container();
  app.stage.addChild(wallLayer);

  // Map border
  const wall = new PIXI.Graphics();
  wall.lineStyle(20, 0x000000);
  wall.moveTo(0, 0);
  wall.lineTo(width, 0);
  wall.lineTo(width, height);
  wall.lineTo(0, height);
  wall.lineTo(0, 0);
  wallLayer.addChild(wall);

  // Show only 60% walls
  const { visibleWalls, hiddenWalls } = splitWalls(staticWalls, 1.0);
  visibleWalls.forEach(({ x, y, dir, isDoor }) => {
    drawGridWall(wallLayer, x, y, dir, isDoor, widthSize, heightSize);
  });

  // Save references for robotManager to access
  app._wallLayer = wallLayer;
  app._hiddenWalls = hiddenWalls;

  return app;
}