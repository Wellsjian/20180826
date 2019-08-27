"""
练习：定义对象计数器
    统计一个类创建了多少对象
"""


class Count_object:
    count1 = 0

    @classmethod
    def count(cls):
        print("总共创建了%d次对象" % cls.count1)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Count_object.count1 += 1
    def esercise(self):
        print("我是对象中的方法.")


#通过对象来访问实例变量和实例方法，类不能访问实例成员  类可以访问实例方法
#访问实例方法  对象名  + 方法名
c1 = Count_object("王", 25)
c1.esercise()
#访问实例变量   对象名 + 实例变量名
c2 = Count_object("李", 24)
print(c2.name)
c3 = Count_object("和", 26)
#通过类来访问实例方法
name = "园园"
Count_object.esercise(name)





#通过类来访问类方法和类变量   对象可以访问类方法和类变量
#访问类方法，类名 + 类方法名
Count_object.count()
#访问类变量 ， 类名 + 类变量名
print(Count_object.count1)
#通过对象来访问类方法a
c4 = Count_object("园园",27)
c4.count()
#通过对象来访问类变量
c5 = Count_object("乐乐",25)
print(c5.count1)
