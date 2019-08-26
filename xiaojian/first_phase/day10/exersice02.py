"""
1.  定义：敌人类
    具有数据（姓名，攻击力，攻击距离，生命值）
        行为（print——self ，在控制台中输出对象数据
2.在控制台录入三个敌人，存入列表
 并在控制台中循环调用print_self方法
"""


class Enemy:
    def __init__(self, name, attack, striking_distance, vitality):
        self.name = name
        self.atttack = attack
        self.striking_distance = striking_distance
        self.vitality = vitality

    def print_self(self):
        print('%s的攻击力是：%d, 攻击距离为：%d 生命值是：%d' % (self.name, self.atttack, self.striking_distance, self.vitality))


list01 = []
# enemy = Enemy("反叛者%d" , 5, 20, 100)
# enemy.print_self()
# list01.append(enemy)
for i in range(3):
    enemy = Enemy("反叛者%d"%i, 5, 20, 100)
    list01.append(enemy)
    enemy.print_self()
    print(enemy.__dict__)
