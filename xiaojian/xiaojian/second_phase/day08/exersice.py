"""
作业:
    1.将父子进程拷贝文件的练习 ,用multiprocess模块中Process完成
    2.将fork 和 process 比较
    3.复习一下函数和类的使用
    4.总结下聊天室
"""

from multiprocessing import Process as p
from multiprocessing import Pool
import os
from time import sleep,ctime

number = os.path.getsize("1904")
obj = open("1904", "rb")
def get_top():
    obj1 = open("part01", "w+")
    data = obj.read(number//2).decode()
    print(data)
    obj1.write(data)
    obj.close()
    obj1.close()

def get_bottom():
    obj2 = open("part02", "w+")
    obj.seek(number//2)
    data = obj.read().decode()
    print(data)
    obj2.write(data)
    obj.close()
    obj2.close()

list = [get_top,get_bottom]

job = []
for i in list:
    pr = p(target=i)
    pr.start()
    job.append(pr)

for i in job:
    i.join()







