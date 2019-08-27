"""
1.三合一   架构图  代码   理论
2.独立完成当日练习
3.开放型作业：洞察客观世界的事物，自行定义子类与父类，子类至少两个，父类至少一个
4.有若干个图形（圆形/矩形...）
    定义图形管理类，1.记录所有图形（多个图形对象，多个矩形对象）
                  2.提供计算总面积的而方法
                  用面向对象方法分析
5.穷尽一切手段在互联网上收集继承与多态的资料，结合课堂所讲，为答辩准备，开闭原则，依赖倒置`
写成自诉文档
关键词 ：  封装  继承  多态   面向对象    三大特征
"""

class Electronics:
    def __init__(self, name, model, brand):
        self.name = name
        self.model = model
        self.brand = brand

    def get_info(self):
        print("我可以获得信息。")


class Computer(Electronics):
    def __init__(self, name, model, brand, laptop, desktop):
        super().__init__(name, model, brand)
        self.laptop = laptop
        self.desktop = desktop
    def call(self):
        print("我可以打电话")
        

class MobilePhone(Electronics):
    def __init__(self, name, model, brand, smart_phone, featre_phone):
        super().__init__(name, model, brand)
        self.smart_phone = smart_phone
        self.feature_phone = featre_phone
    def play_games(self):
        print("我可以打游戏")


class Number:
    def __init__(self):
        self.number = []

    def get_number(self,shape):

        area = shape.get_area()
        print(area)
        self.number.append(area)
    def get_total_area(self):
        total_area = 0
        for item in self.number:
            total_area += item
        return total_area

class ShapeManager:
    # def __init__(self ):
        # self.count = count
    def get_area(self):
        pass



class Circle(ShapeManager):

    def __init__(self, radius,count =0 ):
        # super().__init__(count)
        self.radius = radius
        self.count =count
    def get_area(self):
        area =  3.14 * self.radius * self.radius
        # print(area)
        return area

class Rectangle(ShapeManager):
    def __init__(self, length, wideth):
        # super().__init__(count)
        self.length = length
        self.wideth = wideth


    def get_area(self):
        area = self.wideth * self.length
        # print(area)
        return area

n1 = Number()
c1 = Circle(5)
n1.get_number(c1)
r1 = Rectangle(2, 3)
n1.get_number(r1)
r1 = Rectangle(3, 6)
n1.get_number(r1)
total_area = n1.get_total_area()
print(total_area)




    

























