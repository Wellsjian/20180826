# 练习1:定义,敌人类,具有数据(姓名,攻击力,攻击距离,生命值)
#           行为(print_self 在控制台输出对象数据).
# 练习2:在控制台中录入3个敌人,存入列表中.
#      并在控制台中循环调用print_self方法.
class Enemy:
  def __init__(self, name, atk, distance, hp):
    self.name = name
    self.atk = atk
    self.atk_distance = distance
    self.hp = hp

  def print_self(self):
    print(self.name, self.atk, self.atk_distance, self.hp)


# e01 = Enemy("灭霸",9999,999999,99999)
# e01.print_self()
# list_all_enemy = []
# for i in range(3):
#   name = input("请输入姓名:")
#   atk = int(input("请输入攻击力:"))
#   distance = int(input("请输入攻击距离:"))
#   hp = int(input("请输入生命值:"))
#   e01 = Enemy(name, atk, distance, hp)
#   list_all_enemy.append(e01)
#   e01.print_self()

# 练习1:定义函数,在敌人列表中,查找姓名是"灭霸"的对象.
def find01(list_target):
  for item in list_target:
    if item.name == "灭霸":
      return item

# 测试
# list01 = [
#   Enemy("灭霸", 9999, 999999, 99999),
#   Enemy("蚩尤", 4000, 10, 500),
#   Enemy("钢铁侠", 5000, 30, 6000),
# ]
# re = find01(list01)
# re.print_self()

# 练习2:定义函数,在敌人列表中,查找攻击力大于等于5000的所有敌人.
# 15:40 上课
def find02(list_target):
  result = []
  for item in list_target:
    if item.atk >= 5000:
      result.append(item)
  return result

# 测试
list01 = [
  Enemy("灭霸", 9999, 999999, 99999),
  Enemy("蚩尤", 4000, 10, 500),
  Enemy("钢铁侠", 5000, 30, 6000),
]
re = find02(list01)
for item in re:
  item.print_self()












