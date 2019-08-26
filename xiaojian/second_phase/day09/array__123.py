"""
共享内存通信  array
"""

from  multiprocessing import Process
from multiprocessing import Array

# shm = Array("i",[1,2,3])
# shm = Array("i",3)
shm = Array("c",b"hello")


def fun():
    for i in shm:
        shm[1]=b"E"
        print(i)

p = Process(target=fun)

p.start()
p.join()
for i in shm:
    print(i)