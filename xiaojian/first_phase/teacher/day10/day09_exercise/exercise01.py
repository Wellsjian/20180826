"""
5. 创建狗类,具有姓名.体重等数据
   具有坐,吃,导盲等方法
   创建至少2对象.
   画出代码内存图.
"""

class Dog:
  def __init__(self,name,weight = 50):
    self.name = name
    self.weight = weight

  def sit_down(self):
    print(self.name + "坐下了")

d01 = Dog("米咻",60)
d02 = Dog("嘿米")
# 多个对象调用同一个方法,通过方法self参数访问对象数据.
d01.sit_down()
d02.sit_down()
d03 = d02
d03.weight = 80
print(d02.weight)# ?  11:00

