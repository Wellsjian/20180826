"""
file 文件操作  读取
    1.打开文件
    2.开始你的读写
    3.关闭文件

"""

# 读文件
"""
1.打开文件
obj = open("./exersice01","r+")
obj1 = open("./jmc/快速排序.gif","rb")
2.读文件
# while True:
#     num = obj1.read(1024)
#     if not obj1.read:
#         break
#     print(num)

# data = obj.readline()
# print(data)
# data = obj.readline()
# print(data)
# print(obj.read(6))
# 读取所有内容,每行作为列表中的一个元素
# data = obj.readlines()
# print(data)

# 通过for循环，每次获取一行
for line in obj:
    print(line)
3.关闭文件.
# obj.close()

"""


#写文件
"""
obj = open("./exersice01","wb")
# 如果是wb,则写入的必须是字节串,通过字符串.encode()来转换为字节串
#写文件操作
obj.write("搞不明白你\n".encode())
obj.write("怎么能这样".encode())

obj.writelines([b"abc",b"def"])
#关闭操作
obj.close()
"""


"""
with语句块
"""

with open("./exersice01","r") as obj:
    print(obj.read())

# 语句结束,自动销毁
    









