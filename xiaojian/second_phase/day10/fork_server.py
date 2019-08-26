"""
基于fork搭建基础网络并发通信模型

重点代码

思路分析
1.每当有一个客户端链接就创建一个新的进程作为客户端请求处理进程
2.客户端如果结束,对应进程应该销毁
"""
from socket import *
import os,signal

HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port %d......" %PORT)

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()


while True:
    try:
       c , addr = sockfd.accept()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    #创建子进程,处理客户端
    pid = os.fork()
    if pid == 0:
        sockfd.close()
        handle(c)
        os._exit(0)#handle()处理完客户需求则退出子进程.
     #connfd 对父进程没用
    c.close()
           #无论创建出错,还是父进程都需要返回接收请求









