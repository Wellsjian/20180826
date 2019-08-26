"""
UDP  客户端
"""

from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

#服务端 地址
addr = (("172.40.74.177", 22222))

#循环发送消息
while True:
    data = input("please send the message:")

    sockfd.sendto(data.encode(),addr)

    msg, addr = sockfd.recvfrom(1024)
    print("i am received")

