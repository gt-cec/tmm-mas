// sockets.js: functions for creating the socket and handling data flow to/from the client through it

function createSocket() {
    let socket = io(location.host)


    socket.on("connect", () => {
        console.log("Connected to socket server")
    })

    socket.on("message", (msg) => {
        console.log(`Message from server: ${msg}`)
        const data = msg
        if (data) {
            console.log('Received:', data)

            const sliderValue = disparitySlider.value
            let dynamicThreshold

            switch (sliderValue) {
                case '0':
                    dynamicThreshold = 'low'
                    break
                case '1':
                    dynamicThreshold = 'medium'
                    break
                case '2':
                    dynamicThreshold = 'high'
                    break
                default:
                    dynamicThreshold = 'low'
            }

            // if this is the first message, overwrite the savedRobotData and show the robots
            if (data.initial) {
                savedRobotData = data.robots
                savedObjectives = data.objectives
                initialRobotData = data.robots
                drawSimulationMap()
            }

            // if this data has a message, show the message (one message can inform changes to multiple robots)
            if (data.message) {
                displayMessage(data.message, dynamicThreshold, Object.keys(data.robots), Object.keys(data.objectives))
            }

            if (data.robots !== undefined) {
                // on the first run, set up the robot buttons
                if (numRobots == -1) {
                    createRobotButtons(Object.keys(data.robots).length)
                }
                // set the new robot data
                Object.keys(data.robots).forEach((robotId) => {
                    newRobotData[robotId] = data.robots[robotId]
                })
            }

            if (data.objectives !== undefined) {
                Object.keys(data.objectives).forEach(objective => {
                    newObjectives[objective] = data.objectives[objective]
                })
            }
        }
    })

    socket.on("disconnect", () => {
        console.log("Disconnected from socket server")
        isPlaying = false
        playStopButton.textContent = 'Play'
    })

    return socket
}