"""
  运算符
  1. 逻辑运算符(与  或  非)
    bool 关系  bool
  17:00
"""

# 与 and 表示 并且 的关系 (都得满足) -->  一假俱假
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# 或 or 表示 或者 的关系 (一个满足就行) -->  一真俱真
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# 非 not 表示 取反的关系
print(not True)  # False

# 练习:在控制台中获取一个年份
# 判断输入的是否是闰年
# 条件1: 能被4整除但是不能被100整除
# 条件2: 能被400整除

year = int(input("请输入年份:"))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(result)
