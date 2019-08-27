# 删除列表中所有偶数(群讨论)
#    [3,2,4,6,8,8,5,3]
# 11:00 上课
list01 = [3, 2, 4, 6, 8, 8, 6, 3]
# for item in list01:
#   if item % 2 == 0:
#     list01.remove(item)

# 根据索引倒序删除
for i in range(len(list01)-1,-1,-1):
  if list01[i] % 2 == 0:
    # list01.remove(list01[i])
    del list01[i]
print(list01)
