# 5. 描述全国各个城市的景区与美食
#     北京：
#         景区：故宫 天安门  天坛
#          美食：烤鸭  炸酱面  豆汁  卤煮
#     四川：
#         景点：九寨沟  峨眉上 春熙路
#         美食: 火锅 串串香 兔头

# {"北京":{"景区":["故宫","天安门","天坛"],
#         "美食":["烤鸭","炸酱面","豆汁","卤煮"]
#                 },
#  "四川":{"景区":["九寨沟","峨眉山","春熙路"],
#         "美食":["火锅","串串香","兔头"]
#                 }
#  }8.10


# 改动前：
dict01 = {}

while True:
    place = input("请输入您想要去的地方：")
    if place == "esc":
        break
    # info = input("请输入您要查找的特色类型：")
    dict02 = {}
    dict01[place] = dict02
    scenic_spot_all = []
    delicious_food_all = []
    while True:
        scenic_spot = input("请输入您想要去的景区：")
        if scenic_spot == "esc":
            flag = 1
            break
        scenic_spot_all.append(scenic_spot)
        dict02["风景"] = scenic_spot_all
    while flag == 1 :
        dlicious_food = input("请输入你想吃的美食：")
        if dlicious_food == "esc":
            break
        delicious_food_all.append(dlicious_food)
        dict02["美食"] = delicious_food_all
# print(dict01)
for key1,value1 in dict01.items():
    print(key1)
    for key2 ,value2 in value1.items():
        print(key2,end=" ")
        for i in value2:
            print(i,end= " ")
        print()


# 改动后：

# dict04 = {}
# while True:
#     place = input("请输入您将要去的旅游地点：")
#     if place == "esc":
#         break
#     dict05 = {}
#     while True:
#         info = input("请您输入您索要获取的信息：")
#         if info == "esc":
#             break
#         list1 = []
#         while True:
#             information = input("请您输入该信息的具体特征：")
#             if information == "esc":
#                 break
#             list1.append(information)
#         dict05[info] = list1
#     dict04[place] = dict05
#
# for place1 , info1 in dict04.items():
#     print(place1)
#     for key3 ,value3 in info1.items():
#         print(key3,end= " ")
#         for i in value3:
#             print(i,end = " ")
#         print()
























