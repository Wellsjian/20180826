from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

addr = ("127.0.0.1",22222)

while True:

    aid = int(input("please input your ID:"))
    name = str(input("please input your name:"))
    age = int(input("please input your age:"))
    score = float(input("please input your score:"))

    data = struct.pack("i32sif",aid,name.encode(),age,score)

    sockfd.sendto(data,addr)

    data ,addr = sockfd.recvfrom(1024)
    print(data.decode())