"""
练习
    1.（4,4,5,565,6,7）通过迭代器获取元素
    2.通过迭代器 获取字典
"""
tuple01 = (4,4,5,565,6,7)
iterable = tuple01.__iter__()
print(iterable)
while True:
    try:
        item = iterable.__next__()
        print(item)
    except StopIteration:
        break


dict01 = {"张无忌":3,"赵敏":2}

iterable = dict01.__iter__()


while True:
    try:
        key = iterable.__next__()
        print(key,dict01[key])

    except StopIteration:
        break







