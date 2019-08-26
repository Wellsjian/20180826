from multiprocessing import Pool
import os

number = os.path.getsize("1904")
obj = open("1904", "rb")


def get_top():
    obj1 = open("part03", "w+")
    data = obj.read(number // 2).decode()
    print(data)
    obj1.write(data)
    obj.close()
    obj1.close()


def get_bottom():
    obj2 = open("part04", "w+")
    obj.seek(number // 2)
    data = obj.read().decode()
    print(data)
    obj2.write(data)
    obj.close()
    obj2.close()


p = Pool()
list = [get_top, get_bottom]
for i in list:
    p.apply_async(i)
p.close()
p.join()
