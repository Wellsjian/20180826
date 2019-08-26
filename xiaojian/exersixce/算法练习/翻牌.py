# 1 -100 有 100张牌 ,背面朝上
# 一人从第二张牌开始 每隔一张牌翻一次
# 另一人从第三张牌开始,每隔两张翻一次
# .........
# 求最后正面朝上的牌

def get_side():
    dict = {}
    flag = False
    for i in range(1, 5):
        dict[i] = flag
    start = 2
    while start <= 101//2 :

        for j in range(start, 101, start):
             dict[j] = not dict[j]
        start += 1

    for i in dict:
        if dict[i] == True:
            print(i)

get_side()