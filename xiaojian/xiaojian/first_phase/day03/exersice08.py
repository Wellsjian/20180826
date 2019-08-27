'''
一张纸的厚度是0.01毫米
请计算对折多少次超过珠穆朗玛峰8844.43米
'''
# meter = 0.00001
# count = 0
# while meter < 8844.43:
#     meter *= 2
#     count += 1
# print(count)


'''
猜数字游戏
游戏进行一个1--100之间的随机数、
让玩家重复猜测，直到猜对为止
'''

import random
import string
number = random.randint(1, 100)
count = 0
while count < 3:
    num = (input("请您进行猜数字游戏输入猜的数："))
    if num.strip().isdigit():
        count += 1
        num = int(num)
        if num > number:
            print("猜大了")
        elif num < number:
            print("猜小了")
        elif num == number:
            print("猜对了,总共猜了%d次" % count)
            break
else :   # else执行的条件是while循环条件不满足时
    print("游戏失败")


# while True:
#     循环体
#     if 退出条件：
#         break



