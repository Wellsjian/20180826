# 练习:修改下列代码,使逻辑正确.(使用调试,查看流程与取值)

price = input("请输入商品单价:")
price = float(price)
amount = int(input("请输入数量:"))
money = float(input("请输入金额:"))
result = money - price * amount
if result >= 0:
  print("应找回:" + str(result))
else:
  print("钱不够")

