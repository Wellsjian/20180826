"""
  运算符
  身份运算符
"""
num01 = 800
num02 = 1000
print(num01 is num02)  # False
# id函数,返回变量存储的地址.
print(id(num01))
print(id(num02))

# 文件时python,对下列代码进行了优化.创建的1000对象是一个.
num01 = 1000
num02 = 1000
print(id(num01))
print(id(num02))
print(num01 is num02)  # True

num03 = num01
print(num03 is num01)  # True
