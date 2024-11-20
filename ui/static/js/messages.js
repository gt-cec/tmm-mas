
function displayMessage(message, dynamicThreshold, robotIds, objectives) {
    const messageBox = document.createElement('div')
    messageBox.classList.add('message-box')

    switch (dynamicThreshold) {
        case 'low':
            messageBox.classList.add('message-low')
            break
        case 'medium':
            messageBox.classList.add('message-medium')
            break
        case 'high':
            messageBox.classList.add('message-high')
            break
    }

    messageBox.innerText = message
    messageBox.robotIds = robotIds
    messageBox.objectives = objectives
    // if the robot ID is currently filtered out, set display to none
    if (!isAtLeastOneRobotIdVisible(messageBox.robotIds)) {
        messageBox.style.display = "none"
    }
    document.getElementById('data').prepend(messageBox) // Prepend for latest messages at the top

    messageBox.onclick = (e) => {
        // replace the plans of the relevant robot IDs, this uses the new robot data so clicking an old message does not overwrite with old data
        messageBox.robotIds.forEach(robotId => {
            savedRobotData[robotId] = newRobotData[robotId]
        })
        shadedRobotIds = messageBox.robotIds

        messageBox.objectives.forEach(objective => {
            savedObjectives[objective] = newObjectives[objective]
        })
        drawSimulationMap()
        fadeOutMessage(messageBox)
    }
}

function fadeOutMessage(element) {
    element.classList.add("fadeout")
    window.setTimeout(() => {
        element.remove()
        shadedRobotIds = []
        drawSimulationMap()
    }, 2000)
}