import socketio
import PIL.Image
import base64, io

def send_image(client, path):
    # open the image
    image = PIL.Image.open(path)
    # convert to bytes array
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="png")
    img_bytes = img_bytes.getvalue()
    
    # Encode the byte data to base64
    base64image = base64.b64encode(img_bytes).decode('utf-8')
    client.emit("cam", {"image": base64image})
    return

if __name__ == "__main__":
    client = socketio.Client()
    client.connect("http://localhost:5000")
    send_image(client, "cec.png")