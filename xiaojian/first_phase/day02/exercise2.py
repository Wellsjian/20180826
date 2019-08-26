# 在控制台上录入学生信息(姓名，年龄，成绩，性别)
# 将相应的数据转换为相应的类型


name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))
score = float(input("请输入您的成绩："))
sex = input("请输入您的性别：")

print(name+ age+ score+sex)
print(type(name), type(age), type(score),type(sex))
