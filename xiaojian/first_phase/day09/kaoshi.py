'''
练习1
# '''
# list0101 = (1,2,3,4)
# n =0
# for i in list0101:
#     for j in list0101:
#         for k in list0101:
#             if i!=j and j!=k and i!=k:
#                 n+=1
#                 print("%s%s%s"%(i,j,k))
# print(n)


'''
练习2
'''
#
# count = 0
# while count < 3:
#     name = input("请输入您的用户名：").strip()
#     if name != "songwei":
#         count += 1
#         print("登录失败，还有%d次机会"%(3-count))
#         continue
#     password = input("请输入密码：")
#     if password != "123":
#         count += 1
#         print("登录失败，还有%d次机会" % (3 - count))
#         continue
#     else:
#         print("登录成功")
#         break
'''
# 练习3
# '''
# name = "alLLLladadaDASDEWQRCax"
# print(name.startswith("al"))
# print(name.endswith("x"))
# print(name.replace("l","p"))
# print(name.split("l"))
# print(name.upper())
# print(name.lower())
# print(name.istitle())
# print(name.capitalize())
# print(name.title())
# print(name.lower())
# print(name.casefold()) #把整个字符串的所有大写字母变为小写


'''
练习4
'''
# nunber = int(input("请输入数字（1-7）:"))
# dict01 = {1:"星期一",2:"星期二",3:"星期三",4:"星期四",5:"星期五",6:"星期六",7:"星期七"}
# if nunber in (1,2,3,4,5):
#     print(dict01[nunber]+":工作日")
# elif nunber in (6,7):
#     print(dict01[nunber]+":休息日")
# else:
#     print("输入错误.")

"""
练习六
"""
# list01  = []
# for i in range(1,4):
#     x = int(input("请输入第%d个数："%i))
#     list01.append(x)
# # for i in range(len(list01)):
# #     for j in range(i+1,len(list01)):
# #         if list01[i] > list01[j]:
# #             list01[i],list01[j] = list01[j],list01[i]
# list01.sort()
#
# print(list01)

"""
练习七
# """
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
result = day
list_all_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month > 2:
    result += sum(list_all_day[:month - 1]) + 1
    print(result)
else:
    result += sum(list_all_day[:month - 1])
    print(result)
print("这是一年第%d天" % result)

# list01 = [1000000,600000,400000,200000,100000,0]
# list02 = [0.01,0.15,0.03,0.05,0.075,0.1]
#
# profit = int(input("请您输入当月利润："))
# bonus = 0
# for i in range(len(list01)):
#     if  list01[i] < profit:
#         bonus += (profit -list01[i])*list02[i]
#         # print((profit -list01[i])*list02[i])
#         profit = list01[i]
# print(bonus)

#
# #
# # 90000     90000*0.1  = profit * 0.1
#              profit*list020[5]
# #
# # 150000    (150000-100000)* 0.75 + 100000*0.1
#                (profit-list01[4])*list02[4]
#                list01[4]*list02[5]
# # 250000    (250000-200000)*0.05 + 200000-100000*0.75 +100000*0.1
#              profit -list01[3]*list02[3]
#              (list01[3]-list01[4])
#


#
# a = dict(zip(("a","b","c","d","e"),(1,2,3,4,5)))
# print(a)
#
# print([i for i in range(9) if i in a])


#
# list01 = [1000000,600000,400000,200000,100000,0]
# list02 = [0.01,0.15,0.03,0.05,0.075,0.1]
# list01.reverse()
# list02.reverse()
# print(list01)
#
# profit = int(input("请您输入当月利润："))
# bonus = 0
