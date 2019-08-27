# 练习：定义函数，根据月份计算天数．# 参照：day03作业
# month = int(input("请输入月份:"))
# year = int(input("请输入年份:"))
# if month < 1 or month > 12:
#   print("输入错误")
# elif month == 2:
#   if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("29天")
#   else:
#     print("28天")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#   print("30天")
# else:
#   print("31天")

"""
def get_days_for_month(year, month):
  if month < 1 or month > 12:
    return "输入错误"
  if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
      return "29天"
    return "28天"
  if month in (4, 6, 9, 11):
    return "30天"
  return "31天"


print(get_days_for_month(2000, 2))
"""


def is_leap_year(year):
  """
    判断是否是闰年
  :param year: 需要判断的年份
  :return: 是闰年返回ｔｒｕｅ 是平年返回ｆａｌｓｅ
  """
  # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  #   return True
  # else:
  #   return False
  return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_days_for_month(year, month):
  if month < 1 or month > 12:
    return "输入错误"
  if month == 2:
    # if is_leap_year(year):
    #   return 29
    # return 28
    return 29 if is_leap_year(year) else 28
  if month in (4, 6, 9, 11):
    return 30
  return 31


print(get_days_for_month(2000, 2))
