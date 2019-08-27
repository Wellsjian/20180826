"""
  静态方法:
  将函数 放到 类中,就是静态方法.
"""


# # 表示向右01
# def get_right():
#   return Vector2(0, 1)
# # 表示向上01
# def get_up():
#   return Vector2(-1, 0)

class Vector2:
  """
    向量
  """

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @staticmethod  # 调用当前方法时,不会自动传递任何信息.
  def get_right():
    return Vector2(0, 1)

  @staticmethod
  def get_up():
    return Vector2(-1, 0)

  @staticmethod
  def get_left():
    return Vector2(0, -1)

  @staticmethod
  def get_down():
    return Vector2(1, 0)


# 点
pos01 = Vector2(1, 2)
# 通过静态方法,获取向右的方向
right = Vector2.get_right()
# 表示 pos01 点向右: 点 + 方向
pos02 = Vector2(pos01.x + right.x, pos01.y + right.y)
print(pos02.x, pos02.y)

"""
  00   01   02   03  04
  10   11   12   13  14
  20   21   22   23  24
"""

# 练习:定义类方法,获取向左的方向,
#     定义类方法,获取向下的方向,
#     表示 02点,向左的点.
pos03 = Vector2(0, 2)
left = Vector2.get_left()
x = pos03.x + left.x
y = pos03.y + left.y
pos04 = Vector2(x, y)
print(pos04.x,pos04.y)
