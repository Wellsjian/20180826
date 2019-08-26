"""
  计算列表中最小值(不使用min)．
"""

list01 = [3, 45, 56, 6, 7, 2, 8, 9]
min_value = list01[0]
for index in range(1, len(list01)):
  if min_value > list01[index]:
    min_value = list01[index]
print(min_value)
