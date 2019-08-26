"""
封装01:使用方法来封装数据
"""


class Wife():
    """
    老婆
    """

    def __init__(self, name, age):
        self.name = name
        # 1.隐藏变量
        # 内部做法：  改变变量名称  下划线+类名 +变量名  wife01._Wife__age
        # self.__age = age
        #通过方法来操作数据，而不是直接来设置数据
        self.set_age(age)

        # 2.提供写入/读取变量的功能

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 28 <= value <= 32:
            self.__age = value
        else:
            raise Exception("我不要")


wife01 =Wife("丽丽", 28)
print(wife01.get_age())
wife01.set_age(29)

wife02 = Wife("莹莹", 30)
# 不符合业务逻辑
w01 = Wife("丽丽", 30)
# 创建了新成员变量,没有访问成员变量__age
# w01.__age = 87
# 无法读取私有变量
# print(w01.__age)
# 小人做法
# print(w01._Wife__age)

# 通过方法,操作变量
w01.set_age(30)
print(w01.get_age())
print(w01.__dict__)