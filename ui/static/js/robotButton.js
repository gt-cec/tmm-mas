// robotButton.js: functions for handling the robot filter buttons

function setRobotPlanFilter() {
    // go through the communications and hide those not filtered
    Array.from(document.getElementById("data").children).forEach(element => {
        // ignore robot button classes
        if (!element.classList.contains("message-box")) {
            return
        }        
        // filter of -1 means show everything
        if (isAtLeastOneRobotIdVisible(element.robotIds)) {
            element.style.display = "flex"
        }
        // hide others
        else {
            element.style.display = "none"
        }
    })

    // redraw the simulation map canvas
    drawSimulationMap()

    // redraw the plan panel
    displayPlan()
}

function isRobotIdVisible(robotId) {
    return robotFilterId == -1 || robotId == robotFilterId
}

function isAtLeastOneRobotIdVisible(robotIds) {
    return robotFilterId == -1 || robotIds.includes(robotFilterId.toString())
}

function setRobotButtonVisuals() {
    for (let i = 0; i < numRobots; i++) {
        ["left", "right"].forEach((direction) => {
            let button = document.getElementById("robot-button-" + (i+1) + "-" + direction)
            // not the correct robot? Make sure the filter is removed
            if ((i+1) != robotFilterId) {
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
}

function clickedRobotButton(robotId) {
    robotFilterId = robotId == robotFilterId ? -1 : robotId
    setRobotPlanFilter()
    setRobotButtonVisuals()
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