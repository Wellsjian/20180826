"""
4. 定义在控制台中打印二维列表的函数
二维列表：
[
    [2,4,0,8,"a"],
    [0,2,4],
    [4,0],
    [0,2,2,0],
]
打印结果：
2   4   0  8   a
0   2   4
4   0
0   2   2  0
"""
def print_double_list(list_target):
  """
    在控制台中打印二维列表
  :param list_target: 列表
  :return:
  """
  for r in range(len(list_target)):
    for c in range(len(list_target[r])):
      print(list01[r][c], end=" ")
    print()

# ----------------------------------

list01 = [
  [2, 4, 0, 8, "a"],
  [0, 2, 4],
  [4, 0],
  [0, 2, 2, 0],
]

print_double_list(list01)
