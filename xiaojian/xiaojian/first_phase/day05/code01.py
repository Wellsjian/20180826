'''
列表

'''

#1. 创建列表
list1 = []
list2 = list(range(5)) #括号里为可迭代对象
print(list2)

# 2.添加元素
# 结尾追加
list2.append("孙悟空")
list2.append("孙悟空")
list2.append("孙悟空")
print(list2)
# 指定位置插入
list2.insert(1,"猪八戒")
print(list2)


# 3.删除
# 根据元素删除
list2.remove("孙悟空")
print(list2)
#根据索引删除
del list2[6]
print(list2)

# 4.修改元素
list2[4] = "杀神"
print(list2)

# 5.索引 切片:定位元素
# 通过切片来获取一个新列表
list3 = list2[::3]
print(list3)
# 通过切片来修改元素
list3[:2:] = ["ab"]
print(list3)

# 6.　索引　＋　ｆｏｒ 定义元素
# 获取列表中每个元素
# 正向
for i in range(len(list2)):
  print(list2[i])
  # list2[i] =0

# 倒序
for i in range(len(list2)-1,-1,-1):
  print(list2[i])

# 正向跳着
for i in range(0,len(list2),2):
  print(list2[i])

list03 = [4,54,5,566,7]
result = sum(list03)
print(result)

#永久性排序
# list03.sort()
# print(list03)
list03.sort(reverse=True)
print(list03)



















