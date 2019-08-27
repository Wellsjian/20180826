"""
  元组
  练习：exercise01.py
       exercise02.py
"""

#1. 创建元组
# --空元组
t01 = ()
t01 = tuple()
# --具有默认值的元组
t01 = (1,"a")
# 列表(可变)：预留空间
# 元组(只读)：按需分配
t01 = tuple([1,2,3,4,5])
list01 = list(t01)

# t02 = (1)  # 此时为整数１，并非元素１
t02 = (1,)

t03 = 1,2,3,4 # 创建元祖时，可以省略小括号

# 2. 通过切片／索引获取元素
print(t03[:2])
print(t03[2])

# 3. 获取所有元素
for item in t03:
  print(item)

# 通过索引
for index in range(len(t03)):
  print(t03[index])

for index in range(len(t03)-1,-1,-1):
  print(t03[index])







