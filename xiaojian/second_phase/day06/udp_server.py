"""
UDP  套接字服务端
"""

from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(("172.40.74.177", 22222))

while True:
    print("please give me data and adress")
    data, addr = sockfd.recvfrom(1024)
    print(addr)
    print("Message is ", data.decode())

    n = sockfd.sendto(b"Receive", addr)
    print("aleady sent %d bytes" % n)

    if not data:
        break

sockfd.close()
