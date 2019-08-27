'''
面向对象
    -----类 和对象
    定义类：具体事务，抽象化的过程
    创建对象：抽象事物，具体化的过程
'''

class wife():
    """
    老婆
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def play(self):
        print(self.name+"打游戏")

wife01 = wife("丽丽",18)
wife01.play()
wife02 = wife("莹莹",25)
wife02.play()


























