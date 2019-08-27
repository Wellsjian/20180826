"""
进程对象属性  实例
"""
from multiprocessing import Process as p
from time import sleep,ctime

def fun():
    for i in range(5):
        sleep(5)
        print(ctime())


pr = p(target=fun)
p.daemon = True  #子进程会随着父进程的退出而结束
pr.start()
print(pr.name)  #名称
print(pr.is_alive()) #生命周期
print(pr.pid)  #pid









