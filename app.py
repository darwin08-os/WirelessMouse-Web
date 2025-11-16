from flask import Flask, request,render_template
import socket


host = "10.98.9.244"  #your laptop ip
port = 45202

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/cords",methods=["POST"])
def moves():
	data = request.get_json()
	client.sendto(str(data["cordinates"]).encode(),(host,port))	
	return data
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)