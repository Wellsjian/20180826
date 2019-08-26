"""
HTTP  协议测试
"""

from socket import  *

sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.bind(("0.0.0.0",11111))
sockfd.listen(3)

connfd , addr = sockfd.accept()
print("connect with",addr)

data = connfd.recv(1024)

data1 = """
HTTP/1.1 200 OK
Content_Type:text/html

<h1>Hello word<h1>
"""

connfd.send(data1.encode())

print(data)





