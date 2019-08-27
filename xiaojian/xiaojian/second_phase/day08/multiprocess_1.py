"""
muitiprocess  实例2
"""
from multiprocessing import Process as p
from time import sleep as s
import os

def fun1():
    s(2)
    print("吃饭,抽烟")
    print(os.getpid(),".....",os.getppid())
def fun2():
    s(2)
    print("睡觉,喝酒")
    print(os.getpid(),".....",os.getppid())
def fun3():
    s(2)
    print("想豆豆,打豆豆")
    print(os.getpid(),".....",os.getppid())

# things1 = [fun1(),fun2(),fun3()]
# print(id(fun1()))
things = [fun1,fun2,fun3]
print(id(fun1))
job = []
# 创建子进程
for i in things:
    pr = p(target=i)
    pr.start()
    print(pr.pid)
    job.append(pr)
#一起回收
for i in job:
    i.join()





