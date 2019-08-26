"""
主动抛出异常
自定义异常类
练习  ：
        通过人为抛出异常，限制老婆体重范围
"""
class Wife():
    def __init__(self,weight):
        self.weight = weight
    @property
    def weight(self):
        return  self.__weight

    @weight.setter
    def weight(self,value):
        if 50 <= value <= 70:
            self.__weight = value
        else:
            raise WeightError(value,"超出范围了","代码错误")


class WeightError(Exception):
    def __init__(self,value,str_weigt,code):
        super().__init__()
        self.weight_value = value
        self.str_weight = str_weigt
        self.code = code

try:
    w01 = Wife(80)
    print("我的了")

except WeightError as a:
    print("错误提示：",a.str_weight)
    print("错误数值：",a.weight_value)
    print("错误代码：",a.code)















