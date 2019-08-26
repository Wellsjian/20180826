"""
函数内存
"""
def fun01(a):
    a = 2
nember = 500
print(fun01(nember))
print(nember)

# 在内存的方法区存储函数的字节码．（方法体不执行）
def fun01(a):
  a = 600


num01 = 500

# 调用函数，会在内存中开辟空间(栈帧)，存储函数内定义的变量．
fun01(num01)
# 函数执行完毕后,栈帧立即释放．
print(num01)  # 500 函数内部的修改，不影响外部.


def fun02(p1):
  # 修改的是fun02栈帧中p1变量
  p1 = [300, 500]


num02 = [100, 200]
fun02(num02)
print(num02)  # [100,200] 函数内部的修改，不影响外部.


def fun03(p1):
  # p1 变量指向的列表第一个元素
  p1[0] = 300


num03 = [100, 200]
fun03(num03)
print(num03[0])  # 300 函数内部的修改，影响外部.