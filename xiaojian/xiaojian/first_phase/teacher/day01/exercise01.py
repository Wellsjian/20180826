"""
  汇率转换器
  此案例,只需要照抄,不需要理解.
"""

# 1. 获取数据(美元)
str_usd = input("请输入美元:")
int_usd = int(str_usd)
print()


# 2. 逻辑处理(美元 --> 人民币)
str_rmb = int_usd * 6.7284

# 3. 显示结果(显示人民币)
print("结果是:" + str(str_rmb))
