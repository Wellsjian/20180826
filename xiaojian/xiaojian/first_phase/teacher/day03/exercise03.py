"""
  练习:在控制台中获取两个数字,一个运算符(+-*/).
      根据运算符,计算两个数字.
      备注:如果输入的运算符有误,提示:运算符输入错误.
      14:20
"""

number_one = float(input("请输入第一个数字:"))
operator = input("请输入运算符:")
number_two = float(input("请输入第二个数字:"))
if operator == "+":
  print("结果是:" + str(number_one + number_two))
elif operator == "-":
  print("结果是:" + str(number_one - number_two))
elif operator == "*":
  print("结果是:" + str(number_one * number_two))
elif operator == "/":
  print("结果是:" + str(number_one / number_two))
else:
  print("运算符输入错误")



