
'''
短路运算
'''


# 一但结果确定，后面的语句将不再执行。
#
# 把耗时长，耗性能的内容语句放在判断的最后边+


sum4 = 0
for i in range(10,51):
    if i % 10 != 2 and i % 10 != 5 and i % 10 != 9:
        continue
    sum4 += i
print()
print(sum4)

sum4 = 0
for i in range(10,51):
    if i % 10 == 2 or i % 10 == 5 or i % 10 == 9:

        sum4 += i
print()
print(sum4)