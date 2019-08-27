"""
练习：创建调查问卷:多个人的多个喜好.
"请输入姓名：(esc结束)"
"请输入您的喜好:(esc结束)"
调查结束后，逐行显示所有信息．

{
  妹子:[吃,学习],
  qtx:[工作,学习,运动],
}
"""
#17:20
dict_person_hobby = {}
while True:
  name = input("请输入姓名：(esc结束)")
  if name == "esc":
    break
  hobbys = []
  dict_person_hobby[name] = hobbys
  while True:
    hobby = input("请输入您的喜好:(esc结束)")
    if hobby == "esc":
      break
    # 向列表添加元素的同时向字典添加元素
    hobbys.append(hobby)
    # dict_person_hobby[name] = hobbys
for key,value in dict_person_hobby.items():
  print("%s的喜好是：%s."%(key,value))