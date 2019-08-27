'''
列表推导式
'''

list1 = [4, 5, 5, 66, 7, 8, 9]

# 传统写法
list2 = []
for i in list1:
    if i < 10:
        list2.append(i ** 2)
print(list2)

# 推导式写法
list3 = [i ** 2 for i in list1 if i < 10]
print(list3)
