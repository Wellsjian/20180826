 # 列表中比较多个元素大小：并输出：[3,4,45,5,7,9]
# 从小到大排序
# 重点：列表中的元素，两两比较.
# 思想：
# 拿第一个元素,与后面元素进行比较
# 拿第二个元素,与后面元素进行比较
# 拿第三个元素,与后面元素进行比较
# .....
# 拿（倒数第二个元素）
# 交换：
# 发小后面的元素更小
# 交换两个元素(拿的　更小)

"""
list01 = [3,4,45,5,7,9]
# list01[0]  list01[1 --> 5]
for c in range(1,len(list01)):
  # 比较　list01[0]  list01[c]
  pass

# list01[1]   list01[2 --> 5]
for c in range(2,len(list01)):
  # 比较　list01[1]  list01[c]
  pass

# list01[2]   list01[3 --> 5]
for c in range(3,len(list01)):
# 比较　list01[2]  list01[c]
  pass

#--------结论----------
list01 = [3, 4, 45, 5, 7, 9]
for r in range(len(list01) - 1):
  # for c in range(r + 1, len(list01)):
    # 比较　list01[r]  list01[c]
    pass
"""
#主程序
list01 = [3, 4, 45, 5, 7, 9]
# 外层循环:拿数据
for r in range(len(list01) - 1):  # 0          1
  # 内层循环:做比较
  for c in range(r + 1, len(list01)):  # 1->5  2->5
    # 发现更小的再交换
    if list01[r] > list01[c]:
      list01[r], list01[c] = list01[c], list01[r]

print(list01)


# 2.相同种类的延续
'''
判断列表中是否有相同元素
'''

list2 = [3,4,45,5,7,2]

flag = False
for r in range(len(list2) - 1):
    for c in range(r + 1 , len(list2)):
        if list2[r] == list2[c]:
            flag = True
            print("有相同元素.")
            break

    if flag:
        break
if not flag:
    print("没有相同元素.")
'''    
在控制台中录入4个数字，显示最大的数字

提示：
假设第一个最大，依次和后面的进行比较
遇到大的 则替换之
'''

number1 = int(input("请输入第一个数字："))
number2 = int(input("请输入第二个数字："))
number3 = int(input("请输入第三个数字："))
number4 = int(input("请输入第四个数字："))

# 假设第一个最大，依次和后面的进行比较
# 遇到大的 则替换之
max_value = number1

if max_value <= number2:
    max_value = number2

if max_value <= number3:
    max_value = number3

if max_value <= number4:
    max_value = number4

print("最大数是"+str(max_value))
















