# 练习：list --> dict
# ["无忌","赵敏","周芷若"]--{"无忌":2,"赵敏":2,"周芷若":3}
# 字典：键－列表的元素　　值－字符串长度
# 11:42

list01 = ["无忌", "赵敏", "周芷若"]
dict02 = {}
for item in list01:
  dict02[item] = len(item)

dict03 = {item: len(item) for item in list01}
print(dict02)
print(dict03)

