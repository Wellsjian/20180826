"""
1.将一个文件从客户端发送到服务端，要求文件类型随意
2.将tcp两个程序和函数熟练一下
"""
import socket

#
# #服务端
#  # 套接字   套接字   套接字套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockfd.bind(("0.0.0.0", 22222))

sockfd.listen(5)

print("waiting for connect...")
connfd, addr = sockfd.accept()
print("connected")

file_name = connfd.recv(1024)
# print(file_name)
# name = "%s" % file_name.decode()
obj = open(file_name.decode(), "wb+")
n = connfd.send(b"finished")

while n:
    data = connfd.recv(1024)
    if not data:
        break
    obj.write(data)
    obj.read(1024)
    # n = connfd.send(data)
    # print("accped %d bytes" %n)

    # data = obj.read(1024)
    # if not  data:
    #     break
    # print(data.decode())
# connfd.close()
# sockfd.close()
