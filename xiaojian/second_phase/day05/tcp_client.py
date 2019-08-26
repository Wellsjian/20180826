"""
tcp_client  客户端流程代码

重点代码

"""
from socket import  *

#创建套接字对象 ，默认为ipv4。流式套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#连接套接字
sockfd.connect(("127.0.0.1",22222))

#发送消息
while True:
    data = input("MSG>>:")
    if not data:
        break
    sockfd.send(data.encode())
    #接受消息
    data = sockfd.recv(1024)
    print("Sever:",data.decode())


sockfd.close()





