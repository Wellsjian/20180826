"""
  作用域
    -- 局部
    -- 全局
  练习:exercise06.py
"""

g01 = 500

def fun01():
  g01 = 600# 没有修改全局变量g01，而是创建了局部变量g01
  print(g01)#600
  # 局部作用域
  l01 = 100

def fun02():
  print(g01)
  # 局部作用域
  l01 = 200

def fun03():
  # 通过global语句，定义g01为全局变量
  global g01
  g01 = 300# 修改的是全局变量


fun03()
fun01()
fun02()


