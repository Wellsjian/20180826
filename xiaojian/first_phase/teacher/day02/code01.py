"""
  变量
  练习1:画出内存图
  练习2:exercise01.py
"""

# 变量:
# 语法1: 变量名 = 数据
# 语法2: 变量名1 = 变量名2= 数据
# 语法3: 变量名1,变量名2= 数据1,数据2

# 变量名:字母小写,如果有多个单词以下划线分割
#       见名知意

# 内存:10:50 上课
student_name01 = "张无忌"
# 不要使用汉语拼音命名
# xue_sheng_xing_ming = ""
# sn = ""
student_name01 = "张三丰"
student_name02 = "周芷若"
name03 = student_name01 + student_name02

name05 = "玄冥二老"
name04 = name05
# name04 = name05 = "玄冥二老"

# name06 = "赵敏"
# name07 = "灭绝师太"
name06, name07 = "赵敏", "灭绝师太"
print(name06)
print(name07)