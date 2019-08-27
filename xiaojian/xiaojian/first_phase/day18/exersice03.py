"""
练习
    定义Myrange函数
    实现 for i in range(5)功能

    for i in Myrange(5)

"""



class MyRange():
    def __init__(self,number):
        self.__number = number

    def __iter__(self):
        return NumberIterator(self.__number)
class NumberIterator():

    def __init__(self, target):
        self.start = 0
        self.target = target
    def __next__(self):
        if self.start >= self.target:
            raise StopIteration
        result = self.start
        self.start += 1
        return result

for item in MyRange(5):
    print(item)

































