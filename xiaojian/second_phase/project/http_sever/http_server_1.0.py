"""
HTTP 发送网页给浏览器
"""

from socket import *


# 处理客户端请求
def handle(connfd):
    request = connfd.recv(1024)
    # 防止客户端断开
    if not request:
        return
    request_line = request.splitlines()[0]
    # print(request_line)
    info = request.decode().split(" ")[1]
    if info == "/":
        with open("index.html") as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content_Type:text/html\r\n"
            response += "\r\n"
            response += f.read()

    else:
        with open("index.html") as f:
            response = "HTTP/1.1 404 not found\r\n"
            response += "Content_Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>sorry.....<h1>"

    connfd.send(response.encode())


# 搭建一个tcp网络
sockfd = socket(AF_INET, SOCK_STREAM)

sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sockfd.bind(("0.0.0.0", 22222))

sockfd.listen(6)

while True:
    connfd, addr = sockfd.accept()
    handle(connfd)  # 处理客户端请求
