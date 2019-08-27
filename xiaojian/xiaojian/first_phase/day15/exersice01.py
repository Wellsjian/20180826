"""
练习
    定义员工管理器
    --记录所有员工
    --计算员工总薪资

    1.普通员工
    2.程序员 ： 底薪   +   项目分红
    3.销售 ： 底薪 + 提成（销售额 * 0.05）
    4......
    要求 ：增加新岗位 ，员工管理器不变
"""


class EngineerManager:
    """
    员工管理器
    """

    def __init__(self):
        self.all_engineer = []

    def add_engineer(self, engineer):
        """
        增加员工
        :param engineer:
        :return:
        """
        self.all_engineer.append(engineer)

    def calculate_total_money(self):
        """
        计算薪资
        :return:
        """
        total_money = 0
        for item in self.all_engineer:
            total_money += item.get_engineer_money()
        return total_money


class Worker:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def get_engineer_money(self):
        """
        获得工资
        :return:
        """
        return self.basic_salary


class Programmer(Worker):
    """
    程序员
    """

    def __init__(self, basic_salary, particiption_in_profit):
        super().__init__(basic_salary)
        self.particiption_in_profit = particiption_in_profit

    def get_engineer_money(self):
        """
        获得工资
        :return:
        """
        # return self.basic_salary + self.particiption_in_profit
        #里斯替换
        return super().get_engineer_money() + self.particiption_in_profit


class Market(Worker):
    """
    销售员
    """

    def __init__(self, basic_salary, sale):

        super().__init__(basic_salary)
        self.sale = sale

    def get_engineer_money(self):
        """
        获得工资
        :return:
        """
        return self.basic_salary + self.sale * 0.05


manager = EngineerManager()

manager.add_engineer(Programmer(10000, 100000))
manager.add_engineer(Worker(5000))
manager.add_engineer(Market(1800, 100000))

print(manager.calculate_total_money())
