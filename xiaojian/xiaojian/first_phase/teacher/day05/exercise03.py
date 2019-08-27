# 练习1：将list_score列表中大于60的元素存入list01中
# 练习2：获取list_score列表中最大值．(不适用max)
list_score = [60, 85, 100, 26, 20, 90]
list01 = []
for item in list_score:
  if item > 60:
    list01.append(item)

print(list01)

# 假设第一个元素就是最大值
max_value = list_score[0]
# 依次与后面元素进行比较
for i in range(1, len(list_score)):
  # 发现更大的元素,则替换
  if max_value < list_score[i]:
    max_value = list_score[i]
print(max_value)








