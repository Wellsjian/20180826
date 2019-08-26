


from socket import *
from multiprocessing import Process
from database10 import *
from time import sleep
import signal
import sys

HOST = "0.0.0.0"
PORT = 22222
ADDR =(HOST,PORT)

db = Database()

def do_request(connfd):
    db.create_cur()
    while True:
        data = connfd.recv(1024).decode()
        if not data or data[0] == "E":
            continue
        elif data[0] == "R":
            do_register(connfd,data)
        elif data[0] == "L":
            do_log_in(connfd,data)


#处理注册信息
def do_register(connfd,data):
    tmg = data.split(" ")
    name = tmg[1]
    passwd = tmg[2]

    if db.register(name,passwd):
        connfd.send(b"ok")
    else:
        connfd.send(b"Fail")
    return
#处理登录信息
def do_log_in(connfd,data):
    tmg = data.split(" ")
    name = tmg[1]
    passwd = tmg[2]
    if db.log_in(name,passwd):
        connfd.send(b"ok")
    else:
        connfd.send(b"Fail")
    return

# 搭建网络
def main():
    sockfd = socket(AF_INET, SOCK_STREAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Waiting for connect...")
    while True:
        try:
            connfd, addr = sockfd.accept()
            print("Connect from :",addr)
        except KeyboardInterrupt:
            sockfd.close()
            db.close()
            sys.exit("服务端退出")
        except Exception:
            continue
        p = Process(target=do_request,args=(connfd,))
        p.daemon = True
        p.start()




if __name__ == "__main__":
    main()




