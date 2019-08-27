"""
静态方法
将函数放在类中    ，就是静态方法
"""

class Victor:
    """
    定义向量
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y


    #静态方法：如果方法中没有参数，则可以使用静态方法
    #           调用该方法时， 不会传递任何信息
    @staticmethod
    def get_right():
        return Victor(0,1)
    @staticmethod
    def get_up():
        return Victor(-1,0)

pos01 = Victor(1,2)
#表示向右   01
# 通过静态方法 实现 点 向右
right = Victor.get_right()

#表示向上
# up = Victor(-1,0)

# pos01 点 向右
pos02 = Victor(pos01.x +right.x,pos01.y + right.y)
print(pos02.x,pos02.y)
"""
00   01   02   03
10   11   12   13
20   21   22   23
"""











