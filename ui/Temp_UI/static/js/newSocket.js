// create WebSocket connection from client to Socket.IO server
export function createSocket(onDataReceived) {
  const socket = io(location.host);

  socket.on("connect", () => {
    console.log("Connected to socket server");
  });

  socket.on("message", (data) => {
    if (!data.initial && data.robots !== undefined) {
      //console.log("Data sent from server:", data);
      onDataReceived(data);
    }
  });

  socket.on("disconnect", () => {
    console.log("Disconnected from socket server");
  });

  return socket;
}