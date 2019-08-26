from socket import *
import os
sock_file = './sock'
if os.path.exists(sock_file):
    os.remove(sock_file)
s = socket(AF_INET,SOCK_DGRAM)
s.bind('sock_file')
s.listen(3)
while True:
    c,addr = s.accept()
    print('connect from',addr)
    while True:
        data = c.recvfrom(1024)
        print(data.decode())



osi模型,tcp/udp差异http协议内容   三次握手四次挥手
tcp/ip图解
