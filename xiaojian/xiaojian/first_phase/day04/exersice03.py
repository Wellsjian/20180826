'''
1.在控制台中获取一个字符串
打印每个字符的编码值
2.在控制台中，重复录入一个编码值，打印字符，
如果没有编码值，直接回车，则退出循环
'''

# str = input("请输入一个字符串：")
# for i in str:
#     print(ord(i))

while True:
    number = input("请输入一个编码值：")
  
    if not number:
        break
    print(chr(int(number)))
