# 练习1:在控制台中录入商品单价  15
#       再录入商品数量  2
#       最后获取金额,计算应该找回多少钱. 45 - 15 * 2
# 14:37

price = input("请输入商品单价:")
price = float(price)
amount = int(input("请输入数量:"))
money = float(input("请输入金额:"))
result = money - price * amount
print("应找回:"+str(result))









