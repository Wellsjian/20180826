'''
list1 = [56,36,68,44,868]
将list1中所有元素的个位存入list2中
'''
list1 = [56, 36, 68, 44, 868]
list2 = [i % 10 for i in list1]
print(list2)


str1 = "I want to study Python"
list3 = str1.split(" ")
str2 = " ".join(list3[::-1])
print(str2)
