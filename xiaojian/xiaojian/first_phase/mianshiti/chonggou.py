"""
重构： 不改变原有的功能，修改代码
"""

dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def buying():
    """
    购物
    :return:
    """

    print_commodity()
    dict_order = create_order()
    list_order.append(dict_order)
    print("添加到购物车。")


def create_order():
    """
    创建订单
    :return:
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    return {"cid": cid, "count": count}


def print_commodity():
    """
    打印商品信息
    :return:
    """
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def settlement():
    """
    结算
    :return:
    """
    total_money = 0
    total_money = get_tatal_money(total_money)
    pay_total_money(total_money)


def print_order():
    """
    打印订单
    :return:
    """
    for item in list_order:
        commmodity = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commmodity["name"], commmodity["price"], item["count"]))


def get_tatal_money(total_money):
    """
    获取总价
    :param total_money:
    :return:
    """
    for item in list_order:
        commmodity = dict_commodity_info[item["cid"]]
        total_money += commmodity["price"] * item["count"]
    return total_money


def pay_total_money(total_money):
    """
    计算总价
    :param total_money:
    :return:
    """
    while True:
        qian = float(input("总价%d元，请输入金额：" % total_money))
        if qian >= total_money:
            print("购买成功，找回：%d元。" % (qian - total_money))
            list_order.clear()
            break
        else:
            print("金额不足.")


def select_menu():
    """
        选择菜单
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


select_menu()
