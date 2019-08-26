from socket import *
import os,time,sys,signal

#搭建网络通信,构建tcp协议网络
HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)

#创建套接字对象
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

# 进程销毁后,由于没有父进程的处理,会产生僵尸进程,所以通过忽略子进程发出的回收请求让操作系统处理一下
signal.signal(signal.SIGCHLD,signal.SIG_IGN)


def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b"ok")


#循环处理客户要求.每当一个客户需要连接时,创建一个新的进程来处理,客户端结束时,进程随之销毁
print("listen to the connect.....")
while True:
    #对接受的客户端进行try处理
    try:
        connfd ,addr = sockfd.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    print("Connected")
    #创建进程
    pid = os.fork()
    if pid == 0:
        sockfd.close()#对于子进程,sockfd是没有用的
        handle(connfd)
        os._exit(0)#退出子进程
    connfd.close()#对于父进程,connfd 是没有影响的





