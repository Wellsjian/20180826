'''
统计一个函数的使用次数
'''
count = 0
def fun01():

    print("我来了")
    global count
    count +=1
    # return count
fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
print(count)