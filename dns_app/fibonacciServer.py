import json

from flask import Flask, request
from socket import *
import requests

app = Flask(__name__)

arr = [1,1]

def fib(num):
    if num <= len(arr):
        return arr[num-1]

    loops = num - len(arr)
    for i in range(loops):
        arr.append(arr[-1] + arr[-2])
    return arr[num-1]

def regAS(hostname, ip, asIp, asPort):
    url = "TYPE=A\nNAME=" + str(hostname) + "\nVALUE=" + str(ip) + "\nTTL=10\n"

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(url.encode(), (asIp, asPort))

    response, clientAddress = clientSocket.recvfrom(2048)
    clientSocket.close()

    response = response.decode()

    if "success" in  response:
        return "success", response
    else:
        return "fail", response

@app.route("/register", methods=["PUT"])
def register():
    data = request.get_json()

    try:
        hostname, ip, asIp, asPort = data["hostname"], data["ip"], data["as_ip"], int(data["as_port"])
    except:
        return "Something went wrong, check your fields", 400

    result, response = regAS(hostname, ip, asIp, asPort)

    if result == "success":
        return "Registration successful", 201
    else:
        return "Registration failed", 400

@app.route("/fibonacci", methods=["GET"])
def fibPage():
    try:
        number = int(request.args.get("number"))
    except:
        return "Invalid number or request", 400

    res = fib(number)

    return str(res), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)

