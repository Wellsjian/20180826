"""
event  线程互斥方法演示  实例

"""
from threading import Event
from threading import Thread
from time import sleep

print("天王盖地虎,宝塔镇河妖")

s = None
e = Event()

def 杨志荣():
    print("杨志荣前来拜山头")
    global s
    s= "天王盖地虎"
    # e.set()
t = Thread(target=杨志荣)
t.start()
print("说对口令,就是自己人.")
# e.wait()

if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神,你是对的人.")
else:
    print("干死他.....")

t.join()















