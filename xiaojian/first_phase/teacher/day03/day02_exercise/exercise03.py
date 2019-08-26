"""
5. 扩展在控制台中录入总秒数,
   计算几小时零几分钟零几秒
   10:55 上课
"""
total_second = 123456
second = total_second % 60
# total_second // 60  取整数商,表示总的分钟数.
#total_second // 60 除 60,商是小时,余数表示剩余的分钟.
minute = total_second // 60 % 60
hour = total_second // 60 // 60
print(hour)
print(minute)
print(second)


