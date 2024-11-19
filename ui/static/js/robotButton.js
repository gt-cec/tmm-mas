// robotButton.js: functions for handling the robot filter buttons

function setRobotFilter() {
    // go through the communications and hide those not filtered
    Array.from(document.getElementById("data").children).forEach(element => {
        // ignore robot button classes
        if (!element.classList.contains("message-box")) {
            return
        }        
        // filter of -1 means show everything
        if (isRobotIdVisible(element.robotId)) {
            element.style.display = "flex"
        }
        // hide others
        else {
            element.style.display = "none"
        }
    })

    // redraw the simulation map canvas
    drawSimulationMap()
}

function isRobotIdVisible(robotId) {
    return robotFilterId == -1 || robotId == robotFilterId
}

function clickedRobotButton(robotId, numRobots) {
    for (let i = 0; i < numRobots; i++) {
        ["left", "right"].forEach((direction) => {
            let button = document.getElementById("robot-button-" + (i+1) + "-" + direction)
            // not the correct robot? Make sure the filter is removed
            if ((i+1) != robotId) {
                button.classList.remove("robot-button-selected")
            }
            // correct robot and not already selected? Add the filter and select it
            else if (!button.classList.contains("robot-button-selected")) {
                button.classList.add("robot-button-selected")
            }
            // correct robot and already selected? Remove the filter and deselect
            else {
                button.classList.remove("robot-button-selected")
            }
        })
    }
    robotFilterId = robotId == robotFilterId ? -1 : robotId
    setRobotFilter()
}

function createRobotButtons(newNumRobots) {
    numRobots = newNumRobots
    for (let i = 0; i < numRobots; i++) {
        ["left", "right"].forEach((direction) => {
            let container = document.getElementById("robot-buttons-container-" + direction)
            let button = document.createElement("div")
            button.classList = ["robot-button"]
            button.id = "robot-button-" + (i+1) + "-" + direction
            button.innerHTML = "Robot " + (i+1)
            button.setAttribute("onclick", "clickedRobotButton(" + (i+1) + ", " + numRobots + ")")
            container.appendChild(button)
        })
    }
}