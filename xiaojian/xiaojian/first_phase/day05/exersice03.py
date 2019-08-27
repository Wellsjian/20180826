'''
1.将list_score中大于60的元素存入list01中
2.获取list_score列表中的最大值
list_score = [60,85,35,26,20,90]
'''

list_score = [60,85,35,26,20,90]
list01 = []

for i in list_score:
    if i > 60:
        list01.append(i)
print(list01)

max = list01[1]
for i in range(1,len(list01)):
    if max < list01[i]:
        max = list01[i]
print(max)

#找最大值 比较用的是小于   找最小值 ，比较的用的是大于
min1 = list_score[0]
for i in range(1,len(list_score)):
    if min1 > list_score[i]:
        min1 = list_score[i]

print(min1)










