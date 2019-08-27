# 5.计算2 ---100之间的素数
#    素数：只能被1和自身整数的数字
#    算法：
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:  # 如果上面执行完毕以后都没有出现，则执行else
#         list01.append(i
# print(list01)

def is_prime(number):
    if number <= 1:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    return True


def get_prime(begin, end):
    """

    :param begin: 获取范围的起始值,包括起始值
    :param end: 获取范围的结束值，不包含结束值
    :return:
    """
    list01 = []
    for i in range(begin, end):
        if is_prime(i):
            list01.append(i)
    return list01


print(get_prime(5, 59))
