'''
定义函数，实现数值相加
'''

def get_sum(*args):
    sum = 0
    for i in args:
        sum += i

    return sum

print(get_sum(1,2,5,65))

a= [1,3,5,69]
print(sum(a))

def fun03(a,b,*args):
    print(a)
    print(b)
    print(args)

fun03(1,2,3,4)







