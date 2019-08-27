"""
定义父类： 动物（数据：姓名，年龄）
定义子类： 狗（数据：爱称
定义子类： 鸟（数据：
"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, diminutive):
        super().__init__(name, age)
        self.diminutiove = diminutive

dog = Dog("旺财",5,"小旺财")
print(dog.name,dog.diminutiove)
