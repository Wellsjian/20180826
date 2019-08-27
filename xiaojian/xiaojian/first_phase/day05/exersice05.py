'''
英文单词反转
how are you   --->>   you are hao
'''

# string = input("请输入一个字符串：")

str1 = "How are you"

list1 = str1.split(" ")


list3 = " ".join(list1[::-1])
print(list3)