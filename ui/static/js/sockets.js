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

            if (data.result) {
                displayMessage(data.result, dynamicThreshold)
            }
            if (data.robots !== undefined) {
                // on the first run, set up the robot buttons
                if (numRobots == -1) {
                    createRobotButtons(Object.keys(data.robots).length)
                }
                updateSimulation(data)
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