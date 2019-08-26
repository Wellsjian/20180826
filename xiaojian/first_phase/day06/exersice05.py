'''
创建调查问卷，
请输入姓名     esc结束
请输入您的爱好    可以很多  esc结束
'''
dict_name = {}

while True:
    name = input("请输入姓名：")
    if name == "esc":
        break

    list_favorite = []

    dict_name[name] = list_favorite

    while True:
        favorite = input("请您输入您的爱好：")
        if favorite == "esc":

            break
        list_favorite.append(favorite)


for key,value in dict_name.items():
    # for i in list_favorite:
    print("%s的爱好是%s"%(key,value))
















