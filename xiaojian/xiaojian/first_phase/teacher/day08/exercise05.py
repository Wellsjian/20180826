# 练习:定义函数，对列表的升序排列

# 传入的是可变类型对象
# 函数体内部，修改可变对象
# 无需通过返回值，返回结果.
def sort(list_target):
  # 外层循环:拿数据
  for r in range(len(list_target) - 1):  # 0          1
    # 内层循环:做比较
    for c in range(r + 1, len(list_target)):  # 1->5  2->5
      # 发现更小的再交换
      if list_target[r] > list_target[c]:
        list_target[r], list_target[c] = list_target[c], list_target[r]
        # return list_target


# -----------------
list01 = [3, 4, 45, 5, 7, 9]
sort(list01)
print(list01)

# print(sort(list01))
