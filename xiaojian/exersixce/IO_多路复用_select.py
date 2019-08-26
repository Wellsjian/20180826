
#导入模块
from select import select
from socket import *
HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)
#创建套接字,搭建网络tcp实现通信
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)

#创建监听套接字, 一个监听套接字可以监听多个客户端
sockfd.listen(3)

#创建select监听,实现io多路复用
rlist = [sockfd]
wlist = []
xlist = []


#select循环监听客户端
while True:

    rs,ws,xs = select(rlist,wlist,xlist)
    # 遍历列表
    for r in rs:
        #根据遍历到的io的不同 受用不同的if 情况处理
        if r is sockfd:
            connfd, addr = sockfd.accept()
            print("Connected")
            rlist.append(connfd)
        elif r is connfd:
            data = r.recv(1024)
            if not data:
                r.close()
                rlist.remove(r)
                continue
            print(data.decode())
            wlist.append(r)
    for w in ws:
        if w is connfd:
            w.send(b"ok")
            wlist.remove(w)






