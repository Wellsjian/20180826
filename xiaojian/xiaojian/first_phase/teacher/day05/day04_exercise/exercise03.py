"""
5. (扩展)一个小球从１００ｍ的高度落下
    　　每次弹回原高度的一半．
    　　计算：总共弹起来多少次（最小0.01ｍ弹起高度）．
            总共走了多少米
"""
# 10:45

hight = 100
count = 0
distance = hight
# 判断小球弹起来的高度
while hight / 2 >= 0.01:
  count += 1
  hight /= 2  # 弹起来
  print(hight)
  # 累加弹起落下距离
  distance += hight * 2

print(count)
print(round(distance, 1))  # round结果还是数
print("距离是%.1f" % distance)  # 格式化字符串结果是字符串
