#!/usr/bin/env python

import sys
import socket



target_host = "www.yahoo.es"
target_port = 80
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host,target_port))
# send some data
client.send("GET / HTTP/1.1\r\nHost: es.yahoo.com\r\n\r\n")
# receive some data
response = client.recv(4096)

a = iter(response.splitlines())
for line in a:
    if len(sys.argv) > 1 and sys.argv[1] == "h":
        posicion = line.lower().find("html")
        if posicion > 0:
            print (line)
    else:
        print (line)