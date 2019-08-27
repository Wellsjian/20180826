"""
3. 定义在控制台中打印矩形的函数
    for r in range(2):  # 0          1
      # 内层循环控制列
      for c in range(3):  # 012     012
        print("*", end=" ")
      print()  # 换行
"""


def print_rect(r_count, c_count, char):
  """
    控制台在中打印矩形
  :param r_count: 行数量,int类型.
  :param c_count: 列数量,int类型.
  :param char: 填充矩形的字符，str类型.
  :return:
  """
  for r in range(r_count):  # 0          1
    # 内层循环控制列
    for c in range(c_count):  # 012     012
      print(char, end=" ")
    print()  # 换行


print_rect(3, 2, "*")
print_rect(2, 6, "#")











