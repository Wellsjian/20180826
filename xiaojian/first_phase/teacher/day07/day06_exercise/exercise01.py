"""
3. 将1970年到2050年中的闰年，存入列表．
"""

# 传统
list_result = []
for item in range(1970, 2051):
  if item % 4 == 0 and item % 100 != 0 or item % 400 == 0:
    list_result.append(item)
print(list_result)

# 列表推倒式
list_result = [item for item in range(1970, 2051)
               if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]
print(list_result)