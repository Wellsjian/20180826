"""
  练习:
  定义类:具体事物,抽象化的过程.
  创建对象:抽象事物,具体化的过程.

  定义汽车类,数据(品牌,型号,价格),
          行为(启动,行驶...).

  创建至少2个对象.
  17:28
"""


class Car:
  # 两个下划线开头,两个下划线结尾.
  def __init__(self, str_brand, str_model, price=50000):
    # self 是调用当前方法的对象地址
    self.brand = str_brand
    self.model = str_model
    self.price = price

  def start(self):
    """
      启动
    """
    # self 是调用当前方法的对象地址
    print(self.brand + "汽车启动")

  def move(self):
    """
      行驶
    """
    print(self.brand + "汽车行驶")


# 创建对象,调用__init__方法
c01 = Car("宝马", "X5", 600000)
# 自动传递对象地址到start方法,作为第一个参数self
c01.start()
c01.move()

# 所有方法被对象共享
# 此时调用的init与start等方法,
# 和刚才是一个.只不过传递的对象地址不同而已.
c02 = Car("比亚迪", "唐")
c02.start()
c02.move()
