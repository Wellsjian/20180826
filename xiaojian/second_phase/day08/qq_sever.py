"""
服务端
>功能 ： 类似qq群功能
	【1】 有人进入聊天室需要输入姓名，姓名不能重复
	【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
	【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
	【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
	【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx

聊天室思路流程:
1.功能需求分析
2.技术分析
    服务端  客户端

    链接服务   UDP
    用户信息存储
    客户端的收发消息: 多进程 ,放在同一个服务端,分别同时处理收发
3.结构设计
    采用函数封装
    注意 :   * 注释的添加  最好达到20%  文档字符串的编写
            * 功能的测试  尽量确保功能准确性
4.分析功能模块,指定编写流程
    *搭接网络连接  选择数据传输方式
    *进入聊天室
        客户端:
            1.输入姓名
            2.将信息发送给服务端
            3.收到服务端信息反馈
            4.进入聊天室或者重新输入名字
        服务端:
            1.收到客户端请求
            2.判断姓名是否存在
            3.反馈信息给客户端
            4.不允许进入结束,允许时将用户信息存入字典
            5.通知其他用户
    *聊天
        客户端:
            1.创建新的进程
            2.父进程收消息
            3.子进程发消息
        服务端:
            1.接收请求
            2.将消息发送给其他人
    *退出聊天室
        客户端:
            1.输入退出
            2.将请求发送给服务端
            3.结束进程  发送进程
            4.接收进程 接收exit  结束进程
        服务端:
            1.接收请求
            2.将退出消息发送给其他人
            3.
    *管理员消息
5.协议的设置   服务端与客户端的内部信息交互协议
    1.存储用户结构: {name:address}
    2.进入聊天室协议:
        *允许进入, 则服务端给客户端发送 "OK"
        *不允许进入,则发送原因
    3.请求类型:
        *进入聊天室: L  name
        *聊天信息:  C   name message
        *退出聊天室  Q  name

"""

from socket import *
import os, sys, struct

# 服务端地址
addr = ("0.0.0.0", 22222)
# 创建字典,接收信息,存储用户信息
user_dict = {}


# 搭建UDP网络
def main():
    # UDP套接字
    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(addr)
    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息:" + msg
            sockfd.sendto(msg.encode(),addr)
    else:
        do_request(sockfd)


# 请求处理函数,循环接收来自客户端的请求
def do_request(sockfd):
    while True:
        data, addr = sockfd.recvfrom(1024)
        # 拆分请求
        tmp = data.decode().split(" ")
        # 根据请求类型执行相应内容
        if tmp[0] == "L":
            do_login(addr, sockfd, tmp[1])
        elif tmp[0] == "C":
            # 拼接消息内容
            text = " ".join(tmp[2:])
            do_chat(tmp[1], sockfd, text)
        elif tmp[0] == "Q":
            if tmp[1] not in user_dict:
                sockfd.sendto(b"EXIT", addr)
                continue
            do_quit(tmp[1], sockfd)


def do_quit(name, sockfd):
    msg = "\n%s leave the chart room." % name
    for i in user_dict:
        if i != name:
            sockfd.sendto(msg.encode(), user_dict[i])
        else:
            sockfd.sendto(b"EXIT", addr)
    user_dict[name] = None


def do_chat(name, sockfd, text):
    msg = "\n%s:%s" % (name, text)
    for i in user_dict:
        if i != name:
            sockfd.sendto(msg.encode(), user_dict[i])


def do_login(addr, sockfd, name):
    if name in user_dict:
        sockfd.sendto("this user name already exist".encode(), addr)
    sockfd.sendto(b"OK", addr)

    msg = "\nwelcom %s get into the chat room." % name

    for i in user_dict:
        sockfd.sendto(msg.encode(), user_dict[i])
    user_dict[name] = addr


if __name__ == "__main__":
    main()
