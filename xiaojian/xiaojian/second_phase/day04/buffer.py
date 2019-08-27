"""
buffer  缓冲区
"""
# 刷新缓冲区条件
# 1.程序结束
# 2.obj.close函数
# 3.obj.flush函数
# 4.缓冲区满了
# 5.遇到行缓冲条件
# with open("./exersice01","a+") as obj:
#
#     while True:
#         str = input()
#         obj.write(str)
#         obj.flush()  #将缓冲内容写入磁盘
#


# 空洞文件
obj = open("exersice01","wb+")
print(obj)
# obj.write(b"start")
# obj.seek(1000,2)
# obj.write(b"end")
# obj.close()

# 通过IO对象获取对应的文件描述符
num = obj.fileno()
# print(num)
import os
# 1. 获取文件大小
os.path.getsize("exersice01")

# 2. 查看文件列表
os.listdir("exersice01")

# 3. 查看文件是否存在
os.path.exists("exersice01")

# 4. 判断文件类型
os.path.isfile("exersice01")

# 5. 删除文件
os.remove("exersice01")







