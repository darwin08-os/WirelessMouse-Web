# udp_mouse_server_compatible.py
import socket
from pynput import mouse
import pyautogui

screen_width, screen_height = pyautogui.size()
host = "0.0.0.0"
port = 45202

cursor = mouse.Controller()
mobile_width = None

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
print(f"UDP server listening on {host}:{port}")

while True:
    try:
        data, addr = server.recvfrom(1024)
        msg = data.decode().strip()

        if not msg:
            continue

        # try to parse as number (your first width send)
        try:
            mobile_width = float(msg)
            print(f"Received mobile width: {mobile_width}")
            continue
        except:
            pass

        # handle movement / clicks
        parts = msg.replace("\n","").split(",")
        if len(parts) == 3 and parts[0] == "move":
            dx = float(parts[1])
            dy = float(parts[2])
            if mobile_width:
                cursor.move((-1 * dx) * (screen_width / mobile_width),
                            (-1 * dy) * (screen_width / mobile_width))
        elif parts[0] == "left":
            cursor.press(mouse.Button.left)
            cursor.release(mouse.Button.left)
        elif parts[0] == "right":
            cursor.press(mouse.Button.right)
            cursor.release(mouse.Button.right)
        else:
            # unknown data; ignore
            pass

    except Exception as e:
        print("Error:", e)
