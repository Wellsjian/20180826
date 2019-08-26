# 1.累加1 ---100 之间整数的和

# sum1 = 0
# for i in range(101):
#     sum1 += i
# print(sum1)

# 2.累加5 ---58 之间整数的和

# sum2 = 0
# for i in range(5,59):
#     sum2 += i
# print(sum2)

# 3.累加6 ---120 之间偶数的和

# sum3 = 0
# for i in range(6,21,2):
#     print(i,end="  ")
#     sum3 += i
# print()
# print(sum3)

# 4.累加10 ---50 之间个位数字是 2 5 8 的整数

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







