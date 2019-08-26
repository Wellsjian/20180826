# 4. 在控制台中获取年份,月份.
# #    显示该月份的天数.2月闰年29天,平年28天.

# year = input("请输入年份：")
# month = input("请输入月份：")
# list = [1,3,5,7,8,10,12]
# if year.strip().isdigit() and month.strip().isdigit():
#     year = int(year)
#     month = int(month)
#
#     if month < 1 or month > 12:
#         print("您的输入不合法.")
#     elif month == 2:
#         day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
#         print("该月份有%s天" % day)
#
#
#     elif month in list:
#             print("该月份有31天")
#     else:
#         print("该月份有30天")
# else:
#     print("您的输入不合法.")

def is_leap_year(year):
    """

    :param year: 需要判断的年份
    :return:
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_count(year, month):
    """
    获取天数
    :param year: 获取年份
    :param month: 获取月份
    :return:
    """

    if month < 1 or month > 12:
        return "您的输入不合法."
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    return 30

print(get_day_count(2000, 15))
print(get_day_count(2010, 3))
print(get_day_count(2019, 6))
