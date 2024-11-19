
function displayMessage(message, dynamicThreshold) {
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
    messageBox.robotId = 1  // !! REPLACE THIS WITH THE ROBOT ID THAT GENERATED THE MESSAGE!!!
    // if the robot ID is currently filtered out, set display to none
    if (!isRobotIdVisible(messageBox.robotId)) {
        messageBox.style.display = "none"
    }
    dataDiv.prepend(messageBox) // Prepend for latest messages at the top
}