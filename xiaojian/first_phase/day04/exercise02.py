'''
随机加法考试
随机产生两个数字，在控制台中录取两个数字相加的结果
输入正确，10分
输入错误扣5分
总计3道题
请计算 8 + 3 =

'''
import random

count = 0
score = 0
for i in range(3):
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)

    result1 = number2 + number1

    result = int(input("请计算" + str(number1) + "+" + str(number2) + "=" + "?"))

    # count += 1
    if result == result1:
        score += 10
        print("答对了，得10分")
    else:
        score -= 5
        print("答错了，扣5分")
print("最后得分为" + str(score) + "分")
