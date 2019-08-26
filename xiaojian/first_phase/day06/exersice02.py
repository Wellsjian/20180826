'''
在控制台中录入几月几日，计算是这一年第几天
'''
month = int(input("请输入月份："))
day = int(input("请输入日子："))

day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day_all = day

# 方法一
# for i in range(month - 1):
#     day_all += day_of_month[i]
#
# print("这是一年第%d天" % day_all )
#
# 方法二

day_all += sum(day_of_month[:month-1])
print("这是一年第%d天" % day_all )




