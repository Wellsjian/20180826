# 练习：(1)在控制台中录入所有学生成绩
# "请输入学生总数："
# "请录入第１个学生成绩:"
#      (2)获取总分
#      (3)获取最高分
#      (4)获取最低分

# 创建列表
list_student_score = []
student_count = int(input("请输入学生总数："))
for i in range(student_count):
  score = float(input("请输入第%d个学生成绩：" % (i + 1)))
  # 添加元素
  list_student_score.append(score)

# 容器内置函数
print("总分：%.1f" % sum(list_student_score))
print("最高分：%.1f" % max(list_student_score))
print("最低分：%.1f" % min(list_student_score))
