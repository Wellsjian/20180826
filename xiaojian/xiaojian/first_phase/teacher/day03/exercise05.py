# 练习:在控制台中录入一个成绩,显示优秀/良好/及格/不及格/有误
# 优秀:90 -- 100
# 良好:80 -- 90
# 及格:60 -- 80
# 不及格:0-60

# score = int(input("请输入成绩:"))
# if 90 <= score < 100:
#   print("优秀")
# elif 80 <= score < 90:
#   print("良好")
# elif 60 <= score < 80:
#   print("及格")
# elif 0 <= score < 60:
#   print("不及格")
# else:
#   print("成绩有误")
score = int(input("请输入成绩:"))# 15:35
if score < 0 or score >100:
  print("成绩有误")
elif score >= 90:
  print("优秀")
elif score >= 80:
  print("良好")
elif score >= 60:
  print("及格")
else:
  print("不及格")










