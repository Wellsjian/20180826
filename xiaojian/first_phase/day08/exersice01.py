# 体会：
# 1.参数    是调用者给定义者的信息
# 2.返回值  是定义者给调用者的信息
# 3.函数    一个功能（职责单一，分而治之）



def get_all_second(hour = 0, minute = 0, second = 0):
    """
    获取总秒数
    :param hour: 输入的小时数
    :param minute: 输入的分钟数
    :param second: 输入的秒数
    :return:
    """
    return hour * 3600 + minute * 60 + second


print(get_all_second(hour =1, second = 1))
