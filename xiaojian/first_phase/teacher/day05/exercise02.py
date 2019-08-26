"""
  练习：在控制台中录入多个学生姓名．
    　　如果有重复的姓名，不存入列表．
    　　如果输入esc,则停止录入．在每行打印学生姓名
  15:46
"""

list_student_name = []
while True:
  name = input("请输入学生姓名：")
  # 如果输入esc, 则停止录入
  if name == "esc":
    break
  # 如果存在　则跳过本次循环
  if name in list_student_name:
    continue
  list_student_name.append(name)
# 正向
for item in list_student_name:
  print(item)
# 倒序获取列表中元素：通过索引获取元素
for i in range(len(list_student_name)-1,-1,-1):
  print(list_student_name[i])














