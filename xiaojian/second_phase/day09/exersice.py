from multiprocessing import Process,Pipe,Pool,queues,Array,Value,Semaphore
from second_phase.day09.test import *
from threading import Thread
import os,time



# 使用单进程分别执行 count  io 10遍 记录时间
# start_time = time.time()
# for i in range(10):#6.322139263153076
#     count(1,2)
# print(time.time() - start_time)
#
#
# start_time = time.time()
# for i in range(10):#3.321495771408081
#     io()
# print(time.time() - start_time)

# 使用10个进程,每个进程执行count io 1次 记录时间
# start_time = time.time()
# jobs = []
# for i in range(10):
#     t = Process(target=count,args=(1,1))#1.5431368350982666
#     t.start()
#     jobs.append(t)
# for i in jobs:
#     i.join()
# print(time.time() - start_time)

# start_time = time.time()
# jobs = []
# for i in range(10):
#     t = Process(target=io)#1.0110893249511719
#     t.start()
#     jobs.append(t)
# for i in jobs:
#     i.join()
# print(time.time() - start_time)


# 使用10个线程,每个线程执行count io 1次 记录时间

# start_time = time.time()
# jobs = []
# for i in range(10):
#     t =Thread(target=count,args=(1,1))#10.65294623374939
#     t.start()
#     jobs.append(t)
# for i in jobs:
#     i.join()
# print(time.time() - start_time)

start_time = time.time()
jobs = []
for i in range(10):
    t = Thread(target=io)#3.827904224395752
    t.start()
    jobs.append(t)
for i in jobs:
    i.join()
print(time.time() - start_time)
























