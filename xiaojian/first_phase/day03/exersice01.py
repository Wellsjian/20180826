# 练习１：
#     在控制台录入商品单价
#     在录入商品数量　２
#     最后获取金额，计算应找回多少钱


unit_price = float(input("请输入商品单价："))



amount = float(input("请输入购买数量："))
money = float(input("请输入顾客的金钱："))
cost = unit_price * amount
loose_change = money - cost
if money > cost:

    print('总合计花费%d元，最终找零%d元' % (cost, loose_change))
else:
    print("您的钱不够")