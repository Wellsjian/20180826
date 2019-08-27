"""
基于多线程的网络基础并发通信搭建

思路分析:
1.每次客户端链接,都要创建一个线程,客户端退出时,则线程结束
"""
from threading import Thread
from socket import *
import sys

HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

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

    t = Thread(target=handle,args=(connfd,))
    t.daemon = True

    t.start()



















