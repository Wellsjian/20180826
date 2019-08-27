# 练习:在控制台中获取小时

"""
def get_total_second(hour,minute,second):
  result = hour * 3600 + minute * 60 + second
  return result

hour = int(input("请输入小时:"))
minute = int(input("请输入分钟:"))
second = int(input("请输入秒:"))

result = get_total_second(hour,minute,second)

print("结果是:" + str(result) + "秒")
"""

#10:55
# 体会：参数　是调用者传递给定义者的信息
#      返回值　是定义者告诉调用者的信息
#      函数  一个功能(职责单一)
def get_total_second(hour, minute, second):
  return hour * 3600 + minute * 60 + second

# re = get_total_second(1,2,3)
# print(re)

print(get_total_second(1, 2, 3))
