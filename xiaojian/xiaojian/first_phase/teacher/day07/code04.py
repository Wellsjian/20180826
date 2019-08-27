"""
  for for 嵌套
  练习：exercise05.py
       exercise06.py
"""

# print("*",end = " ")
# print("*",end = " ")
# print("*",end = " ")
# print()
# print("*",end = " ")
# print("*",end = " ")
# print("*",end = " ")

# 外层循环控制行
for r in range(2):  # 0          1
  # 内层循环控制列
  for c in range(3):  # 012     012
    print("*", end=" ")
  print()  # 换行

"""
    * * * 
    * * * 
"""

"""
    * # * # * 
    * # * # *
    * # * # *
"""
for r in range(3):
  for c in range(5):
    if c % 2 == 0:
      print("*", end=" ")
    else:
      print("#", end=" ")
  print()

"""
4行     内层循环
#         1次
##        2次
###       3次
####      4次
"""

for r in range(4):  # 0     1      2     3
  for c in range(r + 1):  # 0   01    012   0123
    print("#", end=" ")
  print()







