"""
练习 ：定义子类 ： 狗
                鸟
      定义父类 ： 动物

      创建不同类型的对象
      体会 isinstance
          issubclass
"""


class Animal:
    """
    动物
    """
    def yell(self):
        print("动物会叫")


class Dog(Animal):
    """
    狗
    """
    def watch(self):
        print("狗会看东西")


class Bird(Animal):
    """
    鸟
    """
    def fly(self):
        print("鸟会飞")


a1 = Animal()
d1 = Dog()
d1.yell()
b1 = Bird()

print(isinstance(a1, Dog))
print(isinstance(a1, Animal))

print(issubclass(Dog, Animal) and Dog == Animal)
print(issubclass(Dog, Dog))
