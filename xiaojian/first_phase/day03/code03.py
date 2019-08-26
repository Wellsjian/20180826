'''
条件表达式
'''

sex = input("请您输入性别：")
# if sex = "男":
#     value = 1
# else:
#     value = 0

# 根据条件，选择性的为变量赋值
value = 1 if sex == "男"  else 0
print(value)