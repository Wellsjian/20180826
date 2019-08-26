"""
  练习2:在控制台中依次获取2个变量
       将两个变量交换,再输出到控制台中.
       "请输入第一个变量:"
       "请输入第二个变量:"
       "第一个变量是:"xxx
       "第二个变量是:"yyy
  11:00
"""

number01 = input("请输入第一个变量:")
number02 = input("请输入第二个变量:")

# 借助第三个变量进行交换(跨语言的编程思想)
# temp = number01
# number01 = number02
# number02 = temp

# 直接交换(python 独特的方式)
number01,number02 = number02,number01

print("第一个变量是:"+number01)
print("第二个变量是:"+number02)
