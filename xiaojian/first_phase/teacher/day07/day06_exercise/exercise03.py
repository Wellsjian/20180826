"""
5. 计算一个字符串中的字符以及出现的次数.
abcdefce
a 1
b 1
c 2
d 1
e 2
f 1
"""
# 主题思想：
# 逐一判断字符出现的次数
# 将每个字符以及出现的次数存入一个容器{字符:出现次数,...}

str_input = "abcdefce"
dict_result = {}
for item in str_input:
  # 该字符串在字典中不存在，则新增字符与次数１
  if item not in dict_result:
    dict_result[item] = 1
  else:  # 如果存在，则累加出现次数
    dict_result[item] += 1

print(dict_result)
