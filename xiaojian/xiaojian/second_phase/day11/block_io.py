"""
设置套接字为非阻塞IO,设置setblocking,,设置超时检测 settimeout

    如果没有客户端连接,每隔3秒填充一个日志
"""

from  socket import *
import time,os,sys
HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)

obj = open("log.txt","a+")

sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

# 设置套接字为非阻塞IO
# sockfd.setblocking(False)
# 超时检测
sockfd.settimeout(3)

while True:
    print("Waiting for connect.....")
    try:
        connfd,addr = sockfd.accept()
    except (BlockingIOError,timeout) as b:
        #如果没有客户端连接,则每隔3秒写一条日志
        obj.write("%s : %s\n"%(time.ctime(),b))
        obj.flush()
        time.sleep(3)
    else:
        print("Connnect from the port %d"%PORT)



