"""
练习2 ：
    为学习和玩耍功能统计时间
"""
import time


def calculate_all_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        cost_time = start_time - time.time()
        print("执行时间是", cost_time)
        return result

    return wrapper


class Student:
    # def __init__(self,func):
    #     self.func = func

    # def calculate_all_time(self,func):
    #     def wrapper(*args,**kwargs):
    #         self.start_time = time.time()
    #         result = func(*args,**kwargs)
    #         cost_time = self.start_time - time.time()
    #         print("执行时间是",cost_time)
    #         return result
    #     return wrapper
    @calculate_all_time
    def study(self, *args, **kwargs):
        print("学习")
        time.sleep(2)
        # cost_time = self.start_time - time.time()
        # return  cost_time

    @calculate_all_time
    def play(self, *args, **kwargs):
        print("玩耍")
        time.sleep(3)


student = Student()
student.study()
student.play()
