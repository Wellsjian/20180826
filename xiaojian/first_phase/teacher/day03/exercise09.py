# 猜数字游戏
# 游戏运行产生一个1--100之间随机数
# 让玩家重复猜测,直到猜对为止.
# 提示:大了,小了,猜对了,总共猜了?次.
import random

# 产生一个随机数
# random_number = random.randint(1, 100)
# count = 0
# while True:
#   count += 1
#   input_number = int(input("请输入整数:"))
#   if input_number > random_number:
#     print("大了")
#   elif input_number < random_number:
#     print("小了")
#   else:
#     print("猜对了,总共猜了" + str(count) + "次")
#     break

random_number = random.randint(1, 100)
print(random_number)
count = 0
while count < 3:
  count += 1
  input_number = int(input("请输入整数:"))
  if input_number > random_number:
    print("大了")
  elif input_number < random_number:
    print("小了")
  else:
    print("猜对了,总共猜了" + str(count) + "次")
    break
else:  # 循环结束,不是因为break,才执行else语句.
  print("游戏失败")
