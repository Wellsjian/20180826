"""
身份运算符
"""
# is 判断的是变量的地址  = 判断的是变量的值
num1 = 1000
num2 = 1000
print(num1 is num2)     #True
print(id(num1))         #140393352561136
print(id(num2))         #140393352561584

num3 = num1             #140393352561136
print(num3 is num1)     #True

T