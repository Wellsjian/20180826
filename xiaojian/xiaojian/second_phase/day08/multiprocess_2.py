"""
带参数的  multiprocess
"""

from multiprocessing import Process as p
from time import sleep as s

def worker(sec,name):
    for i in range(3):
        s(sec)
        print("I'm %s"%name)
        print("I'm working......")

# pr = p(target=worker,args=(2,"小圆"))
pr = p(target=worker,kwargs={"name":"小圆","sec":2})
pr.start()

pr.join()