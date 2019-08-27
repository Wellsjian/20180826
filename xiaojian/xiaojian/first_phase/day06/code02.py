"""
字典
"""

# 1.创建字典
dict01 = {"王":4,"富":12,"建":8}
print(dict01)
dict02 = dict([[0,1],[2,3]])
print(dict02)

# 2.添加字典

dict01["wfj"] = 99
print(dict01)

# 3.获取字典
if "王" in dict01:
    print(dict01["王"])

#4.删除字典
del dict01["wfj"]
print(dict01)

dict03 =dict([[1,2]])
print(dict03)

#5.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值

print(dict01.get("富"))

# setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default,返回值为none
print(dict01.setdefault("园"))
print(dict01)











