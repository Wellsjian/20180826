
#导入模块
from socket import *
from select import *

# 建立套接字
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)
# 绑定地址
sockfd.bind(ADDR)
# 建立监听套接字
sockfd.listen(3)

p = poll()

fdmap = {sockfd.fileno():sockfd}

# 将监听的对象加入监听里,参数一为监听的IO名称, 参数二为监听的IO类型
p.register(sockfd,POLLIN|POLLOUT)

while True:

    events= p.poll()

    for fd,event in events:
        if fd == sockfd.fileno():
            connfd , addr = fdmap[fd].accept()

            p.register(connfd,POLLIN)
            fdmap[connfd.fileno()]=connfd
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                fdmap[fd].close()
                p.unregister(fdmap[fd])
                del fdmap[fd]
            print(data.decode())
            fdmap[fd].send(b"ok")






















