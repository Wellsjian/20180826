"""
客户端.
    随时收发 ,多进程同时进行, 选择多进程编程
"""

from socket import *
import struct, os, sys

# 服务端地址
addr1 = ("127.0.0.1", 22222)


# 搭建UDP网络,启动主函数
def main():
    # 创建UDP套接字
    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 向服务端发送请求
    while True:
        name = input("please give your name:")
        msg = "L " + name
        sockfd.sendto(msg.encode(), addr1)
        data, addr = sockfd.recvfrom(1024)
        if data.decode() == "OK":
            print("you aleady get into the chat room.")
            break
        else:
            print(data.decode())
    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit(0)
    # 子进程来发消息
    elif pid == 0:
        sent_message(name, sockfd)
    # 父进程来收消息
    else:
        receive_message(sockfd)


# 对接收到的消息进行处理
def receive_message(sockfd):
    while True:
        try:
            data, addr = sockfd.recvfrom(1024)
        except KeyboardInterrupt:
            # data.decode() = "EXIT"
            sys.exit()
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + "\nPlease start your performance", end=" ")


# 发送消息
def sent_message(name, sockfd):
    while True:
        try:
            text = input("Please start your performance")
        except KeyboardInterrupt:
            text = "quit"
        # 退出
        if text == "quit":
            msg = "Q " + name
            sockfd.sendto(msg.encode(), addr1)
            sys.exit()
        msg = "C %s %s" % (name, text)
        sockfd.sendto(msg.encode(), addr1)


if __name__ == "__main__":
    main()
