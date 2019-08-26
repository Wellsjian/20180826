"""
练习1.将通用函数定义在list_helper.py模块中，在当前模块中测试
练习2.
    功能一： 定义函数，在列表中查找”如来神掌“技能
    功能二： 定义函数，在列表中查找攻击力大于50的单个技能
    功能三： 定义函数，在列表中查找cd大于0的单个技能
    功能四： 定义函数，在列表中计算攻击力小于50的数量
    功能五： 定义函数，在列表中计算cd等于0的个数
    功能六： 定义函数，在列表中计算攻击力的总和
    功能七： 定义函数，在列表中计算攻击速度的总和
    功能八： 定义函数，在列表中获取攻击力最大的技能
    功能九： 定义函数，在列表中获取攻击速度最大的技能
    功能十： 定义函数，在列表中获取攻击力，使攻击力成为一个新的列表
    功能十一： 定义函数，在列表中获取技能名称，使技能名称成为一个新的列表
    功能十二： 定义函数，对技能列表根据攻击力进行生序排列
    功能十三： 定义函数，对技能列表根据攻击速度进行生序排列


    将通用代码定义在list_helper.py中
            将变化点使用在lambda中

"""
from project_month01.common.list_helper import ListHelper
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

# 功能一： 定义函数，在列表中查找”如来神掌“技能
# print((ListHelper.first(list,lambda e : e.skill_name =="如来神掌" )).skill_name)

# 功能二： 定义函数，在列表中查找攻击力大于50的单个技能
# print((ListHelper.first(list,lambda e : e.attack > 50)).skill_name)

# 功能三： 定义函数，在列表中查找cd大于0的单个技能
# print((ListHelper.first(list,lambda e : e.CD > 0).skill_name)

# 功能四： 定义函数，在列表中计算攻击力小于50的数量
# print( ListHelper.count(list,lambda e : e.attack < 50))

# 功能五： 定义函数，在列表中计算cd等于0的个数
# print((ListHelper.count(list,lambda e : e.CD = 0).skill_name)

# 功能六： 定义函数，在列表中计算攻击力的总和
# print(ListHelper.get_sum(list,lambda e : e.attack ))

# 功能七： 定义函数，在列表中计算攻击速度的总和
# print(ListHelper.get_sum(list,lambda e : e.atk_speed ))

# 定义函数，在列表中获取攻击力最大的技能
# print((ListHelper.get_max1(list,lambda e : e.attack)).skill_name)

# 功能九： 定义函数，在列表中获取攻击速度最大的技能
# print(ListHelper.get_max(list,lambda e : e.atk_speed))

# 功能十： 定义函数，在列表中获取攻击力，使攻击力成为一个新的列表
# for item in ListHelper.get_element(list,lambda e : e.attack):
#     print(item)
#
# 功能十一： 定义函数，在列表中获取技能名称，使技能名称成为一个新的列表
# for item in ListHelper.get_element(list,lambda e : e.skill_name):
#     print(item)
# 功能十二： 定义函数，对技能列表根据攻击力进行生序排列
for item in ListHelper.order_by(list,lambda e : e.attack):
    print(item.skill_name)
# 功能十三： 定义函数，对技能列表根据攻击速度进行生序排列
for item in ListHelper.order_by(list,lambda e : e.atk_speed):
    print(item.atk_speed)
