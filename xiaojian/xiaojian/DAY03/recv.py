from socket import *
import os
sock_file = './sock'
s = socket(AF_INET,SOCK_DGRAM)
s.connect(sock_file)
while True:
    msg = input('>>>')
    if not msg:
        break
    s.send(msg.encode())
s.close()