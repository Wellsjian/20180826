"""
创建进程池  及其演示
"""
from multiprocessing import Pool
from time import sleep, ctime


def work(msg):
    sleep(2)
    print(msg)
    return ctime()


# 创建进程池
pool = Pool(10)
# 添加事件
for i in range(20):
    msg = "真期待,小园%d" % i
    # r 为 事件返回值
    r = pool.apply_async(work, args=(msg,))
# 关闭进程池
pool.close()
# 回收进程池
pool.join()

print(r.get())
