#! /usr/bin/python3

import socket

s = socket.socket()

s.connect(("127.0.0.1", 22))

answer = s.recv(1024)

print (answer)

s.close()