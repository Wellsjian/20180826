"""
1.三合一
2.当天练习独立完成
3.  使用面向对象描述下列情景
        玩家攻击敌人，敌人受伤后掉血或者死亡，还可能死亡刁掉装备
        敌人攻击玩家，玩家受伤后掉血并且碎屏，还可能死亡游戏结束
4.  使用面向对象来描述下列场景
        张无忌 教 赵敏 打篮球
        赵敏 教 张无忌 画眉
        张无忌 上班赚了10000元
        赵敏 上班赚了5000元


        要求 ；遇到数据要进行数据封装
5.穷尽一切手段在互联网中收集封装的知识，并结合课堂所讲，总结为自己的东西话术，
为全国面向对象课程答辩峰会    做准备
"""

# 3.  使用面向对象描述下列情景
#         玩家攻击敌人，敌人受伤后掉血或者死亡，还可能死亡刁掉装备
#         敌人攻击玩家，玩家受伤后掉血并且碎屏，还可能死亡游戏结束
import random
#总结  ： 以上情景属于行为不同  ，所以定位两个类


class Person:
    def __init__(self, name, atk=5, hp=100):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def attack(self, enemy):
        enemy.damage(self.atk)

    def damage(self,value):
        self.hp -= value
        print("玩家受伤了.")
        print("碎屏")
        if self.hp <= 0:
            self.__death()
    def __death(self):
        print("玩家死亡了。")



class Enemy:
    def __init__(self, name, atk=3, hp=20):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def damage(self,value):
        self.hp -= value
        print("敌人受伤了.")
        if self.hp <= 0:
            self.__death()
    def __death(self):
        print("敌人死亡了。")

    def attack(self, person):
       person.damage(self.atk)


p1 = Person("无所畏惧")
e1 = Enemy("反叛者")
p1.attack(e1)
p1.attack(e1)
p1.attack(e1)
p1.attack(e1)







# 4.  使用面向对象来描述下列场景
#         张无忌 教 赵敏 打篮球
#         赵敏 教 张无忌 画眉
#         张无忌 上班赚了10000元
#         # 赵敏 上班赚了5000元
# 以上情景，属于数据不同，所以定义一个类 ,让对象去区分

class Person1:
    def __init__(self, name ):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def teach(self,person_other,skill):
        print(self.name+ "教"+person_other.name+skill)
        #类内部  可以使用私有变量  ， 也可以使用属性
        #类外部  只能使用变量

    def work(self,money):
        print("%s上班赚了%d钱"%(self.name,money))
    # def work(self, money):


p3 = Person1("张无忌")

p2 = Person1("赵敏")
p3.teach(p2,"打篮球")
p2.teach(p3,"画眉")
p3.work(10000)
