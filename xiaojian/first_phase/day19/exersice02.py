"""
用lambda方法来改写技能类
"""
class SkillSysterm:
    def __init__(self, skill_name, attack, CD_time, atk_speed):
        self.skill_name = skill_name
        self.attack = attack
        self.CD_time = CD_time
        self.atk_speed = atk_speed

def get_skill(list, func):
    for item in list:
        if func(item):
            yield item

list = [
    SkillSysterm("一阳指", 15, 0, 3),
    SkillSysterm("降龙十八掌", 14, 9, 5),
    SkillSysterm("九阴真金", 20, 8, 9),
    SkillSysterm("旋风腿", 5, 10, 6)
]

for item in get_skill(list, lambda item: item.CD_time == 0):
    print(item.skill_name)
for item in get_skill(list, lambda item: item.attack > 10):
    print(item.skill_name)
for item in get_skill(list, lambda item: item.atk_speed < 5):
    print(item.skill_name)
