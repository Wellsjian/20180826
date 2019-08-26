'''
1.三合一
2.当天练习独立完成
3.在控制台中获取一个整数作为边长
根据边长打印矩形
      4
       ****
       *  *
       *  *
       ****
      6
      ******
      *    *
      *    *
      *    *
      *    *
      ******
4.在控制台中录入一个字符串
判断是否为回文
例如 ：  上海自来水来自海上

5.（扩展题）一个小球从100米落下，每次弹回原高度的一半，
计算：1.总共弹起多少次，最小高度为0.01m
     2.总共走了多少米
6.看书python从入门到编程第五章和第七章

'''

# 3.在控制台中获取一个整数作为边长
# 根据边长打印矩形
#       4
#        ****
#        *  *
#        *  *
#        ****
#       6
#       ******
#       *    *
#       *    *
#       *    *
#       *    *
#       ******


# number = int(input("请输入矩形的边长："))
#
# for i in range(1, number + 1):
#     if i == 1 or i == number:
#         print("*" * number)
#     else:
#         print("*" + " " * (number - 2) + "*")


# number = int(input("请输入矩形的边长："))
# # 头
# print("*" * number)
# # 中间
# for i in range( number - 2):
#     print("*" + " " * (number - 2) + "*")
# # 尾巴
# print("*" * number)


# 4.在控制台中录入一个字符串
# 判断是否为回文
# 例如 ：  上海自来水来自海上
#  想法：回文字符串正过来看和倒过来看一样
# str = input("请输入一个字符串：")
#
# if str == str[::-1]:
#     print("%s字符串为回文字符串"%str)
# else:
#     print("%s字符串不是回文字符串"%str)

str01 = list((input("请输入一个字符串：")))

# str.reverse()
# print(a)

if str01 == str01.reverse():
    print("回文")
else:
    print("不是回文")





# 5.（扩展题）一个小球从100米落下，每次弹回原高度的一半，
# 计算：1.总共弹起多少次，最小高度为0.01m
#      2.总共走了多少米
#
meter = 100
count = 0
hight = 100
# 判断小球弹起的高度
while meter / 2 > 0.01:
    count += 1
    meter /= 2
    hight += 2 * meter
print(count, hight)
