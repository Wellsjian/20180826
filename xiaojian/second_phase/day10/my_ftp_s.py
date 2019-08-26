"""ftp 文件服务器

***代码实现: day5/ftp***

功能
	【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
	【2】 客户端可以查看服务器文件库中有什么文件。
	【3】 客户端可以从文件库中下载文件到本地。
	【4】 客户端可以上传一个本地文件到文件库。
	【5】 使用print在客户端打印命令输入提示，引导操作
1.功能需求分析
2.技术分析
    服务端  客户端
    网络传输方式:tcp传输协议  下载文件必须可靠   时间长需要保持连接
    客户端采用多进程多线程并发通信同时操作文件
    服务端数据存储库
3.结构设计
    客户端 : 发起请求

    服务端 : 封装用类来封装
4.分析功能模块,指定编写流程
     网络并发模块
     进入文件库  entrance
     查看文件   list
     下载文件   get_filename
     上传文件   put_filename
     退出文件库  exit
5.协议设置
    文件列表查看:  只提供普通文件(非隐藏文件)
    客户端请求类型:  L  文件链表   查看文件
                   G  filename  下载文件
                    P  filename   上传文件
                    Q   退出  退出文件库
"""
from socket import *
from threading import Thread
import os ,time ,sys

HOST = "0.0.0.0"
PORT = 22222
ADDR = (HOST,PORT)
FTP = "/home/tarena/下载/wenjianku/"

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(3)

    print("Listen the port %d" %PORT)
    while True:
        try:
            connfd ,addr = sockfd.accept()
        except KeyboardInterrupt:
            sys.exit("Exit")
        except Exception as  e:
            print(e)
            continue
        ftp = FTPMyThead(connfd)
        ftp.setDaemon(True)
        ftp.start()
class FTPMyThead(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            print(data)
            if data == "L":
                self.do_list()
            elif data.split(" ")[0] == "G":
                self.do_get(data)

    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)

        files1 = ""
        for file in files:
            if file[0] != "." and os.path.isfile(FTP+file):
                files1 += "\n" + file

        self.connfd.send(files1.encode())

    def do_get(self,data):
        filename = data.split(" ")[-1]
        try:
            obj = open(FTP+filename,"rb")
        except:
            self.connfd.send("该文件不存在".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)
        while True:
            data = obj.read(1024)
            print(data.decode())
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"**")
                obj.close()
                break
            self.connfd.send(data)





if __name__ == "__main__":
    main()









