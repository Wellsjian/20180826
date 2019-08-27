"""
wait 来处理僵尸
"""
# import os

# pid = os.fork()
#
# if pid < 0 :
#     print("create failed")
#
# elif pid == 0 :
#     print("child pid",os.getpid())
#     os._exit(5)
# else:
#     pid,status = os.wait()
#
#     print("pid:",pid)
#     print("status",os.WEXITSTATUS(status))
#
#     while True:
#         pass
#


"""
用创建二级子进程来处理僵尸进程
"""

# from time import sleep
# import os
#
# def f1():
#     for i in range(4):
#         sleep(2)
#         print("写代码")
# def f2():
#     for i in range(5):
#         sleep(2)
#         print("测代码")
# pid = os.fork()
#
#
# def get_two_progress():
#     p = os.fork()
#     if p == 0:
#         f2()
#     else:
#         os._exit(0)
#
#
# if pid < 0:
#     print("Error")
# elif pid == 0 :
#     get_two_progress()
# else:
#     os.wait()
#     f1()

"""
用signal信号方法处理僵尸进程
"""

import signal
import os

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
pid = os.fork()

if pid < 0:
    pass
elif pid == 0 :
    print("Child pid",os.getpid())
else:
    while True:
        pass























