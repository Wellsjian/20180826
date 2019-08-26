"""
面试题:可以 被for的条件
        对象具有__iter__（）方法
"""

list01 = [1,25,8,8,74,852,5]
# for 原理：
# 1.获取迭代器对象
iterable = list01.__iter__()
# 2.循环获取下一个元素
while True:
    try:
        item =  iterable.__next__()

# 3.异常处理
    except StopIteration:
        break

# 面试题 ：不使用for循环，获取字典记录

dict01 = {"张无忌":3,"赵敏":2}
iterable = dict01.__iter__()
while True:
    try:
        key = iterable.__next__()
        print(key,dict01[key])

    except StopIteration:
        break










