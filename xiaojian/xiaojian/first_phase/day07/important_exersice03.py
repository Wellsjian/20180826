'''
列表为[3,4,45,5,7,9]
从小大大排序
思想：
    列表中的元素两两进行比较
    1.拿第一个元素进行比较
    2.拿第二个元素和后面的进行比较
    3.继续拿第三个元素和后面的进行比较
    ........
    发现后面的元素更小，则交换两元素
    交换两个元素（拿的   更小）


'''

# list1 = [3,4,45,5,7,9]
# # list1[0]   list1[1]  list1[2]  ...
# # list2 = []
# for i in range(len(list1) -1 ):
#     for j in  range(i + 1 ,len(list1)):
#         if list1[i] > list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)

'''
判断列表中是否有相同元素
'''

list2 = [3,4,45,5,7,2]

flag = False
for r in range(len(list2) - 1):
    for c in range(r + 1 , len(list2)):
        if list2[r] == list2[c]:
            flag = True
            print("有相同元素.")
            break

    if flag:
        break
if not flag:
    print("没有相同元素.")
















