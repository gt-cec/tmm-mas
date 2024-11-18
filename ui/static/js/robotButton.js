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
}

function isRobotIdVisible(robotId) {
    return robotFilterId == -1 || robotId == robotFilterId
}

function clickedRobotButton(robotId, numRobots) {
    for (let i = 0; i < numRobots; i++) {
        let button = document.getElementById("robot-button-" + (i+1))
        // not the correct robot? Make sure the filter is removed
        if ((i+1) != robotId) {
            button.classList.remove("robot-button-selected")
            robotFilterId = robotId
        }
        // correct robot and not already selected? Add the filter and select it
        else if (!button.classList.contains("robot-button-selected")) {
            button.classList.add("robot-button-selected")
            robotFilterId = robotId
        }
        // correct robot and already selected? Remove the filter and deselect
        else {
            button.classList.remove("robot-button-selected")
            robotFilterId = -1
        }
    }
    setRobotFilter()
}

function createRobotButtons(numRobots) {
    let robotButtonContainer = document.getElementById("robot-buttons-container")
    for (let i = 0; i < numRobots; i++) {
        let button = document.createElement("div")
        button.classList = ["robot-button"]
        button.id = "robot-button-" + (i+1)
        button.innerHTML = "Robot " + (i+1)
        button.setAttribute("onclick", "clickedRobotButton(" + (i+1) + ", " + numRobots + ")")
        robotButtonContainer.appendChild(button)
    }
}