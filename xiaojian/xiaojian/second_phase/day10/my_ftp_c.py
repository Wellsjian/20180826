
from socket import *
import  time,os,sys,time

HOST = "127.0.0.1"
PORT = 22222
ADDR = (HOST,PORT)


class FTPThread:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b"L")
        data = self.sockfd.recv(1024)
        if data.decode() == "ok":
            data = self.sockfd.recv(1024).decode()
            print(data)

    def do_get(self,cmd):
        filename = cmd.strip().split(" ")[-1]
        msg = "G " + filename
        self.sockfd.send(msg.encode())
        data = self.sockfd.recv(1024).decode()
        if data == "ok":
            obj = open(filename,"wb")
            while True:
                data = self.sockfd.recv(1024)
                print(data.decode())
                if data ==b"**":
                    break
                obj.write(data)
            obj.close()
        else:
            print(data)




def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    ftp = FTPThread(sockfd)
    while True:
        print("""
        1)list
        2)get filename
        3)put filename
        4)quit
        """)
        cmd = input("请输入指令")
        if cmd == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            ftp.do_get(cmd)


if __name__ == "__main__":
    main()
