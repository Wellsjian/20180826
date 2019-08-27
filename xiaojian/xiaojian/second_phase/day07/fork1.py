import os
import time

a = 1

pid = os.fork()


if pid < 0:
    print("Create process failed")
elif pid == 0:
    time.sleep(1)
    print("old process")
    print(os.getpid())
    print(os.getppid())
    print("a =", a)
else:
    print("new process")
    print(pid)
    print(os.getpid())
    print(a)

print("Fork test end .", a)
