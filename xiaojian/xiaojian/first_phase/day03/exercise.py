# day03作业:
# 1. 三合一.
# 2. 当天练习独立完成.
# 3. 在控制台中获取月份,显示季度,或者提示月份错误.
# 4. 在控制台中获取年份,月份.
#    显示该月份的天数.2月闰年29天,平年28天.
# 5. 累加1--100之间的整数和.
# 6. (扩展)根据身高体重,参照BMI,返回身体状况.
#     BMI:用体重千克数除以身高米数的平方得出的数字
#     中国参考标准
#     体重过低BMI<18.5
#     正常范围18.5≤BMI<24
#     超重24≤BMI<28
#     I度肥胖28≤BMI<30
#     II度肥胖30≤BMI<40
#     Ⅲ度肥胖BMI≥40.0
# 7. 阅读:程序员的数学第4章.


# 练习3
# 3. 在控制台中获取月份,显示季度,或者提示月份错误.
# month = input("请输入月份：")
# if month.strip().isdigit():
#     month = int(month)
#     if month < 1 or month > 12:
#         print("输入不合法！！！")
#     elif  month <=3 :
#         print("貌似在春天.")
#
#     elif  month <=6 :
#         print("仿佛在夏天.")
#
#     elif  month <=9 :
#         print("应该在秋天.")
#
#     else   :
#         print("大约在冬天.")
#
# else:
#     print("输入不正确.")


# 练习4
# 4. 在控制台中获取年份,月份.
#    显示该月份的天数.2月闰年29天,平年28天.

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


# 练习5. 累加1--100之间的整数和.

#
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)


# 6.(扩展)
# 根据身高体重, 参照BMI, 返回身体状况.
#     BMI:用体重千克数除以身高米数的平方得出的数字
#     中国参考标准
#     体重过低BMI<18.5
#     正常范围18.5≤BMI<24
#     超重24≤BMI<28
#     I度肥胖28≤BMI<30
#     II度肥胖30≤BMI<40
#     Ⅲ度肥胖BMI≥40.0

# height = float(input("请输入您的身高："))
# weight = float(input("请输入您的体重："))
#
# BMI = round(weight / (height / 100) ** 2, 1)
# print(BMI)
#
# if 0 < BMI < 18.5 :
#     print("体重过低.")
# elif BMI < 24 :
#     print("正常范围.")
# elif BMI < 28 :
#     print("超重.")
# elif BMI < 30 :
#     print("I度肥胖.")
# elif BMI < 40 :
#     print("II度肥胖.")
# elif BMI >= 40.0 :
#     print("Ⅲ度肥胖.")









