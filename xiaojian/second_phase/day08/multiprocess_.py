"""
muitiprogress  实例一
"""
import multiprocessing as mp
from time import *

a = 1


def fun():
    print("开始第一个进程.")
    sleep(5)
    global a
    a = 100
    print("a:",a)
    print("子进程结束了.")

# 创建进程对象
p = mp.Process(target=fun)
p.start()#启动进程
sleep(3)
print("父进程干点啥")
p.join(1)#回收进程
print("a=",a)
