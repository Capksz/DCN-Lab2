import socket

from flask import Flask, request, jsonify
from socket import *
import os

dnsFile = "dnsFile.txt"

def loadDNS():
    records = {}

    if os.path.exists(dnsFile):
        with open(dnsFile, "r") as f:
            for line in f:
                hostname, ip, ttl = line.strip().split(",")
                records[hostname] = {"ip":ip, "ttl":int(ttl)}
    return records

def saveDNS(hostname, ip, ttl):
    with open(dnsFile, "a") as f:
        record = hostname + "," + ip + "," + ttl + "\n"
        f.write(record)

dnsRecords = loadDNS()

def registration(message):
    #index 0: dns type, 1: hostname, 2: ip, 3: TTL
    try:
        lines = message.split("\n")
        arr = []
        for i in range(4):
            field = lines[i].split("=")[1].strip()
            if not field:
                return "fail"
            arr.append(field)

        if arr[0] != "A":
            return "fail"
        arr[3] = int(arr[3])

        if arr[1] in dnsRecords:
            return "fail"

        dnsRecords[arr[1]] = {"ip":arr[2], "ttl":int(arr[3])}
        saveDNS(arr[1], arr[2], str(arr[3]))
        return("success")
    except:
        return "fail"

def queried(message):
    # index 0: dns type, 1: hostname
    try:
        lines = message.split("\n")
        arr = []
        for i in range(2):
            field = lines[i].split("=")[1].strip()
            if not field:
                return "fail"
            arr.append(field)

        if arr[0] != "A":
            return "fail"

        if arr[1] in dnsRecords:
            record = dnsRecords[arr[1]]
            ip = record["ip"]
            ttl = record["ttl"]
            res = "TYPE=A\nNAME=" + str(arr[1]) + "\nVALUE=" + str(ip) + "\nTTL="+ str(ttl) + "\n"
            return res
        else:
            return "fail"
    except:
        return "fail"

def runServer():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("0.0.0.0", 53533))

    print("Server up and running")

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode()

        if message.startswith("TYPE=A\nNAME="):
            if "VALUE=" in message:
                response = registration(message)
            else:
                response = queried(message)
            print(response)
            serverSocket.sendto(response.encode(), clientAddress)

if __name__ == "__main__":
    runServer()
