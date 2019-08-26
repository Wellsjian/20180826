'''
在控制台中录入字符串，直到输入esc为止，
将之前输入的字符串进行拼接
'''

str_all = []
while True:

    str1 = input("请输入字符串：")

    if str1 == "esc":
        break

    str_all.append(str1)

str_all = "".join(str_all)

print(str_all)

