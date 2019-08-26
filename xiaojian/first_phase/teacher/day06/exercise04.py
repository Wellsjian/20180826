"""
  练习：在控制台中录入多个学生信息(姓名,性别,成绩,年龄),
  如果姓名输入esc,则停止录入．
  逐行打印所有学生信息．
  15:55

  1,2获取学生信息，需要通过索引,代码可读性差.
  {
    "张三":["男",100,25],
    "李四":["男",100,25]
  }
  相比1,4,获取学生更灵活．
  [
    ["张三","男",100,25],
    ["李四","男",100,25],
  ]

  相比１，２内存占用过多
  [
    {"name":"张三","sex":"男","score":100,"age":25},
    {"name":"李四","sex":"男","score":100,"age":25},
  ]

  相比2,3查找人的速度快
  {
    "张三" :{"sex":"男","score":100,"age":25},
    "李四":{"sex":"男","score":100,"age":25},
  }

  序列：有序  灵活(索引／切片)
  散列：无序  速度快　　可读性更高
"""

# 选择第一种数据结构
# {
#   "张三": ["男", 100, 25],
#   "李四": ["男", 100, 25]
# }

dict_student_info = {}
while True:
  name = input("请输入姓名：")
  if name == "esc":
    break
  sex = input("请输入性别：")
  score = int(input("请输入成绩："))
  age = int(input("请输入年龄："))
  dict_student_info[name] = [sex, score, age]

# 打印信息
for key, value in dict_student_info.items():
  print("%s的性别是%s，成绩是%d,年龄是%d." % (key, value[0], value[1], value[2]))












