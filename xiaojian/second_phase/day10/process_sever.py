"""
基于Process多进程的的并发通信的搭建
"""
from multiprocessing import Process
from socket import *
import sys,signal

HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port %d......" %PORT)

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")

while True:
    try:
        connfd , addr = sockfd.accept()
    except  KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)
        continue

    t = Process(target=handle,args=(connfd,))
    t.daemon = True

    t.start()