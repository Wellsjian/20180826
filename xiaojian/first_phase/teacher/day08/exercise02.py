# 练习：定义函数，根据成绩，判断等级.
# score = int(input("请输入成绩:"))
# if score < 0 or score >100:
#   print("成绩有误")
# elif score >= 90:
#   print("优秀")
# elif score >= 80:
#   print("良好")
# elif score >= 60:
#   print("及格")
# else:
#   print("不及格")

"""
def get_score_level(score):
  if score < 0 or score > 100:
    return "成绩有误"
  elif score >= 90:
    return "优秀"
  elif score >= 80:
    return "良好"
  elif score >= 60:
    return "及格"
  else:
    return "不及格"

score = int(input("请输入成绩:"))
level = get_score_level(score)
print(level)
"""

# return 可以退出函数
def get_score_level(score):
  if score < 0 or score > 100:
    return "成绩有误"
  # 如果程序执行到35行代码,程序退出.
  # 如果程序执行到38行代码,意味着34行的条件不满足
  if score >= 90:
    return "优秀"
  if score >= 80:
    return "良好"
  if score >= 60:
    return "及格"
  return "不及格"

print(get_score_level(100))



