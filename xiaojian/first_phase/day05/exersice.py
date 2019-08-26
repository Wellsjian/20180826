'''
1.三合一
2.当前练习独立完成
3.计算列表中的最小值，不使用min函数
4.双色球:
        蓝色1-17之间的整数  红色1-33之间的整数
        蓝色有1个           红色有7个不重复的数字
        1.随机产生一注彩票[一个蓝球，7个红球]，打出彩票
        2.在控制台中购一注彩票：
        "请输入第一个红球号码："
        "请输入第二个红球号码"
        "号码不在范围内"
        "号码已经重复"
5.阅读python入门到实践第3章第4章

'''

# 3.计算列表中的最小值，不使用min函数
# list1 = []
# while True:
#     number = input("请输入一个整数：")
#     if number == "esc":
#         break
#     list1.append(int(number))
# print(list1)
#
# min = list1[0]
#
# for i in range(1,len(list1)):
#     if min > list1[i]:
#         min = list1[i]
# print(min)


# 4.双色球:
#         蓝色1-17之间的整数  红色1-33之间的整数
#         蓝色有1个           红色有7个不重复的数字
#         1.随机产生一注彩票[一个蓝球，7个红球]，打出彩票
#         2.在控制台中购一注彩票：
#         "请输入第一个红球号码："
#         "请输入第二个红球号码"
#         "号码不在范围内"
#         "号码已经重复"
import random

# list2 = []
#
# while len(list2) < 7:
#     number = random.randint(1,33)
#     if number in list2:
#         continue
#     list2.append(number)
# list2.append(random.randint(1,17))
# print(list2)

#

list3 = []

while len(list3) < 7:
    number = int(input("请输入第%d个红球号码：" % (len(list3) + 1)))
    if number < 1 or number > 33:
        print("号码不在范围内,重新输入!!!")
        continue
    if number in list3:
        print("号码已经重复,再次输入!!!")
        continue

    list3.append(number)
print(list3)

while len(list3) < 8:
    number1 = int(input("请输入篮球号码："))
    if number1 < 1 or number1 > 18:
        print("号码不在范围内,重新输入!!!")
        continue
    list3.append(number1)

print(list3)

# if list3 == list2:
#     print("您中奖了")
