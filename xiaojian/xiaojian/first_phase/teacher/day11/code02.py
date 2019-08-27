"""
   封装数据2:使用属性property封装(不常用写法)
"""


class Wife:
  """
    老婆
  """

  def __init__(self, name, age):
    self.name = name
    # 通过方法操作数据
    # 本质操作的是类变量
    self.age = age
    # self.set_age(age)

  def get_age(self):
    return self.__age

  def set_age(self, value):
    if 28 <= value <= 32:
      self.__age = value
    else:
      raise Exception("我不要")

  # 拦截 对数据的操作,转为调用读写方法.
  age = property(get_age, set_age)
  # property对象内部通过python描述符协议实现的


w01 = Wife("丽丽", 30)
# 通过方法,读取变量
print(w01.age)# 本质操作的是类变量
# print(w01.get_age())
print(w01.__dict__)
