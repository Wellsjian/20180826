"""
  字符串 --> 列表
"""
str01 = "张无忌-赵敏-周芷若"
list_result = str01.split("-")
print(list_result)

# 练习：英文单词反转
# "How are you"  --> "you are How"
str02 = "How are you"
list_result = str02.split(" ")
str_result = " ".join(list_result[::-1])
print(str_result)
