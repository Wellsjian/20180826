"""
re 模块的使用
"""

import re
# s = "Alex:1994,sunny:1933"
# pattern = r"\w+:\d+"
# l = re.findall(pattern,s)
# print(l)#['Alex:1994', 'sunny:1933']
#
# pattern1 = r"(\w+):\d+"
# l1 = re.findall(pattern1,s)
# print(l1)#['Alex', 'sunny']
#
# pattern2 = r"(\w+):(\d+)"
# l2 = re.findall(pattern2,s)
# print(l2)#[('Alex', '1994'), ('sunny', '1933')]
#
# #使用combine对象调用
# pattern3 = r"(\w+):(\d+)"
# regex = re.compile(pattern3)
# l = regex.findall(s,0,10)
# print(l)
#
# #按照匹配到的内容来切割
# s = "Alex:1994,sunny:1933"
# # l = re.split(r":|,",s)
# l = re.split(r"[:,]",s)
# print(l)
#
# #按照匹配的内容来替换
#
# s = "Alex:1994,sunny:1933"
# l = re.sub(r",","*******",s)
# print(l)
#
# l = re.subn(r":","+++++++",s)
# print(l)
#
# #按照
# s = """
# 2019-06-01 今天是儿童节,妈妈给我买了个新铅笔盒
# 2019-07-05 今天我打架了,妈妈打了我
# 2019-10-06 今天我第一天上了学,学到了apple"""
#
# it = re.finditer(r"\d+",s)
# for i in it:
#     print(i.group())
#
# #完全匹配
# m = re.fullmatch(r"\w+","Steven")
# print(m.group())
#
# #匹配某个目标字符串的开始位置
# m1 = re.match(r"[A-Z]\w+","hello Word")
# print(m1)



s = '''beijing

hebei

zhangjiakou'''


l =re.split(r"\n\n",s)
print(l)
for i in l:
    print(i)







