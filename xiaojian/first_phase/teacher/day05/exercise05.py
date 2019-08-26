# 练习：将list01中所有元素的个位存入list02中.
list01 = [56, 36, 68, 44, 868]

list02 = []
for item in list01:
  list02.append(item % 10)

list02 = [item % 10 for item in list01]

print(list02)
