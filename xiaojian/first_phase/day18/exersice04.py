"""
改写  1.  员工管理器
改写  2.   myrange
*********体会程序执行过程，理解生成器代码生成规则
"""
# 练习1
class Employee():
    pass
class EmployeeManager():
    def __init__(self):
        self.list_manager = []

    def add_employee(self,employee):
        self.list_manager.append(employee)

    def __iter__(self):
      # return EmployeeIterable(self.list_manager)

        for item in self.list_manager:
            yield item

# class EmployeeIterable():
#     def __init__(self,target):
#         self.target = target
#         self.index = 0
#     def __next__(self):
#
#         if self.index > len(self.target)-1:
#             raise StopIteration
#
#         result = self.target[self.index]
#
#         self.index += 1
#         return result
manage = EmployeeManager()
manage.add_employee(Employee())
manage.add_employee(Employee())
manage.add_employee(Employee())
manage.add_employee(Employee())
iterable = manage.__iter__()
# print(iterable)
while True:
    try:
        item = iterable.__next__()
        print(item)

    except StopIteration:
       break

# 练习2/
class MyRange():
    # def __init__(self,number):
    #     self.__number = number
    #     self.__start_number = 0

    def __iter__(self,number):
        self.__start_number = 0
        while number > self.__start_number :
            result = self.__start_number
            self.__start_number += 1
            yield result

# class NumberIterator():
#
#     def __init__(self, target):
#         self.start = 0
#         self.target = target
#     def __next__(self):
#         if self.start >= self.target:
#             raise StopIteration
#         result = self.start
#         self.start += 1
#         return result

for item in MyRange().__iter__(5):
    print(item)