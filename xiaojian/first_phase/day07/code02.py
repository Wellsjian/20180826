'''
函数
'''
"""
print("摆拳")
print("勾拳")
print("侧踹")
print("正瞪")

#.......

print("摆拳")
print("勾拳")
print("侧踹")
print("正瞪")

#.......

print("摆拳")
print("勾拳")
print("侧踹")
print("正瞪")
"""

# 做功能
def attack():
  """
    单次攻击
  :return:
  """
  print("摆拳")
  print("侧踹")
  print("勾拳")
  print("正瞪")

# 用功能
attack()
# 用功能
attack()
# 用功能
attack()

# 形参
def attack_repeat(count):
  """
    重复攻击
  :param count: 重复攻击的次数
  """
  for i in range(count):
    print("摆拳")
    print("侧踹")
    print("勾拳")
    print("正瞪")

#实参
attack_repeat(2)