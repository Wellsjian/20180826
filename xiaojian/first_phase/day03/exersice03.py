# 练习
#
# 在控制台中获取两个数字，一个运算符，根据运算符
# 计算两个数字
# 备注：如果输入不是运算符，提示运算符输入错误


number1 = float(input("请输入第一个数："))
number2 = float(input("请输入第二个数："))
opreator = input("请输入运算符：")

if opreator == "+":
    result = number1 + number2
    print("%s %s %s = %s" % (number1, opreator, number2,result))
elif opreator == "-":
    result = number1 - number2
    print("%s %s %s = %s" % (number1, opreator, number2,result))
elif opreator == "*":
    result = number1 * number2
    print("%s %s %s = %s" % (number1, opreator, number2,result))
elif opreator == "/":
    result = number1 / number2
    print("%s %s %s = %s" % (number1, opreator, number2,result))
else:
    print("您的运算符输入有误")








