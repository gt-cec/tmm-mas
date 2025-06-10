const gridSize = 6;
const mapWidth = 800;
const mapHeight = 500;
const cellWidth = mapWidth / gridSize;
const cellHeight = mapHeight / gridSize;
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

export { gridSize, mapHeight, cellWidth, cellHeight };

export function initPixiMap() {
  const app = new PIXI.Application({
    width: mapWidth,
    height: mapHeight,
    backgroundColor: 0xB6B0AD
  });

  const appContainer = document.getElementById("pixiMap");
  if (!appContainer) {
    console.error("Cannot find the corresponding div to attach PixiJS canvas");
    return null;
  }

  appContainer.appendChild(app.view);

  // Draw grid
  // const grid = new PIXI.Graphics();
  // grid.lineStyle(1, 0xA3A3A3);
  // for (let i = 0; i <= gridSize; i++) {
  //   grid.moveTo(i * cellWidth, 0);
  //   grid.lineTo(i * cellWidth, height);
  //   grid.moveTo(0, i * cellHeight);
  //   grid.lineTo(mapWidth, i * cellHeight);
  // }
  // app.stage.addChild(grid);

  const wallLayer = new PIXI.Container();
  app.stage.addChild(wallLayer);

  const mapBorders = new PIXI.Graphics();
  mapBorders.lineStyle(20, 0x000000);
  mapBorders.moveTo(0, 0);
  mapBorders.lineTo(mapWidth, 0);
  mapBorders.lineTo(mapWidth, mapHeight);
  mapBorders.lineTo(0, mapHeight);
  mapBorders.lineTo(0, 0);
  wallLayer.addChild(mapBorders);

  const { visibleWalls, hiddenWalls } = splitWalls(staticWalls, 0.5);
  visibleWalls.forEach(({ x, y, dir, isDoor }) => {
    drawWall(wallLayer, x, y, dir, isDoor);
  });

  app._wallLayer = wallLayer;
  app._hiddenWalls = hiddenWalls;

  return app;
}

export function drawWall(wallLayer, gridX, gridY, direction, isDoor = false) {
  const x = gridX * cellWidth;
  const y = (gridSize - gridY - 1) * cellHeight;

  const wall = new PIXI.Graphics();
  isDoor ? wall.lineStyle(10, 0xD3D3D3) : wall.lineStyle(10, 0x000000);

  switch (direction) {
    case 'left':
      wall.moveTo(x + 5, y);
      wall.lineTo(x + 5, y + cellHeight);
      break;
    case 'right':
      wall.moveTo(x + cellWidth - 5, y);
      wall.lineTo(x + cellWidth - 5, y + cellHeight);
      break;
    case 'top':
      wall.moveTo(x, y + 5);
      wall.lineTo(x + cellWidth, y + 5);
      break;
    case 'bottom':
      wall.moveTo(x, y + cellHeight - 5);
      wall.lineTo(x + cellWidth, y + cellHeight - 5);
      break;
    default:
      console.warn(`Invalid wall direction: ${direction}`);
      return;
  }

  wallLayer.addChild(wall);
}

function splitWalls(walls, visibleRatio = 0.6) {
  const shuffled = [...walls].sort(() => Math.random() - 0.5);
  const cutoff = Math.floor(walls.length * visibleRatio);
  return {
    visibleWalls: shuffled.slice(0, cutoff),
    hiddenWalls: shuffled.slice(cutoff)
  };
}