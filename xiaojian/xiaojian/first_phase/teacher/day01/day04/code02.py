"""
  continue
"""

# sum = 0
# for item in range(10, 51):
#   # 满足条件 则累加
#   if item % 10 == 2:
#     sum += item
# print(sum)

sum = 0
for item in range(10, 51):
  # 不满足条件 则跳过本次循环
  if item % 10 != 2:
    continue

  sum += item
print(sum)
