"""
tcp_server.py  tcp套接编程   ： 服务端流程

重点代码
"""

import socket

# while True:
# 1.创建套接字对象
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, )
# 2.绑定地址
sockfd.bind(("0.0.0.0 ", 8888))
# 3.设置sockfd为监听套接字
sockfd.listen(5)
# 4.阻塞等待处理客户端链接
while True:
    print("waitting for connect.....")
    try:
        connfd, addr = sockfd.accept()
        print("connect from", addr)
    except KeyboardInterrupt:
        print("Sever exit")
        break
    # 5.接收消息
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("Mseeage:", data.decode())
        # 返回发送的字节数
        n = connfd.send(b"*****Thank You*****")
        print("Send %d bytes" % n)

    # 6.关闭套接字
    connfd.close()
sockfd.close()
