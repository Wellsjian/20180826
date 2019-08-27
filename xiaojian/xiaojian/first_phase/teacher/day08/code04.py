"""
  函数实际参数
"""


def fun01(a, b, c, d):
  print(a)
  print(b)
  print(c)
  print(d)


# 位置传参:实参与形参的位置[依次对应]
fun01(1, 2, 3, 4)

# -- 序列传参: * 号将序列拆分后与形参位置依次对应
list01 = [1, 2, 3, 4]
fun01(*list01)

# 关键字传参:实参根据形参的[名称进行对应]
fun01(b=1, c=2, d=3, a=4)
fun01(1, 2, d=5, c=2)  # 先位置传参,再关键字传参
# fun01(d=5, c=2,1, 2,)# 先关键字传参,再位置传参(错误)

# -- 字典传参: ** 将字典拆分后与形参的名字进行对应
dict01 = {"d": 4, "c": 3, "a": 1, "b": 2}
fun01(**dict01)


# 形参
#   -- 默认参数:如果不传递参数,可以使用默认值代替.
def fun02(a=0, b=0, c=0, d=0):
  print(a)
  print(b)
  print(c)
  print(d)


# 关键字传参 + 默认参数: 可以选择性的为形参赋值
fun02(b=2)  # 为参数b赋值
fun02(2)  # 为参数a赋值


# 练习:随意传递参数
# 根据小时/分钟/秒,计算总秒数.
def get_total_second(hour=0, minute=0, second=0):
  return hour * 3600 + minute * 60 + second


print(get_total_second(minute=2))
