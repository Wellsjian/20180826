# 练习：在控制台中重复录入字符串，直到输入esc为止．
#      最后打印拼接后的字符串．
# 17:15 上课

list_result = []
while True:
  str_input = input("请输入字符串")
  if str_input == "esc":
    break
  list_result.append(str_input)
str_result = "".join(list_result)
print(str_result)