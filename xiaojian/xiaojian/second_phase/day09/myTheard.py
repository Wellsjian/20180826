"""
thread class
自定义线程类演示 实例
"""
from threading import Thread

"""
1.继承Thread
2.重写__init__方法和run方法
"""
"""
class MyThread(Thread):
    def __init__(self,attr):
        self.attr = attr
        super(MyThread, self).__init__()

    def fun1(self):
        print("来吧,猴孩子")

    def fun2(self):
        print("来吧,猫孩子")

    def run(self):
        self.fun1()
        self.fun2()

t = MyThread("小东")
t.start()
t.join()
"""

"""
练习:  自定义线程类
        通过完成上面的类.使下面的程序可以运行
"""
from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        self._target(*self._args, **self._kwargs)


def player(sec, song):
    for i in range(3):
        print("Playing %s : %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={"song": "凉凉"})
t.start()
t.join()
