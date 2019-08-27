
"""
生成器表达式与普通列表表达式的区别
"""


# 1.列表表达式
list01  = [4,4,5,56,6,78]
# 立即执行,将所有结果存入内存
result01 = [item for item in list01 if item >5]
for item in result01:
  print(item)

# 2.生成器表达式
result02 = (item for item in list01 if item >5)
# 延迟执行,循环一次 计算一次  返回一个(覆盖了上一个)
for item in result02:
  print(item)

#生成器函数的原理是__next__内置方法的一次次循环操作，第一次for后，已经
for item in result02:
  print(item)
