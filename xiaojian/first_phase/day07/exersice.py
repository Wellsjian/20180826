"""
1.三合一
2.独立完成每日练习
3.定义在控制台中打印矩形的函数
4.定义在控制台中打印二维列表的函数
5.计算2 ---100之间的素数
   素数：只能被1和自身整数的数字
   算法：
6.阅读程序员的数学第5章
"""


# 3.定义在控制台中打印矩形的函数
#
def print_rectangle(higth, wideth, char):
    """

    :param higth:  打印矩形的长度   int类型
    :param wideth: 打印矩形的宽度int类型
    :param char:   打印矩形的填充字符
    :return
    :
    """
    for i in range(higth):
        for j in range(wideth):
            print(char, end=" ")
        print()


print_rectangle(10, 8, "-")


# 4.定义在控制台中打印二维列表的函数
# 二维列表：
# [
#     [2,4,0,8,"a"],
#     [0,2,4],
#     [4,0],
#     [0,2,2,0],
# ]
# 打印结果：
# 2   4   0  8   a
# 0   2   4
# 4   0
# 0   2   2  0

def print_double_list(count):
    """
    在控制台中打印二维列表
    :param count: 用来判断输入数据的行数
    :return:
    """
    #
    # list001 = []
    # for i in range(count):
    #     number = input("请输入第%d行元素：" % (i+1))
    #     number = list(number)
    #     list001.append(number)
    # # print(list001,end=" ")
    #
    # for item  in list001:
    #     for i in item:
    #         print(i,end="  ")
    #     print()


# ------------------------------------------------------------------------------

# list02 = [
#     [2,4,0,8,"a"],
#     [0,2,4],
#     [4,0],
#     [0,2,2,0],
# ]
#
# erwei_list(list02)


# print_rectangle(8)


# 5.计算2 ---100之间的素数
#    素数：只能被1和自身整数的数字
#    算法：
import time

# list01 = []
# flag = True
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j == 0 :
#             flag = False
#             break
#         flag = True
#     if flag:
#         list01.append(i)
# print(set(list01))


# 老师版逻辑

list01 = []
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # 如果上面执行完毕以后都没有出现，则执行else
        list01.append(i)
print(list01)

# 3     2
# 4     23
# 5     234
# 6     2345
# 7     23456
# 8     234567
