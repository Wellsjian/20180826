"""
创建父子进程,复制一个文件,各自复制一半到新的文件中

总结:
   1.父进程中生成文件描述符,子进程从父进程拷贝,此时父子进程
   对该文件的描述符的使用会产生相互影响
   2.如果父子进程中各自生成自己的文件描述符,则不会产生影响

"""

import os


# obj = open("./1904","rb")
# obj1 = open("dict1.txt","w")
# obj2 = open("dict2.txt","w")

number = os.path.getsize("1904")//2

pid = os.fork()


def get_top():
    global obj, data
    obj = open("./1904", "rb")
    obj1 = open("dict1.txt", "w")
    data = obj.read(number).decode()
    obj1.write(data)
    obj1.close()
    obj.close()


def get_bottom():
    global obj, data
    obj = open("./1904", "rb")
    obj2 = open("dict2.txt", "w")
    obj.seek(number)
    while True:
        data = obj.read().decode()
        if not data:
            break
        obj2.write(data)
    obj2.close()
    obj.close()


if pid <  0:
    print("Error")

elif pid == 0 :
    p = os.fork()
    if p == 0:
        get_top()
    else:
        os._exit(0)
else:
    os.wait()
    get_bottom()






