'''
在控制台中录入所有学生成绩
请录入学生人数
1.请录入学生成绩
2.获取总分
3.获取最高分
4.获取最低分
'''

student_count = int(input("请输入需要录入学生的总数："))
# 创建列表
list_student_score = []

for i in range(student_count):
    score = float(input("请输入第%d个学生成绩：" % (i + 1)))
    # 添加元素
    list_student_score.append(score)
# 容器内置函数
print("总分是：%.2f" % sum(list_student_score))
print("最低分是：%.2f" % min(list_student_score))
print("最高分是：%.2f" % max(list_student_score))
