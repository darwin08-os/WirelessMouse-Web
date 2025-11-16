import socket
from pynput import mouse
import pyautogui

screen_width, screen_height = pyautogui.size()

host = "0.0.0.0"
port = 45202
width = '' #width of mobile
server = socket.socket()

server.bind((host,port))

server.listen(1)
print("listening...")

conn,addr = server.accept()
print("connected to : ", addr)

width = int(str(conn.recv(100).decode()))

cursor = mouse.Controller()


# {'cordinates': 'move,-2,-0.5\n', width : some Value}
while True:
	cordinates = conn.recv(100).decode()
	if not cordinates:
		break
	elif cordinates.split(",")[0] == "move":
		cursor.move((-1 * float(cordinates.split(",")[1])) * (screen_width/width),(-1 * float(cordinates.split(",")[2]))*(screen_width/width))
	elif cordinates.split(",")[0] == "left":
		cursor.press(mouse.Button.left)
		cursor.release(mouse.Button.left)
	elif cordinates.split(",")[0] == "right":
		cursor.press(mouse.Button.right)
		cursor.release(mouse.Button.right)
	else:
		pass	
conn.close()
server.close()