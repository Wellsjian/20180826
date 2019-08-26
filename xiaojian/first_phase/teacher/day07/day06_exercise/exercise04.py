"""
6.(扩展)猜拳游戏:石头剪刀布
系统随机选择一个
用户输入一个
判断输赢

提示：将胜利策略存入容器
石头 战胜　剪刀
剪刀　　　　布
布        石头
"""
import random

# 胜利策略
dict_wins = {
  "石头": "剪刀",
  "剪刀": "布",
  "布": "石头",
}
# 随机 1   --> "布"
list_items = ("剪刀", "布", "石头")
random_number = random.randint(0, 2)
str_sys_input = list_items[random_number]

str_user_input = input("请输入：")

if str_user_input == str_sys_input:
  print("平局")
elif dict_wins[str_user_input] == str_sys_input:
  print("胜利")
else:
  print("失败")
