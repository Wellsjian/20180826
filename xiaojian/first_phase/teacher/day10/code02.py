"""
  类成员(类变量/类方法)
  练习:exercise02.py
"""

class ICBC:
  """
    工商银行
  """
  # 类被加载时,类变量被创建.
  # 通过类变量,表示总行的钱
  total_money = 5000000

  @classmethod  # 调用当前方法时,自动传递类名(类地址).而不是对象地址
  def print_total_money(cls):
    # 表达类的行为,只能操作类变量,不能操作实例变量.
    print("总行的钱有:%d" % cls.total_money)

  def __init__(self, name, money):
    # 通过实例变量,表示支行的钱
    self.name = name
    self.money = money
    # 从总行中扣除当前支行使用的钱
    ICBC.total_money -= money


# 创建对象,创建实例变量
i01 = ICBC("天坛支行", 100000)
# 访问类变量
# print(ICBC.total_money)
# 访问类方法
ICBC.print_total_money()  # 自动传递类名,到类方法中.
i02 = ICBC("天安门支行", 200000)
print(ICBC.total_money)


