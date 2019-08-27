# 练习：在控制台中录入月，日，计算这是这一年的第几天.
#     例如:3月６日  1月天数＋２月天数+6
#     例如:5月８日  累加前４个月天数＋８

# 方法１：
# # 1. 将每月天数存入元组
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月："))
day = int(input("请输入天："))
# 2. 存储当月的天数
result = day
# 3. 累加之前的天数
for i in range(month - 1):# 0 1 2  3
  result += day_of_month[i]
print(result)

# 方法２：
# 1. 将每月天数存入元组
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月："))
day = int(input("请输入天："))
# 2. 存储当月的天数
result = day
# 3. 累加之前的天数
result += sum(day_of_month[:month-1])
print(result)