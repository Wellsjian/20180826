# 练习1:累加1--100之间整数
sum = 0
for item in range(1, 101):
  # sum  item
  # 0 +=  1
  # 1 +=  2
  # 3 +=  3
  # 6 +=  4
  sum += item
print(sum)

# 练习2:累加5--58之间整数
sum = 0
for item in range(5, 59):
  sum += item
print(sum)

# 练习3:累加6--20之间偶数
sum = 0
for item in range(6, 21, 2):
  sum += item
print(sum)

# 练习4:累加10--50之间个位是2  5  9 的整数
sum = 0
for item in range(10, 51):  # 10  11  12  13 ...
  unit = item % 10
  if unit == 2 or unit == 5 or unit == 9:
    sum += item
print(sum)










