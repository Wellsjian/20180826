'''
将下列代码，定义在函数中，在调用函数，打印三角形
'''

def print_triangle(ranks,char):
    """

    :param ranks:打印三角形的行数
    :param char:打印三角形填充的元素
    :return:
    """


    for i in range(ranks):
        for j in range(i+1):
            print(char, end=" ")
        print()

print_triangle(5,"*")
