"""
封装数据3：使用标准属性来封装数据
"""



class Wife():
    """
    老婆
    """

    def __init__(self, name, age):
        self.name = name
        # 通过方法操作数据
        # 本质是通过操作类变量
        self.age = age
    @property#拦截读取造作,本质是创建property对象，注册读取方法
    def age(self):
        return self.__age

    @age.setter#拦截写入操作，本质是将写入方法注册到property对象中
    def age(self, value):
        if 28 <= value <= 32:
            self.__age = value
        else:
            raise Exception("我不要")



w01 =Wife("丽丽", 28)

print(w01.age)
print(w01.__dict__)