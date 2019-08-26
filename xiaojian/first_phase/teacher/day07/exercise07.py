# 练习：将下列代码，定义在函数中．再调用函数，绘制三角形．
# for r in range(4):  # 0     1      2     3
#   for c in range(r + 1):  # 0   01    012   0123
#     print("#", end=" ")
#   print()

def print_triangle(char,row):
  """
    打印三角形
  :param char: 填充三角形的字符
  :param row:　三角形的行数
  :return:
  """
  for r in range(row):  # 0     1      2     3
    for c in range(r + 1):  # 0   01    012   0123
      print(char, end=" ")
    print()

print_triangle("*",2)
print_triangle("#",4)
print_triangle("$",8)

