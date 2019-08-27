"""
  练习:
  匀变速直线运动的位移与时间公式:
  距离 = 初速度 * 时间 + 0.5 * 加速度 * 时间平方
  已知:距离,时间,初速度,
  计算:加速度
  15:35
"""

# 加速度 = (距离 - 初速度 * 时间) * 2 /  时间平方

distance = float(input("请输入距离:"))
initial_velocity = float(input("请输入初速度:"))
time = float(input("请输入时间:"))

accelerated = (distance - initial_velocity * time) *2 / time ** 2

print("加速度是:"+str(accelerated))



















