"""
  选择语句
  练习:exercise01.py
      exercise02.py
      exercise03.py
      exercise04.py
      exercise05.py
"""

sex = input("请输入性别:")
# 1 tab --> 4空格(缩进)

if sex == "男":
  print("您好,先生.")
elif sex == "女":
  print("您好,女士.")
else:
  print("性别未知")
#调试:让程序中断,逐语句执行,审查程序执行过程(流程,变量取值).
# 步骤:
# 1. 加入断点(程序中断的行)
# 2. 调试运行
# 3. 逐过程执行(F8)
# 4. 停止调试(Ctrl + F2)
