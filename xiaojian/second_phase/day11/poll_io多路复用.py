from socket import *
from select import *

HOST = "0.0.0.0."
PORT = 22222
ADDR = (HOST,PORT)

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

p = poll()

#fileno   文件描述符
fdmap = {sockfd.fileno(): sockfd}
#register 里需要有两个参数，监控io对象 ,io类型,将监控Io对象加入poll中
p.register(sockfd,POLLIN|POLLERR)

while True:
    #循环遍历发生的事件
    events = p.poll()

    for fd ,event in events:
        if fd == sockfd.fileno():
            connfd ,addr = fdmap[fd].accept()
            print("Listen the port %d" %PORT)
            p.register(connfd,POLLIN)
            fdmap[connfd.fileno()] = connfd
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                fdmap[fd].close()
                p.unregister(fd)
                del fdmap[fd]
                continue
            print("Receive",data.decode())
            fdmap[fd].send(b"ok")


