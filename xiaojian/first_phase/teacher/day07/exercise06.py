# 练习:判断列表中是否具有相同元素
# 思路：列表中所有元素俩俩比较，发现相同元素即得到结论
#      所有元素比较后，没有发现元素即得到结论
list01 = [3, 4, 45, 5, 7, 1]
"""
#　假设没有相同元素
result = False
for r in range(len(list01) - 1):
  for c in range(r + 1, len(list01)):
    if list01[r] == list01[c]:
      print("具有相同元素")
      result = True

if not result:
  print("没有相同元素")
"""

# 　假设没有相同元素
result = False
for r in range(len(list01) - 1):
  for c in range(r + 1, len(list01)):
    if list01[r] == list01[c]:
      print("具有相同元素")
      result = True
      # 后续循环不再执行
      break  # 跳出内层循环

  if result:# 如果有结论，则跳出外层循环
    break

if not result:
  print("没有相同元素")
