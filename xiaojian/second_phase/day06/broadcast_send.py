"""
广播  发送端
"""
from socket import *
import time

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#广播地址
addr = ("172.40.74.255",9999)
sockfd.bind(addr)

data = """
****************
我们是一个世界的人
****************
"""

while True:
    time.sleep(2)
    sockfd.sendto(data.encode(),addr)

