

from socket import *
from getpass import getpass


HOST = "0.0.0.0"
PORT = 22222
ADDR =(HOST,PORT)

# 搭建网络
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.connect(ADDR)
#注册
def do_register():
    while True:
        name = input("name:")
        passwd = getpass()
        passwd1 = getpass("Again:")
        if (" " in name) or (" " in passwd):
            print("格式不对")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        msg = "R %s %s" %(name,passwd)
        sockfd.send(msg.encode())
        data = sockfd.recv(1024).decode()
        if data == "ok":
            print("注册成功")
        else:
            print('注册失败')
        return
def do_log_in():
    while True:
        name = input("name:")
        passwd = getpass()
        msg = "L %s %s"%(name,passwd)
        sockfd.send(msg.encode())
        data = sockfd.recv(1024).decode()
        print(data)
        if data == "ok":
            print("登陆成功")
        else:
            print("登录失败")
        return


def main():
    while True:
        print("""
*****************************
1)注册
2)登录
3)退出
*****************************
""")
        cmd = input("请输入选项:")
        if cmd == "1":
            do_register()
        elif cmd == "2":
           do_log_in()
        elif cmd == "3":
            pass
        if cmd == "1":
            pass





if __name__ == "__main__":
    main()