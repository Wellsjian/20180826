"""
定义学生类(姓名，年龄，成绩）
    重写   __str__    __repr__
    创建一个对象，在克隆一个学生对象
    在控制台打印两个对象
"""



class Suddent:
    def __init__(self,name,score,age):
        self.name = name
        self.score = score
        self.age = age

    def __str__(self):
        return "'姓名：%s 分数：%d 年龄:%d" %(self.name,self.score,self.age)


    def __repr__(self):
        return "Suddent('%s,%d,%d')" %(self.name,self.score,self.age)

s1 = Suddent("园园",96,25)

s2 = eval("Suddent('园园',96,25)")

s3 = s1.__repr__()

print(s1)
print(s2)
print(s3)

s4 = eval('s3')
print(s4)






