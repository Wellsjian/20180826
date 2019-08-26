'''
1.在控制台中随意输入，
输入esc则停止
打印所有不重复元素

2.经理:曹操  刘备  孙权
技术员 ： 曹操  刘备  张飞 关羽
计算 1. 找找即是经理也是技术员的有谁
    2.只是经理不是技术元员的是有谁
    3.是技术员不是经理的有谁
    4.张飞是经理吗
    5.身兼一职的都有谁
    6.经理和技术员总共有多少人

'''

# set_result = set()
# while True:
#     str1 = input("请输入随意的字符串：")
#     if str == "esc":
#         break
#     set_result.add(str1)
#     print(set_result)

# set_result = set()
#
# while True:
#   str_input = input("请输入：")
#   if str_input == "esc":
#     break
#   set_result.add(str_input)
#
# for item in set_result:
#   print(item)

# technologist1 = frozenset(["曹操", "刘备", "张飞", "关羽"])
# technologist = {"曹操", "刘备", "张飞", "关羽"}
# manager = {"曹操", "刘备", "孙权"}
#
# print(technologist & manager)
# print(manager - technologist)
# print(technologist - manager)
# print("张飞" in manager)
# print(technologist ^ manager)
# print(len(technologist | manager))
