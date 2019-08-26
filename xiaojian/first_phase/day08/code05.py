
'''
函数形式参数
'''

# 位置形参
def fun01(z,b,c):
    pass


# *  星号元组形参，让实参个数无限制
def fun02(*a):
    print(a)

#可以不传，也可以传递多个参数
#让实参个数无限制
fun02([1,2,3])
fun02(1,2,3,4)
fun02(...)

#命名关键字形参： 要求必须以关键字传参
def fun03(*,a,b):
    print(a)
    print(b)

fun03(b=8,a=5)

# *号后面的形参都是关键字传参
def fun05(*args,a,b):
    print(a)
    print(b)
    print(args)

fun05(12,8,59,a=1,b=2)

#双星号字典传参,实参可以传递多个参数
def fun06(**kwargs):
    print(kwargs)

fun06(a=1,c=3,b2=69)





