"""
  列表list  --> 字符串str 　
  练习：exercise04.py
"""
# 需求：根据某些逻辑，拼接字符串
# 0123456789

# str_result = ""
# for item in range(10):
#   # 缺点：每次+ ,都会产生新的字符串对象．
#   #      替换str_result变量存储的地址，而之前的对象成为垃圾
#   str_result =str_result + str(item)
# print(str_result)

list_result = []
for item in range(10):
  # 向列表追加字符(不会每次产生新对象，造成垃圾)
  list_result.append(str(item))
# list --> str
str_result = "".join(list_result)
print(str_result)












