'''
在控制台中录入学生信息（姓名：性别：成绩：年龄）
如果姓名输入esc,则停止输入
'''


# list01 = []
dict = {}


while True:

    name = input("请输入姓名：")

    if name == "esc":
        break

    sex = input("请输入性别：")
    score = input("请输入成绩：")
    age = input("请输入年龄：")
    dict01 = {}
    # dict["姓名："] = name
    dict01["性别"] = sex
    dict01["成绩"] = score

    dict01["年龄"] = age

    dict[name] = dict01

for i,value in dict.items():
    for key in value:

        print("%s的性别为%s 成绩是%d 年龄为%d",%(i,value["性别"],value["成绩"],value["年龄"]))



# dict_student_info = {}
# while True:
#   name = input("请输入姓名：")
#   if name == "esc":
#     break
#   sex = input("请输入性别：")
#   score = int(input("请输入成绩："))
#   age = int(input("请输入年龄："))
#   dict_student_info[name] = [sex, score, age]
#
# # 打印信息
# for key, value in dict_student_info.items():
#   print("%s的性别是%s，成绩是%d,年龄是%d." % (key, value[0], value[1], value[2]))










