"""
管道通信 Pipe 实例
"""

from multiprocessing import Pipe
from multiprocessing import Process
import os, time, sys

# 创建管道对象
fd1, fd2 = Pipe(duplex=True)

def read():
    while True:
        data = fd1.recv() #从管道获取消息
        print(data +"  "+ "小李同意了")
        msg = data +"  "+ "小王恋爱了"
        fd1.send(msg)

def write():
    while True:
        time.sleep(2)
        fd2.send(time.ctime())
        data = fd2.recv()
        print(data)

p1 = Process(target=read)
p2 = Process(target=write)
p1.start()
p2.start()
p1.join()
p2.join()
