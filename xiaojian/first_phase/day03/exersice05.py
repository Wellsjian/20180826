# 在控制台中录入一个成绩，显示优秀/良好/及格/不及格/有误
# 优秀   90--100
# 良好   80--90
# 及格   60--80
# 不及格 低于60


score = int(input("请输入您的成绩："))

if 0 <= score <= 100:
    if 90 <= score <= 100:
        print("优秀")
    elif 80 <= score :
        print("良好")
    elif 60 <= score :
        print("及格")
    else:
        print("不及格")

else:
    print("您的输入有误")

