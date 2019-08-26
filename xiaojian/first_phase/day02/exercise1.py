# 在控制台依次获取两个变量
# 将两个变量变换，输出在控制台上
a = int(input('请输入第一个变量：'))
b = int(input('请输入第二个变量：'))


# 方法一：
print('a=%d,b=%d' % (a, b))
a, b = b, a
print('a=%d,b=%d' % (a, b))
# 方法二：
c = a
a = b
b = c
print('a=%d,b=%d' % (a, b))