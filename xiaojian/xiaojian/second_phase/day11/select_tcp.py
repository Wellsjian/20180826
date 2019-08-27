"""
IO 多路复用 select 方法的使用

重点代码
>select 实现tcp并发通信服务
rs, ws, xs=select(rlist, wlist, xlist[, timeout])

>	【1】将关注的IO放入对应的监控类别列表
	【2】通过select函数进行监控
	【3】遍历select返回值列表，确定就绪IO事件
	【4】处理发生的IO事件
"""
from socket import *
from select import select

HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST, PORT)

# 创建一个监听套接字对象作为关注的IO口
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(ADDR)
sockfd.listen(3)

# 设置关注IO列表,里面放的都是io对象
rlist = [sockfd]
wlist = []
xlist = []

#循环监控IO
while True:
    # 监控IO
    rs, ws, xs = select(rlist, wlist, xlist)

    # 遍历三个返回列表
    for r in rs:
        if r is sockfd:
            connfd , addr = r.accept()
            print("Connect from the port %d" %PORT)
            #增加新的io监控对象
            rlist.append(connfd)
        elif r is connfd:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print("Receive:",data.decode())
            #我们希望主动的处理需求
            wlist.append(r)



    for w in ws:
        if w is connfd:
            w.send(b"ok")
            wlist.remove(w) #使用后移除

    for x in xs:
        pass
