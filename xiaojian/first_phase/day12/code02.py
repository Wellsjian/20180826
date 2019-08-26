"""
封装2：使用属性property来封装
"""
class Wife():
    """
    老婆
    """

    def __init__(self, name, age):
        self.name = name
        #通过方法操作数据
        #本质是通过操作类变量
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 28 <= value <= 32:
            self.__age = value
        else:
            raise Exception("我不要")
    #拦截  对数据的操作，转为调用读写方法
    age = property(get_age,set_age)
    #property对象内部通过python描述符协议来实现


w01 =Wife("丽丽", 28)
w01.set_age(30)
print(w01.get_age())
print(w01.__dict__)