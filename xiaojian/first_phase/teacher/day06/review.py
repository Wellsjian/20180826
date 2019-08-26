"""
  day05 复习
  容器
    列表
      1. 内存图
      2. 定义:　　变量　可变　序列
      3. 适用性：存储／管理多个数据．
      4. 操作
          创建
          添加
          删除
          定位
          查询
"""
list01 = [1000, "a", ["b", 500]]
list02 = [1000, "a", ["b", 500]]

print(list01 is list02)  # ? False
print(list01 == list02)  # ? True

# -------------列表基础操作-------------
list01 = [1, 2]
list01 = list("abc")
list01.append("数据1")
list01.insert(2, "数据2")

print(list01)
list01.remove("a")
del list01[1]
print(list01)

# list01[1] = [1,2,3]# ['b', [1, 2, 3], '数据1']
list01[1:2] = [1, 2, 3]  # ['b', 1, 2, 3, '数据1']
print(list01)

# 顺序读取每个元素(简单)
for item in list01:
  print(item)

# 根据索引(灵活)
# 正向
for index in range(len(list01)):
  print(list01[index])

# 倒序
for index in range(len(list01) - 1, -1, -1):
  print(list01[index])
