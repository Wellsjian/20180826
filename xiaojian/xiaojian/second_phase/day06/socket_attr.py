"""
套接字属性
"""

from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)
# 设置套接字端口立即运行
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sockfd.bind(("172.40.74.177", 22222))

sockfd.listen(5)

connfd, addr = sockfd.accept()

print(sockfd.family)  # AddressFamily.AF_INET,获取协议地址类型

print(sockfd.type)  # SocketKind.SOCK_STREAM,获取套接字地址类型

print(sockfd.getsockname())  # ('172.40.74.177', 22222),获取绑定的IP地址

print(sockfd.fileno())  # 3 , 获取文件描述符

print(connfd.getpeername())  # 获取连接的客户端地址

print(sockfd.getsockopt(SOL_SOCKET,SO_REUSEADDR))
