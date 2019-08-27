"""
1.文件函数使用熟练(open.read.write)
2.从终端输入一个文件名称（包含路径）,如果该文件存在
则将该文件复制到当前目录下，命名为1904（要求文件是任意类型）
如果文件不存在，则打印该文件不存在


思路分析：
    1.同时打开两个文件，从一个文件读出，写入另一个文件

3.向一个文件写入日志，写入格式：
    1. 2019-1-1 12:12:12
       2019-1-1 12:12:13

    2.要求每隔一秒写入一次，每条占时间一行
    3.程序死循环，Ctrl+ c退出
    4.如果程序退出，重新启动时，要求跟上次内容衔接
"""
# dir_input = input("请输入查找的文件名（包括路径)：")
# try:
#     ob = open("/home/tarena/桌面/xiaojian/dir","rb")
# except:
#     print("该文件夹不存在。")
# else:
#     obj = open("/home/tarena/桌面/xiaojian/dir","wb")
#     while True:
#         data = ob.read(1024)
#         if not data:
#             break
#         obj.writelines(data)

# import os
# if os.path.exists("./dir"):
#     obj = open("./dir","rb")
#     read1 = obj.read()
#     obj1 = open("./1904","wb")
#     obj1.write(read1)
#     obj.close()
#     obj1.close()
# else:
#     print("该文件不存在")


import time


# def log():
#     obj2 = open("./log","a+")
#     result = 0
#     while True:
#         result += 1
#         time01 = time.localtime()
#         time02 = time.strftime("%y-%m-%d %H:%M:%S", time01)
#         time.sleep(1)
#         obj2.write(str(result))
#         obj2.write("\t")
#         obj2.write(time02)
#         obj2.write("\n")
#         obj2.flush()



def log1():
    obj2 = open("./log1", "a+")
    print(obj2)
    result = 0
    obj2.seek(0, 0)
    for line in obj2:
        result += 1
    while True:
        result += 1
        time.sleep(1)
        s = "%d   %s\n" % (result, time.ctime())
        obj2.writelines(s)
        obj2.flush()


log1()
