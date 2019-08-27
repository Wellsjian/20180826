"""
练习，使用内置高阶函数
    1.查找技能列表中攻击力在50--100之间的所有技能
    2.在技能列表中，获取技能名称与cd的列表
    3.在技能列表中，查找攻击速度最小的技能
    4.在技能列表中，
"""
class SkillSysterm:
    def __init__(self, skill_name, attack, CD_time, atk_speed):
        self.skill_name = skill_name
        self.attack = attack
        self.CD_time = CD_time
        self.atk_speed = atk_speed


list = [
    SkillSysterm("一阳指", 15, 0, 3),
    SkillSysterm("降龙十八掌", 55, 9, 5),
    SkillSysterm("如来神掌", 20, 0, 9),
    SkillSysterm("旋风腿", 5, 10, 6)
]

for i in filter(lambda e : 50 < e.attack < 100,list):
    print(i.attack)
for item in filter(lambda e : (e.skill_name,e.CD_time),list):
    print((item.skill_name,item.CD_time))

print((min(list,key = lambda e : e.atk_speed)).skill_name)


result = sorted(list,key=lambda e:e.CD_time,reverse=True)
# sorted返回的是一个新列表，我们改变的是原有的列表，
list[:] = result
for i in list:
    print(i.CD_time)

print( (max(list,key=lambda e : e.skill_name )).skill_name)





