# 主程序
# list01 = [3, 4, 45, 5, 7, 9]
# # 外层循环:拿数据
# for r in range(len(list01) - 1):  # 0          1
#   # 内层循环:做比较
#   for c in range(r + 1, len(list01)):  # 1->5  2->5
#     # 发现更小的再交换
#     if list01[r] > list01[c]:
#       list01[r], list01[c] = list01[c], list01[r]
#
# print(list01)

"""
# 练习定义函数，对列表进行排序"""


# #   传入的是可变类型对象
# #   函数体内部，可以修改对象
# #   无需通过返回值，返回结果.


# def print_list(str1):
#     str1 = list(str1)

def sort(print_list):
    """

    :param print_list: 用来获取所需排序的列表
    :return:
    """

    for r in range(len(print_list) - 1):
        for c in range(r + 1, len(print_list)):
            if print_list[r] > print_list[c]:
                print_list[r], print_list[c] = print_list[c], print_list[r]

#
# list = [3, 4, 45, 5, 7, 9]
# sort(list)
# print(list)
sort([1,5,6,8,1,2])
