# 练习1:在控制台中,获取一个字符串.
#      打印每个字符的编码值
str_input = input("请输入字符串:")
for item in str_input:
  print(ord(item))

# 练习2:在控制台中,重复录入一个编码值,打印字符.
#      如果没有输入编码值,而直接回车,则退出循环.
while True:
  str_code = input("请输入编码值:")
  if str_code == "":
    break
  print(chr(int(str_code)))

# 15:12 上课
