"""
使用UDP  完成单词查询，要求一个服务端拥有单词本，从客户端可以循环输入单词

得到单词解释 ，客户端可以直接回车或则发送特殊字符退出
"""

from socket import *
from day04.exersice01 import *

# from exersice03 import *

sockfd = socket(AF_INET, SOCK_DGRAM)

sockfd.bind(("172.40.74.177", 22222))

# obj = open("../day04/dict.txt", "r+")
while True:
    print("wait...")
    data, addr = sockfd.recvfrom(1024)
    result = get_dict(data.decode())

    sockfd.sendto(result.encode(), addr)
