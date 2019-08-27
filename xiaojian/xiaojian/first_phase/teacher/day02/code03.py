"""
  运算符
  1. 算数运算符
  2. 增强运算符
  3. 比较运算符
  练习:exercise03.py  exercise04.py
      exercise05.py  exercise06.py
"""

number01 = 5
number02 = 2
# / 结果是浮点型
# result = number01 / number02
# // 结果是整型  地板除
result = number01 // number02
# 取余数
result = number01 % number02
print(result)

# 取余作用1:判断一个整数能否被另外一个整数整除
number03 = 68
# 判断number03能否被8整除
re = number03 % 8 == 0
print(re)

# 取余作用2:获取个位
number04 = 1237
print(number04 % 10)

# 8 * 8 * 8
print(8 ** 3)

number05 = 2
# 累加(变量与另外一个数据做数学运算,结果又赋值给自身)
# number05 = number05 + 1
number05 += 1

# 字符串不能与整数做算数运算
number = int(input("请输入整数:"))
print(number + 1)




















