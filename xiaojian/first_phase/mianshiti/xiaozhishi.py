
a = range(10)
print(a)

#
list01 = [1,2]
list02 = [3,4]
# list03 = list01 + list02        #正确
#
list04 = list01.extend(list02)   #错误  ，extend 没有返回值
#

# dict01 = {"a":1,"b":2}
# dict02 = {"c":3,"d":4}
# dict03 = dict01 + dict02  #?错误
# dict04 = dict(**dict01,**dict02)
# print(dict04)
#


#列表中删除内容时，需要倒着删，切记
# def del_mot_pass_student(list_target):
#     count = 0
#     for item in range(len(list_target)-1,-1,-1):
#         if list_target[item].score < 60 :
#             del list_target[item]
#             count += 1
#     return list_target
# del_mot_pass_student(list)

# eval 函数
# str = "3*4+5"
# a = compile("str",":","eval")
# b = eval(a)
# print(b)

# print(eval(str))

# exec函数
a =3
expr = """
str = "3*4+5+a"
print(str)
"""
exec(expr)
print(exec(expr))



















