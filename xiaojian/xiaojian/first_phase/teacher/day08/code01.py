"""
  函数:
  返回值：函数的结果
  练习:exercise01.py
      exercise02.py
      exercise03.py
      exercise04.py 
"""


# -------------语法------------------
def fun01():
  print("fun01执行喽")


# None
result = fun01()
print(result)


def fun02():
  print("fun02执行喽")
  # 返回 数据
  # 退出方法
  return 100
  print("fun02又执行喽")


# None
result = fun02()
print(result)


# ---------------定义函数,两个数值相加------------
# 分而治之
# 函数职责单一

def add(number_one, number_two):
  # 逻辑处理
  result = number_one + number_two
  # 返回结果
  return result


# 获取
a = float(input("请输入第一个数字："))
number_two = float(input("请输入第二个数字："))
re = add(a, number_two)
# 显示结果
print("结果是:" + str(re))
