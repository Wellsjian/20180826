"""
  编码
  练习:exercise03.py
"""

name = "悟空"
# 修改变量name存储的地址
# 为什么不可变?:
# 如果将两个字,改变为三个字,很可能破坏其他对象的内存空间
# 所以字符串不能改变
name = "孙悟空"
print(name)

s01 = "b"
# 字 --> 数
num01 = ord(s01)
print(num01)

num02 = 97
# 数 --> 字
s02 = chr(num02)
print(s02)







