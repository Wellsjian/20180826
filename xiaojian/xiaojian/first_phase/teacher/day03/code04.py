"""
  while 循环
  练习:exercise07.py
      exercise08.py
      exercise09.py
"""

# 死循环,直到输入q.
# while True:
#   str_usd = input("请输入美元:")
#   int_usd = int(str_usd)
#   str_rmb = int_usd * 6.7284
#   print("结果是:" + str(str_rmb))
#
#   if input("如果退出输入q:") == "q":
#     break # 退出循环体

# 执行三次
count = 0
while count < 3:  # 0 < 3  1 <3   2<3  3 <3(不满足条件)
  str_usd = input("请输入美元:")
  int_usd = int(str_usd)
  str_rmb = int_usd * 6.7284
  print("结果是:" + str(str_rmb))
  count += 1
