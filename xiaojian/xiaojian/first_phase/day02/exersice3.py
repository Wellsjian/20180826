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

# 练习2:
# 在控制台中获取小时，分钟，秒，计算总秒数
#
# hour = int(input("请输入小时："))
# minute = int(input("请输入分钟:"))
# second = int(input("请输入秒:"))
#
# all_second = hour * 3600 + minute * 60 + second
# print("总秒数为%d" % all_second)


'''练习３：
   匀变速直线运动的位移与时间公式：
   距离＝初速度＊时间＋０．５＊加速度＊时间的平方
   已知：　距离　　时间　　初速度
   计算加速度
'''
# distance = float(input("请输入距离:"))
# time = int(input("请输入时间:"))
# inital_velocity = float(input("请输入初速度:"))
#
# accelerated = 2*(distance - inital_velocity * time )/(time**2)
#
# print("加速度为"+str(accelerated))


"""
练习４：
    古代的一斤为１６两
    在控制台中获取两，计算是几斤几两
"""

# liang = float(input("请输入两："))
# jin = liang // 16
# liang_1 = liang % 16
# print("最终为%d斤%d两" % (jin, liang_1))


"""
在控制台中录入一个四位整数
计算每位相加之和
"""
# 方法1 普通分离参数法
# number = int(input("请输入一个四位整数："))
#
# qian = number // 1000
# bai = number // 100 % 10
# shi = number // 10 % 10
# ge = number % 10
#
# sum = qian + bai + shi + ge
#
# print("和为" + str(sum))

# 方法2 累加的方法
# number = int(input("请输入一个四位整数："))
#
# result = number % 10
# result += (number // 10 % 10)
# result += (number // 100 % 10)
# result += (number //1000)
#
#
# print("和为" + str(result))

# 方法3 for循环法
# number = input("请输入一个四位整数：")
# sum = 0
# for i in number:
#     i = int(i)
#     sum += i
# print(sum)
