# 练习：在控制台中获取一个字符串．
#  打印第一个字符
#  打印最后一个字符
#  如果长度是奇数，打印中间的字符
#  打印倒数３个字符
#  倒序打印字符串
str_input = "abcde"
#  打印第一个字符
print(str_input[0])
#  打印最后一个字符
print(str_input[len(str_input)-1])
print(str_input[-1])
#  如果长度是奇数，打印中间的字符
if len(str_input) % 2 ==1:
  print(str_input[len(str_input) // 2])
# 打印倒数３个字符
print(str_input[-3:])
#  倒序打印字符串
print(str_input[::-1])