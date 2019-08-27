"""
gevent_ sever  基于协程的 tcp 技术

"""
import gevent
from gevent import monkey
monkey.patch_socket() #在导入模块前执行
from socket import *

#创建tcp套接字
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",22222))
sockfd.listen(3)

def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b"ok")
    connfd.close()
while True:
    connfd ,addr = sockfd.accept()
    print("Connect from",addr)
    gevent.spawn(handle,connfd)

sockfd.close()
