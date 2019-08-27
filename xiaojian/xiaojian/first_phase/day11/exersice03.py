"""
定义类方法 ； 获取向左的方向
            获取向下的方向
        表示0,2 的点 向左  向下
"""


class Victor2:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    def get_left():
        return Victor2(0,-1)

    @staticmethod
    def get_bottom():
        return Victor2(1,0)

post01 = Victor2(0,2)

left = Victor2.get_left()
post02 = Victor2(post01.x + left.x,post01.y + left.y)
print(post02.x,post02.y)

bottom = Victor2.get_bottom()
post03 = Victor2(post01.x + bottom.x,post01.y + bottom.y)
print(post03.x,post03.y)