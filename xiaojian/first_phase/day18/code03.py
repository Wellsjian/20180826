"""
迭代器
练习 ：  学生管理器
"""


# 目标： for 自定义类可迭代对象---->for 循环原理

class Student():
    pass


class StudentManager():
    def __init__(self):
        self.__student_list = []

    def add_student(self, student):
        self.__student_list.append(student)

    def __iter__(self):
        return StudentIterable(self.__student_list)  # 返回迭代器对象


class StudentIterable():
    def __init__(self, stu_list):
        self.stu_list = stu_list
        self.index = 0

    def __next__(self):
        if self.index > len(self.stu_list):
            raise StopIteration
        result = self.stu_list[self.index]
        self.index += 1

        return result


manager = StudentManager()
manager.add_student(Student())
manager.add_student(Student())
manager.add_student(Student())
manager.add_student(Student())

iterable = manager.__iter__()
print(iterable)
while True:
    try:
        item = iterable.__next__()
        print(item)
    except StopIteration:
        break
