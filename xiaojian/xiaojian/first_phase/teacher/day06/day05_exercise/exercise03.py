"""
  (2) 在控制台中购买一注彩票
  提示：
      "请输入第1个红球号码："
      "请输入第2个红球号码："
      "号码不在范围内"
      "号码已经重复"
      "请输入蓝球号码："
"""

list_ticket = []
# ７　个红球
while len(list_ticket) < 7:
  number = int(input("请输入第%d个红球号码：" % (len(list_ticket) + 1)))
  if number < 1 or number > 33:
    print("号码不在范围内")
  elif number in list_ticket:
    print("号码已经重复")
  else:
    list_ticket.append(number)


while True:
  number = int(input("请输入蓝球号码："))
  if 1 <= number <= 17:
    list_ticket.append(number)
    break
  else:
    print("号码不在范围内")
