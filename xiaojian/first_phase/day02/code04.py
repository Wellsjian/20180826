"""
逻辑运算符
真值表
True True
True False
False True
False False
"""

# 与   and  并且的关系   --->   一假俱假
# print(True and True)        #True
# print(True and False)       #False
# print(False and True)       #False
# print(False and False)      #False


# 或   or  或者的关系    --->  一真俱真
# print(True or True)        #True
# print(True or False)       #True
# print(False or True)       #True
# print(False or False)      #False


# 非  not  取反的关系
# print(not False)


"""
在控制台上输入一个年份
判断是否为闰年
条件1：能被4整除但不能被100整除
条件2：能被400整除
"""

year = int(input("请输入一个年份："))

result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(result)
