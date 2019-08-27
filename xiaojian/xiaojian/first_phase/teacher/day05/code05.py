"""
  列表推导式
  练习：exercise05.py
"""
# # 需求：list01中所有元素的平方存入list02中
# # 传统写法
# list01 = [4,5,5,66,7,8,9]
# list02 = []
# for item in list01:
#   list02.append(item ** 2)
#
# print(list02)
#
# # 推导式写法
# list03 = [item ** 2 for item in list01]
# print(list03)

# 需求：list01中所有小于10的元素平方存入list02中
# 传统写法
list01 = [4, 5, 5, 66, 7, 8, 9]
list02 = []
for item in list01:
  if item < 10:
    list02.append(item ** 2)

print(list02)

# 推导式写法
list03 = [item ** 2 for item in list01 if item > 10]
print(list03)








