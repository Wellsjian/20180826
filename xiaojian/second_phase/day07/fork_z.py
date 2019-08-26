"""
僵尸进程
"""
import os

pid = os.fork()

if pid < 0:
    pass
elif pid == 0 :
    print("Child pid",os.getpid())
    os._exit(0)
else:
    while True:
        pass




