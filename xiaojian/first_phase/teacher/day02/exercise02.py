# 练习:在控制台中录入学生信息(姓名,年龄,成绩,性别)
# 将相应的数据转换为相应的类型
# 将数据与类型输出到控制台

# 1) input函数结果是str
# 2) 类型转换

# 录入信息
name = input("请输入姓名:")
str_age = input("请输入年龄:")
str_score = input("请输入成绩:")
sex = input("请输入性别:")
# 类型转换
int_age = int(str_age)
float_score = float(str_score)
# 显示结果
print(name +"---"+ str(type(name)))
print(str_age +"---"+ str(type(int_age)))
print(str_score +"---"+ str(type(float_score)))
print(sex +"---"+ str(type(sex)))

