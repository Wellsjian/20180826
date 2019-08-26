"""
IO多路复用的 pool方法练习

poll_server 步骤

重点代码

>	【1】 创建套接字  作为监控IO
	【2】 将套接字register
	【3】 创建查找字典，并维护(要时刻与注册IO保持一致)
	【4】 循环监控IO发生
	【5】 处理发生的IO
"""

from socket import *
from select import *

# 创建监听套接字
HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST, PORT)

sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(ADDR)
sockfd.listen(3)

# 创建关注的IO对象
p = poll()

# 建立查找字典,通过fileno查找IO对象
fdmap = {sockfd.fileno(): sockfd}
# 关注IO
p.register(sockfd, POLLIN | POLLERR)

while True:
    events = p.poll()
    # 循环遍历发生的事件
    for fd, event in events:
        #区分事件进行处理
        if fd == sockfd.fileno():
            connfd, addr = fdmap[fd].accept()
            print("Connect from the port %d"%PORT)
            #添加新的关注IO对象
            p.register(connfd,POLLIN)
            #将IO添加到字典中,体现维护
            fdmap[connfd.fileno()] = connfd
        elif event & POLLIN:#按位与操作判定connfd 是否执行
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fdmap[fd])
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print("Receive:",data.decode())
            fdmap[fd].send(b"ok")