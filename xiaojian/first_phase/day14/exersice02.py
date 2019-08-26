"""
练习  定义父类： 汽车（数据：品牌。型号，价格）
    定义子类 ：  电动汽车（数据：电池，充电功率）
    创建电动汽车对象   画出内存图
"""


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class ElectricCar(Car):
    def __init__(self, battery_capacity, charging_power, brand, model, price):
        super().__init__(brand, model, price)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


e1 = ElectricCar(60, 50, "H7", "小鸟", 100000)
print(e1.battery_capacity)
