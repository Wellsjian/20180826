def fun():
    print("你好吗")
    yield
    print("我很好")

f = fun()
for i in f:
    print(i)
# print(f.__next__())
# print(f.__next__())