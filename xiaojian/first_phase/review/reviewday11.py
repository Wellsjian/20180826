"""
  day11 复习
  类与对象
    实例成员:对象的成员,杯子.

    类成员:类的成员,饮水机.

  封装
    封装数据:多个数据 -->  一个种数据(新类型)
            例如:学生类(姓名/年龄..) 汽车(品牌/价格..)
            适用性:多种信息描述同一种事物.
    封装行为:函数只能表示一个行为.
           类可以将数据与行为合二为一,表示世间万物.
           对外提供[必要]的功能,隐藏(命名已双下划线开头)实现的细节.
    封装的设计思想:
          分而治之:将大的需求分解为多个小类,共同完成.
                 类要小而精,拒绝大而全.
          封装变化:分解的度,识别变化点,单独做成类.
          --------------------------
          高内聚:类内部,高度聚集.完成一个变化点.
          低耦合:类与类关系,尽量松散.
"""
class A:

  b = 50

  def __init__(self,a):
    self.a = a

  def fun01(self):
    print(self.a,"fun01")

# 通过对象地址访问实例成员(变量/方法)
obj01 = A(10)
print(obj01.a)
obj01.fun01()# 自动传递对象地址

# 通过类访问实例方法,但必须手动传递对象地址.(非主流)
obj02 = A(20)
A.fun01(obj01)

# 通过类访问类成员
print(A.b)
# 通过对象地址访问类成员(非主流)
print(obj01.b)





