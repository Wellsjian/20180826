"""
函数式编程练习
定义技能类（技能名称，攻击力，冷却时间，攻击速度）
        定义函数，功能一 ：获取冷却时间为0的所有技能
        定义函数，功能二 ：获取攻击力大于10的所有技能
        定义函数，功能一 ：获取攻击速度小于5的所有技能

    提取变化点
    定义不变的代码（客户端代码)
    测试，三个功能的实现
"""


class SkillSysterm:
    def __init__(self,skill_name,attack,CD_time,atk_speed):
        self.skill_name = skill_name
        self.attack = attack
        self.CD_time = CD_time
        self.atk_speed = atk_speed

def get_skill(list,func):
    for item in list:
        if func(item) :
            yield item
def get_cd_time(item):
    return item.CD_time == 0
def get_attack(item):
    return item.attack > 10
def get_atk_speed(item):
    return item.atk_speed < 5

list = [
    SkillSysterm("一阳指",15,0,3),
    SkillSysterm("降龙十八掌",14,9,5),
    SkillSysterm("九阴真金",20,8,9),
    SkillSysterm("旋风腿",5,10,6)
]


for item in get_skill(list,get_atk_speed):
    print(item.skill_name)

for item in get_skill(list,get_attack):
    print(item.skill_name)
for item in get_skill(list,get_cd_time):

    print(item.skill_name)















