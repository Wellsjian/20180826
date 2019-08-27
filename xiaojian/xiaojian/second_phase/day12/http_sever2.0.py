"""
HTTP  2.0
接口设计:
    1.提供句柄,通过句柄调用属性和方法
        obj = open()
        lock = Lock()
    2.实例化对象,通过对象设置,启动服务
        t = Thread()
        p = Process()

    3.根据功能需求,无法帮助用户决定的内容,通过参数传递
    4.能够解决的问题,不要让用户去解决,需要用户解决的问题可以用重写的方法去解决
技术分析:
    HTTP 协议
思路分析
    1.使用类进行封装
    2.从用户的角度决定代码的编写
"""

# 具体HTTP  sever功能.

from socket import *
from select import *


class HTTPSever:
    def __init__(self, host, port, dir):
        self.addrss = (host, port)
        self.host = host
        self.port = port
        self.dir = dir
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.addrss)

    # 启动服务
    def server_forver(self):
        self.sockfd.listen(5)
        print("listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            self.do_rlist(rs)

    # 具体处理请求
    def handle(self, connfd):
        request = connfd.recv(1024)
        if not request:
            connfd.close()
            self.rlist.remove(connfd)
            return

        # 提取请求内容

        request_line = request.splitlines()[0]
        info = request_line.decode().split(" ")[1]
        print(connfd.getpeername(), ":", info)
        if info == "/" or info[-5:] == ".html":
            self.get_html(connfd, info)
        else:
            self.get_data(connfd,info)
    def get_data(self,connfd,info):
        response = "HTTP/1.1 200 ok\r\n"
        response += "\r\n"
        response += "<h1>Waiting for the HTTPSEVER 3.0<h1>"
        connfd.send(response.encode())

    def get_html(self,connfd,info):
        if info == "/":
            html_name = self.dir + "/index.html"
        else:
            html_name = self.dir + info
        try:
            obj = open(html_name)
        except Exception:
            response = "HTTP/1.1 404 not found\r\n"
            response += "Content_Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>sorry.....<h1>"
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content_Type:text/html\r\n"
            response += "\r\n"
            response += obj.read()
        finally:
            connfd.send(response.encode())


    # 具体处理rlist里的监控信号
    def do_rlist(self, rs):
        for r in rs:
            if r is self.sockfd:
                connfd, addr = self.sockfd.accept()
                print("Connect from ", addr)
                self.rlist.append(connfd)
            else:
                self.handle(r)


if __name__ == "__main__":
    # 希望通过HTTPSever类快速搭建http服务,用以展示自己的网页
    # HOST = "0.0.0.0"
    # PORT = 22222
    # ADDR = (HOST, PORT)
    # DIR = "./static"
    HOST = "172.40.74.151"
    PORT = 8888
    DIR ="./hfklswn"
    # 实例化对象
    httpfd = HTTPSever(HOST, PORT, DIR)
    # 启动HTTP服务
    httpfd.server_forver()
