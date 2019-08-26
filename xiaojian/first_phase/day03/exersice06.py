# 在控制台录入一个年份，如果是闰年 给month变量赋值29，否则28
#
# 在控制台获取一个整数，如果为奇数，则给state赋值为奇数反之偶数

#
# number = int(input("请输入一个整数："))
#
# state = "奇数" if number % 2  else "偶数"
#
# print(state)

year = int(input("请输入一个年份："))

month2 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
month2 = 29 if not year % 4 and year % 100 or not year % 400 else 28

print(month2)
