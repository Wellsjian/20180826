"""
客户端
"""
from socket import  *

sockfd = socket()

addr =("172.40.74.177",22222)
sockfd.connect(addr)
while True:
    obj = open("./exersice_client.py", "rb")
    # print(obj.name.split("/")[-1])

    sockfd.send((obj.name.split("/")[-1]).encode())
    data = sockfd.recv(1024)
    print(data.decode())
    while data:
        data1 = obj.read(1024)
        if not data1:
            break
        sockfd.send(data1)
    if not  obj:
        break

# data = sockfd.recv(1024)
# print(data)

sockfd.close()



