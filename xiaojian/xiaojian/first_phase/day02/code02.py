'''
核心数据类型
'''
# 1.空型 None
# 作用：
#     1.用于占位
#     2.用于解除变量的绑定关系
name = "张三丰"
name = None
print(name)


# 2.整形 int
#     二进制：0b开头，
#     八进制：0o开头，
#     十六进制：0x开头，
#
# 十进制：
# age = 18
# 二进制：
age = 0b10010
print(age)
# 八进制：
age = 0o10
print(age)
# 十六进制：
age = 0xc
print(age)


# 3.浮点型：float
#     科学计数法：1.23e-2代表小数0.0123
a = 1.23e-2
print(a)
print(type(a))


# 4.字符串 ：  用来记录文本信息，用双引号
s01 = "qwertyuiopasdfghjklzxcvbnm"

print(len(s01))

# 5. 复数  ：  complex
s = 3 + 2j
print(s)


# 6.布尔型  ：  bool
#     True 表示真  ，本质为1
#     False 表示假 ， 本质为0
a = True
print(a)











