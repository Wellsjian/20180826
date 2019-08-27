"""
1.创建UDP套接字
2.设置套接字可以接受广播
3.选择接受端口
"""

from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 让套接字可以接受广播
sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

sockfd.bind(("172.40.74.255", 7777))

while True:
    data, addr = sockfd.recvfrom(1024)
    print(data.decode())
