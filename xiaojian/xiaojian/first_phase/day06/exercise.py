'''
1.三合一
2.每天练习独立完成
3.将1970年到2050年中的闰年存入列表
4.描述多个商品信息，在控制台中显示出来
比如说  屠龙刀，10000元
        倚天剑，10000元
        打狗棒， 5000元
5. 描述全国各个城市的景区与美食
    北京：
        景区：故宫 天安门  天坛
         美食：烤鸭  炸酱面  豆汁  卤煮
    四川：
        景点：九寨沟  峨眉上 春熙路
        美食: 火锅 串串香 兔头
6.在控制台中计算一个字符串中的字符以及出现的次数
7.扩展 猜拳游戏 石头剪刀布
           系统随机选择一个
           用户选择一个
           判断输赢
         提示：将胜利策略存入容器
             石头 战胜 剪刀
             剪刀 战胜 布
             布   战胜 石头
8.阅读python入门到实践  第四章和第六章

'''
# 3.将1970年到2050年中的闰年存入列表

# list = []
# for i in range(1970, 2051):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         list.append(i)
# print(tuple(list))
#
# list = [ i  for i in range(1970, 2051)
#         if i % 4 == 0 and i % 100 != 0 or i % 400 == 0
# ]
# print(list)


# 4.描述多个商品信息，在控制台中显示出来
# 比如说  屠龙刀，10000元
#         倚天剑，10000元
#         打狗棒， 5000元
#            ......
#
# dict01 = {"屠龙刀": 10000, "倚天剑": 10000, "打狗棒": 5000}
#
# for key, value in dict01.items():
#     print(key, str(value) + "元宝")

# 5. 描述全国各个城市的景区与美食
#     北京：
#         景区：故宫 天安门  天坛
#          美食：烤鸭  炸酱面  豆汁  卤煮
#     四川：
#         景点：九寨沟  峨眉上 春熙路
#         美食: 火锅 串串香 兔头

# dict02 = {"北京": {"景区": ["故宫", "天安门", "天坛"],
#                  "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]
#                  },
#           "四川": {"景区": ["九寨沟", "峨眉山", "春熙路"],
#                  "美食": ["火锅", "串串香", "兔头"]
#                  }
#           }
#
# for key1, value1 in dict02.items():
#     print(key1)
#
#     for key2, value2 in value1.items():
#         print(key2, end=" ")
#         for i in value2:
#             print(i, end=" ")
#         print()

# 6.在控制台中计算一个字符串中的字符以及出现的次数

# str1 = input("请输入一个字符串：")
#
# list = []
#
# for i in str1:
#     str1.count(i)
#     if i in list:
#         continue
#     list.append(i)
# for i in list:
#     print(i, str1.count(i))
#
# str1 = input("请输入一个字符串：")
# set1 = set(str1)
# for i in set1:
#     print(i, str1.count(i))


# 字典：
#
# str1 = input("请输入一个字符串：")
# dict01 = {}
#
# for i in str1:
#     if i in dict01:
#         dict01[i] = 1
#     else:
#         dict01[i] += 1
# print(dict01)




# 8.扩展 猜拳游戏 石头剪刀布
#            系统随机选择一个
#            用户选择一个
#            判断输赢
#          提示：将胜利策略存入容器
#              石头 战胜 剪刀
#              剪刀 战胜 布
#              布   战胜 石头

import random

menu = '''请选择
(1)石头
(2)剪刀
(3)布
(4)退出'''
dict1 = {"石头": "剪刀", "剪刀": "布", "布": "石头"}
dict2 = {}
while True:
    str1 = random.choice(["石头", "剪刀", "布"])
    str2 = input("请输入您的出拳：")
    dict2[str2] = str1
    # print(dict2)
    if dict1[str1] == str1:
        print("恭喜您，您赢了.")
        break
    elif str1 == str2:
        print("平局.")
    else:
        print("很遗憾，您输了.")
