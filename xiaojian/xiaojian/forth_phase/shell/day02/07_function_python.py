#!/usr/bin/env python3

def add_info():
    print('我是添加')
def mod_info():
    print('我是修改')
def sel_info():
    print('我是查看')

def del_info():
    print('我是删除')

choice = """
1)查询
2)增加
3)修改
4)删除
请选择(1|2|3|4):
"""
choice = input(choice).strip()

if choice in ('1','2','3','4'):
    
    dict01 = {
            "1":sel_info,
            "2":add_info,
            "3":mod_info,
            "4":del_info}
    dict01[choice]()
else:
    print("输入无效")


