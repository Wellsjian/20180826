# 练习:在控制台中录入四个数字
#     显示最大的数字
# 提示:
# 假设第一个就是最大的,依次与后面的数字进行比较.
# 如果发现更大的,则替换假设的.
number01 = float(input("请输入第1个数字:"))
number02 = float(input("请输入第2个数字:"))
number03 = float(input("请输入第3个数字:"))
number04 = float(input("请输入第4个数字:"))

max_value = number01
if max_value < number02:
  max_value = number02
if max_value < number03:
  max_value = number03
if max_value < number04:
  max_value = number04
print(max_value)











