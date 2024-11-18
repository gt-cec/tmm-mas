// drawing.js: functions for drawing on the simulation canvas (map)

// saves the robot data and redraws the simulation map canvas
function updateSimulation(data) {
    savedRobotData = data
    drawSimulationMap()
}

function loadCanvasMapImage() {
    canvasMapImage.src = '/static/img/map.jpeg';
    canvasMapImage.onload = () => {
        ctx.drawImage(canvasMapImage, 0, 0, canvas.width, canvas.height);
    };
}

// (re)draws the simulation map canvas, runs only once and uses the saved robot data
function drawSimulationMap() {
    // clear the map
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    
    // draw the background
    if (canvasMapImage.complete) {
        ctx.globalAlpha = 0.5;
        ctx.drawImage(canvasMapImage, 0, 0, canvas.width, canvas.height);
        ctx.globalAlpha = 1.0;
    };

    // draw the grid
    drawGrid()

    Object.keys(savedRobotData.robots).forEach((robotId) => {
        // if the robot ID is not visible, ignore
        if (!isRobotIdVisible(robotId)) {
            return
        }
        let element = savedRobotData.robots[robotId]
        robotPath.push([element.x, element.y])
        drawPath(element.robotPath, element.colorPath)
        drawPath(element.plan, element.colorPlan)
        robotPath.forEach((point, index) => {
            plotPoint(point.x, point.y, index === robotPath.length - 1)
        })
    })
}

function drawGrid() {
    ctx.strokeStyle = 'rgba(204, 204, 204, 0.35)'
    ctx.lineWidth = 1

    for (let i = 0; i <= gridSize; i++) {
        const pos = i * cellSize

        ctx.beginPath()
        ctx.moveTo(pos, 0)
        ctx.lineTo(pos, canvas.height)
        ctx.stroke()

        ctx.beginPath()
        ctx.moveTo(0, pos)
        ctx.lineTo(canvas.width, pos)
        ctx.stroke()

        if (i > 0 && i < gridSize) {
            ctx.fillStyle = 'black'
            ctx.font = '12px Arial'
            ctx.fillText(i.toString(), 5, canvas.height - pos + 15)
            ctx.fillText(i.toString(), pos - 5, canvas.height - 5)
        }
    }
}

function plotPoint(x, y, isRobot = false) {
    const canvasX = x * cellSize
    const canvasY = canvas.height - (y * cellSize)

    ctx.beginPath()
    ctx.arc(canvasX, canvasY, isRobot ? 6 : 3, 0, 2 * Math.PI)
    ctx.fillStyle = isRobot ? 'red' : 'blue'
    ctx.fill()
}

function drawPath(path, color) {
    if (path.length < 2) return

    ctx.beginPath()
    ctx.moveTo(path[0][0] * cellSize, canvas.height - (path[0][1] * cellSize))

    for (let i = 1; i < path.length; i++) {
        ctx.lineTo(path[i][0] * cellSize, canvas.height - (path[i][1] * cellSize))
    }

    ctx.strokeStyle = color
    ctx.lineWidth = 2
    ctx.stroke()
}
