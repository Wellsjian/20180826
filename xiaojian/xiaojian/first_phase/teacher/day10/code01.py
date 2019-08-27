"""
  实例成员
  练习:exercise01.py
"""


class Enemy:
  pass

  # def __init__(self, name, atk):
  # 创建实例变量:
  #   self.name = name
  #   self.atk = atk

  def fun01(self):
    # 创建实例变量(建议写在init方法中)
    self.hp = 10


# e01 = Enemy("灭霸",9999)
# e01.name = "灭灭"

e01 = Enemy()
# 创建实例变量(不建议使用)
e01.name = "灭霸"
# 修改实例变量
e01.name = "灭灭"
e01.atk = 9999
print(e01.name, e01.atk)
print(e01.__dict__)

e02 = Enemy()
# print(e02.name)
e02.fun01()
print(e02.hp)
print(e02.__dict__)
