# 练习:随机加法考试
# 随机产生两个数字(1-10),在控制台中获取两个数字相加的结果.
# 如果输入正确得10分
# 如果输入错误扣除5分
# 总计3道题
# "请计算8 + 3 = ?"
# 11:42

import random

score = 0
for item in range(3):
  random_number01 = random.randint(1, 10)
  random_number02 = random.randint(1, 10)
  result_input = int(input("请计算" + str(random_number01) + " + " + str(random_number02) + " = ?"))
  if result_input == random_number01 + random_number02:
    score += 10
  else:
    score -= 5

print(score)
