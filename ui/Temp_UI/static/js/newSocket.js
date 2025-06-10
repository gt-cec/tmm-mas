export function createSocket(onDataReceived) {
  const socket = io(location.host);

  socket.on("connect", () => {
    console.log("Connected to socket server");
  });

  socket.on("message", (data) => {
    if (!data.initial && data.robots !== undefined) {
      onDataReceived(data);
    }
  });

  socket.on("disconnect", () => {
    console.log("Disconnected from socket server");
  });

  socket.on("connect_error", (err) => {
    console.log("Connection error:", err.message);
  });

  return socket;
}