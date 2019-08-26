"""
类成员
"""


class ICBC:
    """
    工商银行
    """

    # 表示类方法，表示类的行为，只能操作类变量，不能操作实例变量
    @classmethod
    def get_total_money(cls):
        print("总行的钱为%d" % cls.total_money)

    # 类被加载时，类变量创建
    # 通过类变量，表示总行的钱
    total_money = 5000000

    def __init__(self, name, money):
        self.name = name
        # 通过实例变量来表示支行使用的钱
        self.money = money
        ICBC.total_money -= money


# 创建对象
i01 = ICBC("天坛东门支行", 100000)
# 访问类变量
print(ICBC.total_money)
i00 = ICBC("天安门支行", 200000)
# 访问类方法
ICBC.get_total_money()
