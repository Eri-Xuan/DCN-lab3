from flask import Flask,request
from socket import *
app = Flask(__name__)

UDP_PORT = 53533

@app.route("/register",methods=["PUT"])
def register():
    fs_json = request.get_json
    hostname = fs_json.get("hostname")
    ip = fs_json.get("ip")
    as_ip = fs_json.get("as_ip")
    as_port = fs_json.get("as_port")
    UDP_MESSAGE="TYPE=A\nNAME="+hostname+"\nVALUE="+ip+"\n"+"TTL=10"
    MESSAGE= bytes(UDP_MESSAGE)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MESSAGE,(as_ip,as_port))
    return "Success",201

@app.route("/fibonacci?number=<X>",methods=["GET"])
def fib(X):
    if not isinstance(X,int):
        return "Bad Format", 400
    num1 = 0
    num2 = 1
    num3 = num2
    count = 1
    while count <= X:
        count+=1
        num1 = num2
        num2 = num3
        num3 = num1+num2
    return num3, 200

    

if __name__ == '__main__':
    app.run(debug=True,port=8080)