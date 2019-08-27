'''
["无忌""赵敏""周芷若"]     {"无忌":2,"赵敏":2,"周芷若":3}
'''

list01 = ["无忌","赵敏","周芷若"]
dict01 = {}

for i in list01:
    dict01[i] = len(i)
print(dict01)


dict02 = {i:len(i) for i in list01}
print(dict02)



'''
练习将人与房间号合并为字典
["无忌","赵敏","周芷若"]
[101,102,103]'''

list02 = ["无忌","赵敏","周芷若"]
list03 = [101,102,103]
dict03 = {}
for i in list02:

    dict03[i] = list03[list02.index(i)]
print(dict03)

dict04 =  {i:list03[list02.index(i)] for i in list02}
print(dict04)