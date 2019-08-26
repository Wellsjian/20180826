"""
使用UDP完成
从客户端循环输入学生信息,包含,编号.姓名 年龄 分数 ,将其发送到服务端

服务端将接收到的信息写入一个文件里,每个学生信息占一行
"""
from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(("0.0.0.0",22222))
obj = open("student_info","a+")

while True:

    data, addr =sockfd.recvfrom(1024)
    data1 = struct.unpack("i32sif",data)
    data2 = (data1[0] ,data1[1].decode() ,data1[2] ,data1[3])

    info = "%d  %-10s  %d  %.1f\n"%data2
    obj.write(info)
    data = "你好啊"


    sockfd.sendto(data.encode(),addr)















