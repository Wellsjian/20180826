#!/usr/bin/env python3

import random

all_list = ["石头", "剪刀", "布"]
computer = random.choice(all_list)


you = input('1.石头\n2.剪刀\n3.布\n清出拳(1|2|3):')
win_list = [['石头','剪刀'], ['剪刀', '布'], ['布', '石头']]
if all_list[int(you)-1] == computer:
    print("平局")

elif [all_list[int(you)-1], computer] in win_list:
    print("你赢")
else:
    print("计算机赢")





