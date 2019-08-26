"""
4. 彩票　双色球：
红球:7个，1 -- 33 之间的整数   不能重复
蓝球:１个，1 -- 17 之间的整数
(1) 随机产生一注彩票[7个红球１个蓝球].
"""
import random

list_ticket = []
# ７个不重复的红球
while len(list_ticket) < 7:
  number = random.randint(1, 33)
  if number not in list_ticket:
    list_ticket.append(number)
# 1个蓝球
list_ticket.append(random.randint(1, 17))

print(list_ticket)
