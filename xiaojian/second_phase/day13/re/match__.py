"""
match 对象实例
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"

regex = re.compile(pattern)

obj = regex.search("abcdefghi")

#属性变量
# print(obj.pos)#0  匹配的目标字符串开始位置
# print(obj.endpos)#9  匹配的目标字符串结束位置
# print(obj.re)#re.compile('(ab)cd(?P<pig>ef)') 正则表达式
# print(obj.string)#abcdefghi  目标字符串
# print(obj.lastgroup)#pig  最后一组的名称
# print(obj.lastindex)#2  最后一组的序号

#属性方法

print(obj.span())#(0, 6)  获取匹配内容的起止位置
print(obj.start())#0  获取匹配内容的开始位置
print(obj.end())#6  获取匹配内容的结束位置
print(obj.groupdict()) #{'pig': 'ef'}  获取捕获组字典,组名为键,对应内容为值
print(obj.groups()) #('ab', 'ef')   获取子组对应内容
print(obj.group()) #abcdef  功能:获取match对象匹配内容
            #     参数:默认为0表示获取整个match对象内容,如果是序列号或者组名则表示获取对应子组内容
            #     返回值:匹配字符串


