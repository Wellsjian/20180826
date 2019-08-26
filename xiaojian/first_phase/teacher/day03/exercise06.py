# 练习1:在控制台中获取一个整数:
# 如果是奇数给变量state赋值"奇数",否则赋值"偶数"
number = int(input("请输入整数:"))
# if number % 2 == 1:
#   state = "奇数"
# else:
#   state = "偶数"

# 真值表达式
# if number % 2: # if bool(number % 2) --> if bool(1)
#   state = "奇数"
# else:
#   state = "偶数"

# 条件表达式
state = "奇数" if number % 2 else "偶数"
print(state)


# 练习2:在控制台中获取一个年份
# 如果是闰年,给变量month02变量赋值:29.否则赋值28

year = int(input("请输入年份:"))
# result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# if result:
#   month02 = 29
# else:
#   month02 = 28

# result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# # 条件表达式
# month02 = 29 if result else 28

# 真值表达式(因为代码可读性查,所以特别不建议使用)
# result = not year % 4 and year % 100 or not year % 400
# month02 = 29 if result else 28
# print(month02)

# 建议
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
mont02 = 29 if result else 28













