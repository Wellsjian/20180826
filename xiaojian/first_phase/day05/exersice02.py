'''
在控制台中录入多个学生姓名
如果有重复的名字，则不存入列表
如所输入esc，则停止录入
每行打印出学生姓名

'''


student_name = input("请输入学生姓名：")

list1 = []

while True:
    student_name = input("请输入学生姓名：")

    if student_name == "esc":
        break


    elif student_name   in list1:
        continue

    list1.append(student_name)


for i in list1:
    print(i)

for index in range(len(list1) - 1 ,-1 ,-1):
    print(list1[index])





