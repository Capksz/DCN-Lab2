from flask import Flask, request
from socket import *
import requests

app = Flask(__name__)

def queryAS(hostname, asIp, asPort):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    url = "TYPE=A\nNAME=" + hostname + "\n"
    clientSocket.sendto(url.encode(), (asIp, int(asPort)))
    response, clientAddress = clientSocket.recvfrom(2048)
    clientSocket.close()

    return response

def queryFib(fsIp, fsPort, num):
    url = "http://" + str(fsIp) + ":" + str(fsPort) + "/fibonacci?number=" + str(num)
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return "Error: " + str(response.status_code)


@app.route("/fibonacci", methods=["GET"])
def fib():
    try:
        hostname, fsPort, number, asIp, asPort = request.args.get("hostname"), request.args.get("fs_port"), request.args.get("number"), request.args.get("as_ip"), request.args.get("as_port")
    except:
        return "Error reading arguments", 400

    try:
        number = int(number)
    except:
        return "Number invalid", 400

    if hostname == None or fsPort == None and number == None or asIp == None or asPort == None:
        return "Missing parameters", 400
    print('bye')
    fsIp = str(queryAS(hostname, asIp, asPort).decode()).split("\n")[2].split("=")[1]
    res = queryFib(fsIp, fsPort, number)

    return "The fibonacci result for number " + str(number) + " is: " + str(res), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

