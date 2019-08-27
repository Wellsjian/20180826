# 练习:统计一个类,
#     创建了多少对象(记录init调用次数).画内存图
# 17:00 上课
class Enemy:
  count = 0

  @classmethod
  def print_count(cls):
    print("总共创建了%d个对象" % cls.count)

  def __init__(self):
    Enemy.count += 1


e01 = Enemy()
e02 = Enemy()
Enemy.print_count()
