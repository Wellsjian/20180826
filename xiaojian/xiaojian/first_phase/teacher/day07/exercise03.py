# 练习１：
# 在控制台中随意输入字符串
# 输入esc则停止,然后打印所有不重复字符串.

set_result = set()

while True:
  str_input = input("请输入：")
  if str_input == "esc":
    break
  set_result.add(str_input)

for item in set_result:
  print(item)
