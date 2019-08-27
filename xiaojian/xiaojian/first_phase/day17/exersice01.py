"""
练习一  定义函数  返回星期数
星期一  ... 星期二 ... 星期三
"""
import time

# 1.获取当前时间戳
time01 = time.time()
print(time01)

# 2.获取时间元组
time02 = time.localtime()
print(time02)

# 3.时间元组转换为字符串格式
time03 = time.strftime("%y/%m/%d %H:%M:%S", time02)
print(time03)

# 4.字符串格式转化为时间元组
time04 = time.strptime("2019/5/21","%Y/%m/%d")
print(time04)

# 5.时间元组转换为时间戳
time05 = time.mktime(time04)
print(time05)

def get_week(year, month, day):
    # 字符串转为时间元组
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    # dict_weeks = {
    # 0:"星期一",
    # 1:"星期二",
    # 2:"星期三",
    # 3:"星期四",
    # 4:"星期五",
    # 5:"星期六",
    # 6:"星期日"}
    list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    # return dict_weeks[tuple_time[6]]
    return list[tuple_time[6]]

print(get_week(2019,5,22))
