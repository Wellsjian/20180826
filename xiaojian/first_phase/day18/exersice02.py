
class Employee():
    pass
class EmployeeManager():
    def __init__(self):
        self.list_manager = []

    def add_employee(self,employee):
        self.list_manager.append(employee)

    def __iter__(self):
      return EmployeeIterable(self.list_manager)

class EmployeeIterable():
    def __init__(self,target):
        self.target = target
        self.index = 0
    def __next__(self):

        if self.index > len(self.target)-1:
            raise StopIteration

        result = self.target[self.index]

        self.index += 1
        return result


manage = EmployeeManager()
manage.add_employee(Employee())
manage.add_employee(Employee())
manage.add_employee(Employee())
manage.add_employee(Employee())
# for item in manage:

iterable = manage.__iter__()
print(iterable)
while True:
    try:
        item = iterable.__next__()
        print(item)

    except StopIteration:
       break



















