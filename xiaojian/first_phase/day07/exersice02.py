'''
打印图形
* # * # *
* # * # *
* # * # *
'''
# for i in range(3):
#     for j in range(5):
#         if j % 2 == 1:
#             print("#",end=" ")
#         else:
#             print("*",end=" ")
#     print()

'''
打印图形
'''
for i in range(1,5):
    for j in range(i):
        print("#"  , end=" ")
    print()

for i in range(1,5):
    for j in range(5-i):
        print("#"  , end=" ")
    print()






