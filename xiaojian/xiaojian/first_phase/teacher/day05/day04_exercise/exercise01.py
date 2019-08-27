"""
3.　在控制台中获取一个整数作为边长．
　　根据边长打印矩形．
   例如：４
       ****
       *  *
       *  *
       ****

       6
       ******
       *    *
       *    *
       *    *
       *    *
       ******2
"""
number = int(input("请输入整数："))
# 头
print("*" * number)
# 中间
for item in range(number - 2):
  print("*" + " " * (number - 2) + "*")
# 尾
print("*" * number)
