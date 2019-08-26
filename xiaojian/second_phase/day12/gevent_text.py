"""
gevent
"""
import gevent

def foo(a,b):
    print("Running foo ...",a,b)
    print("foo exit")

f = gevent.spawn(foo(1,2))
gevent.sleep(3)

#阻塞等待[]中的协程结束
gevent.joinall([f])



