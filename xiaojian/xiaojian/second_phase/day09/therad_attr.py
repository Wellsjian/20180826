"""
线程的创建  ,  thead
"""

from threading import Thread
from time import sleep
import os

"""
a = 1
#线程函数
def music():
    for i in range(20):
        global a
        sleep(2)
        print("让我掉下眼泪的\n不止昨夜的酒\n让我依依不舍的\n不止你的温柔")
        print(os.getpid(),"\n余路还要走多久\n你攥着我的手\n让我感到为难的\n是挣扎的自由")
        print("a = %d"%a)
        a = 10000

#创建线程
t = Thread(target=music)
#线程开始
t.start()

for i in range(20):
    sleep(4)
    print(os.getpid(),"\n分别总是在九月\n回忆是思念的愁\n深秋嫩绿的垂柳\n亲吻着我额头")
    print("a : %d"%a)
#线程回收
t.join()
"""
"""
含有参数的线程的创建
"""

"""
def get_music(sec, name):
    print("线程开始吧 ")
    sleep(sec)
    print("线程你走吧 %s" % name)

job = []
for i in range(5):
    t = Thread(target=get_music, args=(5,), kwargs={"name": "校长跑路了"})
    t.start()
    job.append(t)
for i in job:
    i.join()
"""
"""
线程的属性 实例
"""
def get_music(sec, name):
    print("线程开始吧 ")
    sleep(sec)
    print("线程你走吧 %s" % name)

t = Thread(target=get_music,args=(5,), kwargs={"name": "校长跑路了"})
# t.daemon = True
t.setDaemon(True)
t.start()
sleep(6)
t.setName("tarena")
print(t.name)
print(t.getName())
print(t.is_alive())
print(t.isDaemon())














