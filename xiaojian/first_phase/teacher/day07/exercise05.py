# [3,4,45,5,7,9]
# 从小到大排序
# 重点：列表中的元素，两两比较.
# 思想：
# 拿第一个元素,与后面元素进行比较
# 拿第二个元素,与后面元素进行比较
# 拿第三个元素,与后面元素进行比较
# .....
# 拿（倒数第二个元素）
# 交换：
# 发小后面的元素更小
# 交换两个元素(拿的　更小)

"""
list01 = [3,4,45,5,7,9]
# list01[0]  list01[1 --> 5]
for c in range(1,len(list01)):
  # 比较　list01[0]  list01[c]
  pass

# list01[1]   list01[2 --> 5]
for c in range(2,len(list01)):
  # 比较　list01[1]  list01[c]
  pass

# list01[2]   list01[3 --> 5]
for c in range(3,len(list01)):
# 比较　list01[2]  list01[c]
  pass

#--------结论----------
list01 = [3, 4, 45, 5, 7, 9]
for r in range(len(list01) - 1):
  for c in range(r + 1, len(list01)):
    # 比较　list01[r]  list01[c]
    pass
"""

list01 = [3, 4, 45, 5, 7, 9]
# 外层循环:拿数据
for r in range(len(list01) - 1):  # 0          1
  # 内层循环:做比较
  for c in range(r + 1, len(list01)):  # 1->5  2->5
    # 发现更小的再交换
    if list01[r] > list01[c]:
      list01[r], list01[c] = list01[c], list01[r]

print(list01)
