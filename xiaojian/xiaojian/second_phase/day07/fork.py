"""
基于fork 的多进程创建演示
"""

import os
import time

pid = os.fork()

if pid < 0:
    print("Create process failed.")
elif pid == 0:
    time.sleep(3)
    print("New process.")

else:
    time.sleep(5)
    print("old process.")

print("Fork test end.")
