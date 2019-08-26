# 3. 在控制台中获取月份,显示季度,或者提示月份错误.
month = int(input("请输入月份:"))
# if 1 <= month <= 3:
#   print("春")
# elif 4 <= month <= 6:
#   print("夏")
# elif 7 <= month <= 9:
#   print("秋")
# elif 10 <= month <= 12:
#   print("冬")
# else:
#   print("月份输入错误")

if month < 1 or month > 12:
  print("月份输入错误")
elif month >= 10:
  print("冬")
elif month >= 7:
  print("秋")
elif month >= 4:
  print("夏")
else:
  print("春")
