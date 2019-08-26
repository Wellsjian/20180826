# 在控制台中录入4个数字，显示最大的数字
#
# 提示：
# 假设第一个最大，依次和后面的进行比较
# 遇到大的 则替换之

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








