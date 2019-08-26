"""
练习：创建敌人类， 具有数据 攻击力 血量
        保证数据的范围  10-50
        保证血量的范围   0-100
"""


class Enemy:
    def __init__(self, attack, blood):
        self.attack = attack
        self.blood = blood

    @property
    def attack(self):
        return self.__attack

    @property
    def blood(self):
        return self.__blood

    @attack.setter
    def attack(self, value):
        if 10 <= value <= 50:
            self.__attack = value

    @blood.setter
    def blood(self, value):
        if 10 <= value <= 50:
            self.__blood = value
        else:
            raise Exception("超过攻击力范围.")


e01 = Enemy(20, 45)
print(e01.blood)
print(e01.__dict__)

# 总结：
