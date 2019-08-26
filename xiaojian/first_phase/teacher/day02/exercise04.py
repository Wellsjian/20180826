# 练习:在控制台中获取小时
#     获取分钟
#     获取秒
#     计算总秒数
# 15:20 上课
hour = int(input("请输入小时:"))
minute = int(input("请输入分钟:"))
second = int(input("请输入秒:"))
result = hour * 3600 + minute * 60 + second
print("结果是:" + str(result) + "秒")

