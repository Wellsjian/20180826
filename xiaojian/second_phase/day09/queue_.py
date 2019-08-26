"""
消息队列通信   Queue
"""
from multiprocessing import Queue
from multiprocessing import Process
import os, time, sys, random
#创建队列
q = Queue(5)
#定义请求
def request():
    for i in range(10):
        x =random.randint(1, 100)
        y =random.randint(1, 100)
        print("----------------------")
        q.put((x,y))
#处理请求
def handle():
    while True:
        time.sleep(1)
        try:
            a,b = q.get(timeout=5)
        except:
            break
        else:
            print("%d + %d = %d" %(a, b, a+b))
#创建进程
p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()
