"""
练习“
1.编写一个函数，传入一个整数，返回改整数的阶乘
2.将线性结构代码整理总结
"""


def get_factorial(number):
    if number < 1:
        return 1
    else:
        return number * get_factorial(number - 1)


print(get_factorial(1))


# # 1 1 2 3 5 8 13 21
#
def fiboqina(number):
    a, b = 0, 1
    print(b)
    while a + b < 100:
        a, b = b, a + b
        print(b)


# fiboqina(100)

l = [4, 5, 6]

print(id(l))
def fun(a):
    print(id(a))
    a = [1, 2, 3]
    print(id(a))
# return id(a)
print(id(l))
fun(l)
print(fun(l))
print(l)




def fun1():
    x = 5

    def fun2():
        nonlocal x
        x += 1
        return x

    return fun2


a = fun1()
print(a())
print(a())
print(a())

l = [1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12, [13, [14, [15]]]]]]]]]]]]]]]


def bianli(list_target):
    list01 = []
    list01.append(list_target)
    while len(list01) != 0:
        dir = list01.pop()
        for i in dir:
            if type(i) is list:
                list01.append(i)
            else:
                print(i)

# bianli(l)
#递归思想
def bianli1(list_arget):
    for i in list_arget:
        if type(i) is not list:
            print(i)
        else:
            bianli1(i)
# bianli1(l)
import re
def number2(num):
    number1 = str(num)
    list = []
    while len(list) != 0:
        res = re.search(r"\d+", number1).group()
        for i in range(len(res) - 1, -1, -1):
            list.append(res[i])
        res1 = "".join(list)

        if number1[0] == "-":
            res2 = "-" + res1
            return int(res2)
        else:
            return int(res1)

print(number2(-150))




















