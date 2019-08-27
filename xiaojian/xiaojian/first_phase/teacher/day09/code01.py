"""
  类和对象
"""


class Wife:
  """
    老婆   17:15
  """

  def __init__(self, name, age):
    # 数据成员
    self.name = name
    self.age = age

  def play(self):
    print(self.name + "打游戏")


# 对象
w01 = Wife("丽丽", 23)
w01.play()

w02 = Wife("莹莹", 26)
w02.play()
