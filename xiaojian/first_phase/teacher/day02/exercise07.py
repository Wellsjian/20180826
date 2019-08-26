# 练习:在控制台中录入一个四位整数 1234
#     计算每位相加和. 1+2+3+4
# 16:05

# 1234
number = int(input("请输入4位整数:"))
# 个位4
# unit01 = number % 10
# # 十位  1234 // 10  --> 123 % 10 --> 3
# unit02 = number // 10 % 10
# # 百位  1234 // 100  --> 12 % 10 --> 2
# unit03 = number // 100 % 10
# # 千位  1234 // 100  --> 12 % 10 --> 2
# unit04 = number // 1000
# result = unit01 + unit02 + unit03 + unit04
# print("结果是:"+str(result))

#---------------累加--------------------------
result = number % 10
# result = result + number // 10 % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
print("结果是:"+str(result))

