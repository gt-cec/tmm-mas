// drawing.js: functions for drawing on the simulation canvas (map)

function loadCanvasImages() {
    canvasRobotImage.src = "/static/img/robot.png"
    canvasObjectiveImage.src = "/static/img/objective.png"
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

    // draw the robot indicators 
    drawRobotMessageIndicators()

    // draw the robots
    if (savedRobotData) {
        Object.keys(savedRobotData).forEach((robotId) => {
            // check if the robot has not been updated for a while
            let now = Date.now() / 1000
            if (now - savedRobotData[robotId].lastSeen > timeoutForDelayedRobot) {
                drawDelayedRobotIndicator(robotId)
            }

            // if the robot ID is not visible, ignore
            if (!isRobotIdVisible(robotId)) {
                return
            }

            let element = savedRobotData[robotId]

            // draw the robot's initial path
            drawPath(element.initialPlan, colorInitialPlan)

            // draw the robot's completed path
            drawPath(element.robotPath, colorCompletedPlan)

            // draw the robot's current plan
            drawPath(element.currentLocationPlan, colorCurrentPlan, false, true)

            // draw the robot's previous plan if selected
            if (robotFilterId != -1) {
                drawPath(element.previousLocationPlan, colorPreviousPlan, dash=true)
            }

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

    // draw the objective markers
    Object.keys(savedObjectives).forEach(objective => {
        drawObjective(savedObjectives[objective].x, savedObjectives[objective].y, savedObjectives[objective].name)
    })
}

// click handler
function clicked(e){
    e.preventDefault();
    const rect = canvas.getBoundingClientRect();

    // calculate x and y relative to the canvas
    const x = (e.clientX - rect.left) * (canvas.width / rect.width)
    const y = (e.clientY - rect.top) * (canvas.height / rect.height)

    // check if close to a robot
    if (savedRobotData) {
        Object.keys(savedRobotData).forEach((robotId) => {
            // if the robot ID is not visible, ignore
            if (!isRobotIdVisible(robotId)) {
                return
            }
            let element = savedRobotData[robotId]
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

function drawPath(path, color, dash=false, thick=false) {
    if (path.length < 2) return

    ctx.beginPath()
    ctx.moveTo(path[0][0] * cellSize, canvas.height - (path[0][1] * cellSize))

    for (let i = 1; i < path.length; i++) {
        ctx.lineTo(path[i][0] * cellSize, canvas.height - (path[i][1] * cellSize))
    }

    ctx.setLineDash(dash ? [5, 10] : [])

    ctx.strokeStyle = color
    ctx.lineWidth = thick ? 5 : 2
    ctx.stroke()
    ctx.setLineDash([])
}

function drawShadedCircleAroundRobot(robotId) {
    val = pxToCanvas(savedRobotData[robotId]["x"], savedRobotData[robotId]["y"])
    drawShadedCircle(val[0], val[1])
}

function drawShadedCircle(x, y) {
    ctx.fillStyle = 'rgba(255, 0, 0, 0.5)'; // Red with 50% opacity
    ctx.beginPath();
    ctx.arc(x, y, 40, 50, 0, 2 * Math.PI);
    ctx.fill();
}

function drawObjective(x, y, name) {
    // add the image
    val = pxToCanvas(x, y)
    ctx.drawImage(canvasObjectiveImage, val[0] - 15, val[1] - 47, 50, 50)
    ctx.fillStyle = "purple"
    ctx.font = "25px Verdana"
    ctx.fillText(name, val[0] - 9, val[1] + 25)
}

function drawRobotMessageIndicators() {
    markedRobots = []
    // for each message
    Array.from(document.getElementById("messages").children).forEach(element => {
        // ignore robot button classes
        if (!element.classList.contains("message-box")) {
            return
        }

        // if a robot is relevant and not currently marked
        element.robotIds.forEach((robotId) => {
            if (!markedRobots.includes(robotId)) {
                // add id to the marked robot ids
                markedRobots.push(robotId)
                // draw the indicator
                val = pxToCanvas(savedRobotData[robotId].x, savedRobotData[robotId].y)
                ctx.fillStyle = "red"
                ctx.font = "40px Verdana"
                let robotVisible = isRobotIdVisible(robotId)
                ctx.fillText("!", val[0] - (robotVisible ? 30 : 8), val[1] + (robotVisible ? 0 : 15))
                // if robot is visible, add a circle around the indicator
                if (!robotVisible) {
                    ctx.strokeStyle = "red"
                    ctx.beginPath();
                    ctx.arc(val[0], val[1], 20, 0, 2 * Math.PI);
                    ctx.stroke();
                }
            }
        })
    })
}

function drawDelayedRobotIndicator(robotId) {
    // draw the indicator
    val = pxToCanvas(savedRobotData[robotId].x, savedRobotData[robotId].y)
    ctx.fillStyle = "goal"
    ctx.font = "30px Verdana"
    let robotVisible = isRobotIdVisible(robotId)
    ctx.fillText("⏰", val[0] + (robotVisible ? -40 : -15), val[1] + (robotVisible ? -20 : 10))
    // if robot is visible, add a circle around the indicator
    if (!robotVisible) {
        ctx.strokeStyle = "gold"
        ctx.beginPath();
        ctx.arc(val[0], val[1], 30, 0, 2 * Math.PI);
        ctx.stroke();
    }
}