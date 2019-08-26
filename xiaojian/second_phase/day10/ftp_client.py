"""
FTP  客户端
"""

from socket import *
import time,sys

ADDR = ("127.0.0.1",22222) #服务器地址

#客户功能处理类
class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")
        data = self.sockfd.recv(128).decode()
        # 等待回复
        if data == "ok":
            # 一次接收文件链表
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    def do_get(self,cmd):
        filename = cmd.strip().split(" ")[-1]
        msg = "G " + filename
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            obj = open("./"+filename, "wb")
            while True:
                data = self.sockfd.recv(1024)
                if data == b"##":
                    break
                obj.write(data)
            obj.close()

        else:
            print(data)

    def do_put(self,cmd):

        path = cmd.strip().split(" ")[-1]
        filename = path.split("/")[-1]
        try:
            obj = open(filename,"rb")
        except Exception:
            print("文件不存在")
            return
        msg = "P " + filename
        self.sockfd.send(msg.encode())
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == "ok":
            while True:
                data = obj.read(1024)
                if not data :
                    #发送完毕信息,避免粘包
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            obj.close()
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b"Q")
        data = self.sockfd.recv(1024).decode()
        if data == "ok":
            self.sockfd.close()
            sys.exit("THANKS")





#创建客户端网络
def main():
    sockfd = socket(AF_INET,SOCK_STREAM)
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    ftp = FTPClient(sockfd)
    while True:
        print("\n**************命令选项***************")
        print("================get list:=============")
        print("================get file:=============")
        print("================put file:=============")
        print("================quit:=================")
        cmd = input("输入命令:")

        if cmd.strip() == "list":
            ftp.do_list()

        elif cmd[:3] == "get":
            ftp.do_get(cmd)

        elif cmd[:3] == "put":
            ftp.do_put(cmd)

        elif cmd.strip() == "quit":
            ftp.do_quit()
        else:
            print("InputError")



        # sockfd.send(cmd.encode())


if __name__ == "__main__":
    main()
























