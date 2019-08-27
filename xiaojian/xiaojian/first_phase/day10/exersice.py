"""
1.三合一
2.当天练习独立完成
3.2048核心算法（扩展）

        -----内存图
                -----左移动
                -----右移动
            做出 ：上移动
                  下移动
4.画出code.01内的内存图
5.创建狗类，具有姓名，体重的等数据
           具有坐，吃，导盲等方法
           创建至少两个对象
6.以万物皆对象的思想，洞察身边存在的客观事物
      --- 自行创建两个对象，两个类
      核心：体会将现实事物抽象化的过程
            从抽象到具体化的过程
"""

# 5.创建狗类，具有姓名，体重的等数据
#            具有坐，吃，导盲等方法
#            创建至少两个对象
class Dog():
    def __init__(self,name,weight,color):
        """

        :rtype: object
        """
        self.name = name
        self.weight = weight
        self.color = color
    def eat(self):
        print("体重为%d的，名字为%s的，颜色是%s的小狗爱吃鸡蛋。"%(self.weight,self.name,self.color))

    def sit(self):
        print(self.name+"的小狗真懒，就会坐的.")

    def seing_eye_dog(self):
        print(self.color+"小狗会导盲.")

dog1 = Dog("小黑",10,"白色")
dog2 = Dog("旺财",8,"花色")

dog1.eat()
dog1.sit()
dog1.seing_eye_dog()

dog2.seing_eye_dog()
dog2.eat()
#
# 6.以万物皆对象的思想，洞察身边存在的客观事物
#       --- 自行创建两个对象，两个类
#       核心：体会将现实事物抽象化的过程
#             从抽象到具体化的过程

class Dog:
    def __init__(self, name, weight=50):
        self.name = name
        self.weight = weight

    def sit_down(self):
        print(self.name + "坐下了")

d01 = Dog("米咻", 60)
d02 = Dog("嘿米")
# 多个对象调用同一个方法,通过方法self参数访问对象数据.
d01.sit_down()
d02.sit_down()
d03 = d02
d03.weight = 80
print(d02.weight)  # ?
































