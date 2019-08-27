

class Dog:
    def __init__(self,name):
        self.name = name

    @classmethod
    def speak(cls):
        print("%s可以说话了." )

    def sing(self):
        print("我可以唱歌.")

    @staticmethod
    def play(self):
        print("那真是个失误啊")


