"""
  列表
  练习：exercise01.py
  练习：exercise02.py
  练习：exercise03.py
"""
# 1. 创建空列表
list01 = []
list01 = list()

# -- 创建具有默认元素的列表
list01 = [2,"大强",True]
list01 = list("我叫苏明玉")
list01 = list(range(5))
print(list01)

# 2. 添加元素
# -- 追加
list01.append("悟空")
list01.append("唐僧")
# 插入
print(list01)
list01.insert(1,"八戒")
print(list01)

# 3. 删除
# 根据元素
list01.remove("悟空")
# 根据索引
del list01[1]
print(list01)

# 4. 修改
list01[5] = "沙僧"
print(list01)

# 5. 通过　索引／切片(定位元素)　操作元素
# 通过切片获取一个新列表
list02 = list01[:3]

# 通过切片可以修改元素
# list01[:3] = ["a","b","c"]
list01[:3] = ["a"]
print(list01)

# 只支持：正向顺序查找
for item in list01:
  print(item)
  # item = 0 # 不能修改

# 6.　索引　＋　ｆｏｒ 定义元素
# 获取列表中每个元素
# 正向
for i in range(len(list01)):
  print(list01[i])
  # list01[i] =0

# 倒序
for i in range(len(list01)-1,-1,-1):
  print(list01[i])

# 正向跳着
for i in range(0,len(list01),2):
  print(list01[i])

list03 = [4,54,5,566,7]
result = sum(list03)
print(result)






