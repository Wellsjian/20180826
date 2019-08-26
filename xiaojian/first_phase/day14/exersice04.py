"""
练习：手雷爆炸了，可能伤害敌人，玩家
     还可能伤害到其他为止的事物
"""

class AntitankGrenade:
    # def __init__(self, name):
    #     self.name = name

    def explode(self,name_type):
        name_type.hurt(10)

class Object:
    def hurt(self,value):
        pass
# *************************************************************************************************************

class Enemy(Object):
    def hurt(self,value):
        pass
class People(Object):
    def hurt(self,value):
        print("玩家受伤了，掉血 滴，碎屏")


g01 = AntitankGrenade()
p01 = People()
g01.explode(p01)






















