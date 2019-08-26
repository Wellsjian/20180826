"""
共享内存 通信  value
"""
from multiprocessing import Process
from multiprocessing import Value
import random, time, os

# 创建共享内存
money = Value("i", 5000)


# 修改共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1, 1000)


def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100, 800)

p = Process(target=man)
p1 = Process(target=girl)

p.start()
p1.start()

p.join()
p1.join()

# 父进程中获取内存资源
print("一月余额:",money.value)
