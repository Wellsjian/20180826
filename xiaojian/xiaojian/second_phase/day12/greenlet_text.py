"""
协程运行   greenlet
"""

from greenlet import greenlet


def fun1():
    print("执行小建")
    gr2.switch()
    print("结束小建")
    gr2.switch()

def fun2():
    print("执行大建")
    gr1.switch()
    print("结束大建")


gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()  #选择执行
# gr2.switch()