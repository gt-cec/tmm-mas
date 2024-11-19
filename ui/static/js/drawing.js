// drawing.js: functions for drawing on the simulation canvas (map)

function loadCanvasMapImage() {
    canvasRobotImage.src = "/static/img/robot.png"
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

    if (savedRobotData.robots) {
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
    
            // add the image
            val = pxToCanvas(element.x, element.y)
            ctx.drawImage(canvasRobotImage, val[0] - 25, val[1] - 25, 50, 50)
    
            // add a circle around the image if the robot is selected
            if (robotFilterId == robotId) {
                ctx.beginPath();
                ctx.arc(val[0], val[1], 40, 0, 2 * Math.PI);
                ctx.stroke();
            }
        })

        // draw a circle around the robots that changed
        shadedRobotIds.forEach((robotId) => {
            drawShadedCircleAroundRobot(robotId)
        })
    }
}

// click handler
function clicked(e){
    e.preventDefault();
    const rect = canvas.getBoundingClientRect();

    // calculate x and y relative to the canvas
    const x = (e.clientX - rect.left) * (canvas.width / rect.width)
    const y = (e.clientY - rect.top) * (canvas.height / rect.height)

    // check if close to a robot
    if (savedRobotData.robots) {
        Object.keys(savedRobotData.robots).forEach((robotId) => {
            // if the robot ID is not visible, ignore
            if (!isRobotIdVisible(robotId)) {
                return
            }
            let element = savedRobotData.robots[robotId]
            robotLocation = pxToCanvas(element.x, element.y)
            
            if (Math.sqrt(dist_sq(x, y, robotLocation[0], robotLocation[1])) < 40) {
                clickedRobotButton(robotId)
            }
        })
    }
}

function dist_sq(x1, y1, x2, y2) {
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
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

function pxToCanvas(x, y) {
    return [x * cellSize, canvas.height - (y * cellSize)]
}

function plotPoint(x, y, isRobot = false) {
    val = pxToCanvas(x, y)
    const canvasX = val[0]
    const canvasY = val[1]

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

function drawShadedCircleAroundRobot(robotId) {
    val = pxToCanvas(savedRobotData.robots[robotId]["x"], savedRobotData.robots[robotId]["y"])
    drawShadedCircle(val[0], val[1])
}

function drawShadedCircle(x, y) {
    ctx.fillStyle = 'rgba(255, 0, 0, 0.5)'; // Red with 50% opacity
    ctx.beginPath();
    ctx.arc(x, y, 40, 50, 0, 2 * Math.PI);
    ctx.fill();
}