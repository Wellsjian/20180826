from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)

addess = ("172.40.74.177", 22222)

while True:
    data = input("please give me a word:")

    sockfd.sendto(data.encode(), addess)

    data1,addess = sockfd.recvfrom(1024)
    print(data1.decode())
