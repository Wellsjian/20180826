'''
1.三合一
2.当天练习独立完成
3.自学（参照菜鸟教程）字符串/列表/字典常用函数
4.删除列表中所有偶数（群讨论）
     [3,2,4,6,8,8,5,3]
5.玩2048游戏
6.重构 shopping.py 程序
7.阅读python入门到实践第八章
'''

# 4.删除列表中所有偶数（群讨论）
#      [3,2,4,6,8,8,5,3]


# list01 = [3, 2, 4, 6, 8, 9, 5, 3]

# i = 0
# while i < len(list01):
#     if list01[i] % 2 == 0:
#         list01.remove(list01[i])
#         continue
#     i += 1
# print(list01)
#
#根据索引倒叙删除
# list01 = [3, 2, 4, 6, 8, 8, 5, 3]
#
# for i in range(len(list01)-1,-1,-1):
#     if list01[i] % 2 == 0 :
#         list01.remove(list01[i])
# print(list01)

list01 = [3, 2, 4, 6, 8, 9, 5, 3]
for i in list01:
    if i % 2 == 0:
        list01.remove(i)
        print(list01)
    else:
        list01.append(i)
        print(list01)











