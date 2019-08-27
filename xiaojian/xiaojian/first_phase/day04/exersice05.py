'''
在控制台中获取一个字符串
打印第一个字符
打印最后一个字符
如果长度为奇数，打印中间的字符、
打印倒数3个字符
倒序打印字符串
'''



str = input("请输入一个字符串：")

print(str[0])
print(str[-1])
print(type(len(str)))
if len(str) % 2 == 1:
    print(str[len(str)//2])
print(str[-3::])
print(str[::-1])