'''
1.在控制台中按照如下格式输出：圆形的面积为52.5，周长是35.25
其中图形是变量，面积和周长的值为变量
2.在控制台中显示120秒的倒计时，02:00-->01:59-->1:58.
'''
import time
#
# area = 52.5
# permetre = 35.25
# graph = "圆形"
#
# print("%s的图形面积为%.1f，周长为%.2f" %(graph,area,permetre))


# for i in range(120,-1,-1):
#     minute = i // 60
#     second = i % 60
#     time.sleep(2)
#     print("%02d:%02d" %(minute,second))


for i in range(0,121,1):
    minute = i // 60
    second = i % 60
    time.sleep(2)
    l = "%02d:%02d" % ( minute, second)
    print(l)