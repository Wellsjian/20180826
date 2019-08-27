# 练习4
# 4. 在控制台中获取年份,月份.
#    显示该月份的天数.2月闰年29天,平年28天.

# year = input("请输入年份：")
# month = input("请输入月份：")
# tuple1 = (1, 3, 5, 7, 8, 10, 12)
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
#     elif month in tuple1:
#         print("该月份有31天")
#     else:
#         print("该月份有30天")
# else:
#     print("您的输入不合法.")


# 1.方法一
month = int(input("请输入月份："))

if month < 1 or month > 12:
    print("输入错误.")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("本月有31天.")
else:
    print("本月有30天.")
  
#2.方法二

month = int(input("请输入月份："))

day_of_month = (31,28,31,40,31,30,31,31,30,31,30,31)

print(day_of_month[month-1])



















