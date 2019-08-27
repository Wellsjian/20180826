"""
定义汽车类，数据（），行为（）
"""

class Car():
    """
    汽车
    """
    #   创建数据成员
    def __init__(self,str_str_brand,type,price=100000):
        #self是调用当前方法对象的地址
        self.str_str_brand = str_str_brand
        self.type = type
        self.price = price

    def start(self):
        """
        启动
        :return: 
        """
        print(self.str_str_brand+self.type +"启动了.")
    def stop(self):
        """
        停止
        :return: 
        """
        print(self.str_str_brand+self.type +"停止了.")


car1 = Car("宝马","x6")
car1.start()
car2= Car("奔驰","x600").stop()
# print(car2)






