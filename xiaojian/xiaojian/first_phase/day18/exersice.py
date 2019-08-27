"""
1.三合一
2.当天练习独立完成
3.定义学生类（姓名，年龄，性别，成绩）
    定义生成器函数：获取所有女同学
    定义生成器函数：获取年龄大于30岁的所有同学
    定义生成器函数：获取列表中成绩小于60岁的所有学生
4.准备面向对象答辩
5.阅读重构，head first 两本书
"""


class Student:
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score


class StudentManager:
    def __init__(self):
        self.stu_list = []

    def add_student(self, student):

        self.stu_list.append(student)
        return self.stu_list
    #
    # def get_women_student(self):
    #     for item in self.stu_list:
    #         if item.sex == "女":
    #             yield item
    #
    # def get_score_student(self):
    #     for item in self.stu_list:
    #         if item.score >= 60:
    #             yield item
    #
    # def get_age_student(self):
    #     for item in self.stu_list:
    #         if item.age >= 30:
    #             yield item


manager = StudentManager()

manager.add_student(Student("王", 25, "男", 59))
manager.add_student(Student("李", 27, "女", 95))
manager.add_student(Student("赵", 35, "女", 85))
manager.add_student(Student("张", 28, "男", 90))
#
# result = manager.get_women_student()
# result1 = manager.get_score_student()
# result2 = manager.get_age_student()
result3 =(item.name for item in manager.stu_list if item.sex == "女")
for item in result3:
    print(item)
result4 =(item.age for item in manager.stu_list if item.age > 30)
for item in result4:
    print(item)
result5 =(item.score for item in manager.stu_list if item.score > 60)
for item in result5:
    print(item)
