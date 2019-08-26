"""
  函数形式参数
"""


# 位置形参
def fun01(a, b, c):
  pass


# 星号元组形参: * 让实参个数无限制
def fun02(*args):
  print(args)


# 可以不传递参数
fun02()
# 也可以传递多个参数
fun02(1, 2)


# 练习:定义函数,数值相加的函数.
def adds(*args):
  sum = 0
  for item in args:
    sum += item
  return sum


print(adds(1, 2))
print(adds(1, 2, 3, 4, 5, 6, 78))


# 位置形参(必填) + 星号元组形参(可选)
def fun03(a, b, *args):
  print(a)
  print(b)
  print(args)


fun03(1, 2)
fun03(1, 2, 3)


# 命名关键字形参:要求实参必须以关键字传递
def fun04(*, a, b):
  print(a)
  print(b)


fun04(b=1, a=2)


# a b 是命名关键字传参
def fun05(*args, a, b):
  print(args)
  print(a)
  print(b)


fun05(1, 2, 3, 4, 5, a=1, b=2)

# print(*args, sep=' ', end='\n')
print(1, 2, sep="-")


# 双星号字典形参:实参可以传递多个关键字参数
def fun06(**kwargs):
  print(kwargs)

fun06(a=1,b=2,c=3)


# 万能传参:位置传参无限制,关键字传参无限制
def fun07(*args,**kwargs):
  pass

fun07()


def fun08(a,b,*args,c,d,**kwargs):
  pass








