"""
练习：定义函数，在敌人列表中，查找姓名是“灭霸”的对象
"""
class Enemy:
    def __init__(self, name, attack, striking_distance, vitality):
        self.name = name
        self.attack = attack
        self.striking_distance = striking_distance
        self.vitality = vitality

    def print_self(self):
        print('%s的攻击力是：%d, 攻击距离为：%d 生命值是：%d' % (self.name, self.attack, self.striking_distance, self.vitality))

# 练习1：定义函数，在敌人列表中，查找姓名是“灭霸”的对象
def find01(list_target):
    for item in list_target:
        if item.name == "灭霸":
            return item
list01 = [
        Enemy("反叛者1" , 5, 20, 100),
        Enemy("灭霸" , 4, 30, 120),
        Enemy("反叛者3" , 3, 40, 150)
         ]
re = find01(list01)
re.print_self()

# 练习2：定义函数，在敌人列表中，查找攻击力是大于等于4的对象
def find02(list_target):
    list02 = []
    for item in list_target:
        if item.attack >= 4:
            list02.append(item)
    return list02

re1 = find02(list01)
for item in re1:
    item.print_self()


























