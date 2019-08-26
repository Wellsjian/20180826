"""
  核心数据类型
  练习:exercise02.py
"""

#1. None
# 作用1:用于占位
# 创建变量name01,但暂时"不存储数据".
# name01 = None
# name01 = "张三丰"

# 作用2:用于解除变量绑定关系
name01 = "张三丰"
name01 = None


# 2. 整形int
# 十进制
num01 = 18
# 二进制(0  1   10   11  100   101 ....)
num02 = 0b11
# 八进制(0 1 ... 7  10...)
num03 = 0o10
# 十六进制(0 1 ..9 a(10) -- f(15)  10(16))
num04 = 0xa
print(num04)

t = type(num02)# int
print(t)

# 3.浮点型float
f01 = 0.0
f02= 0.2e2
print(f02)
print(type(f01))

# 4. 字符串 str
s01 = "张无忌+++"

# 5.复数 complex
c01 = 3 + 1j
print(type(c01))

# 6. 布尔 bool
b01 = True # 真   对
b01 = False # 假  错
print(type(b01)) # 打印类型








