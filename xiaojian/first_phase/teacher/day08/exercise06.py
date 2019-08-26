# 练习:统计一个函数的执行次数.

count = 0

def fun01():
  global count
  count += 1

fun01()
fun01()
fun01()
fun01()
fun01()
print("执行了%d次"%count)