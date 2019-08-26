'''
字符串 --->>  列表


'''

str1 = "周芷若-赵敏-张无忌"

list1 = str1.split("-")
print(list1)

str = "让我掉下眼泪的 不止作昨夜的酒 让我依依不舍的 不止你的温柔"

list = str.split(" ")

print(list)

name = "让我掉下眼泪的"
name1 = "不止作昨夜的酒"
name2 = "让我依依不舍的"
name3 = "不止你的温柔"

list = [name, name1, name2, name3]
str_result = " ".join(list)

print(str_result)
