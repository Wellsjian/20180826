"""
***封装设计思想
"""
# 设计原则：
# 1.开闭原则
#     扩展（增加新功能）开放
#     修改（不改变代码）关闭
#
# 2.依赖倒置  ：  使用抽象（父类，稳定的），而不是使用子类（多变化）

# 需求 ：老张开车去东北

#

class People:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to(self, type, str_pos):
        type.run(str_pos)


class Car:
    def run(self, str_pos):
        print("行驶到", str_pos)


lz = People("老张")
car = Car()
lz.to(car, "东北")


# 练习：小明在招商银行取钱

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Bank:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def get_money(self, person, value):
        person.money += value
        self.money -= value


xm = Person("小明", 0)
yh = Bank("招商", 100000)

yh.get_money(xm, 5000)
print(xm.money)
