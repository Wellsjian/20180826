# 4. 在控制台中获取年份,月份.
#    显示该月份的天数.2月闰年29天,平年28天
# 1 3 5 7 8 10 12    -->  31
# 4 6  9  11  --> 30
# 2  --> 28   29

month = int(input("请输入月份:"))
year = int(input("请输入年份:"))
if month < 1 or month > 12:
  print("输入错误")
elif month == 2:
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("29天")
  else:
    print("28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
  print("30天")
else:
  print("31天")
