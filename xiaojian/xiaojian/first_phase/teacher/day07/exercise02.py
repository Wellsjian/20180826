# 练习:list + list --> dict
# ["无忌","赵敏","周芷若"]
# [101,102,103]
# 练习:将人与房间号合并为字典

list01 = ["无忌", "赵敏", "周芷若"]
list02 = [101, 101, 102]

dict01 = {}
for i in range(len(list01)):
  dict01[list01[i]] = list02[i]

dict02 = {list01[i]: list02[i] for i in range(len(list01))}

print(dict01)
print(dict02)

# 需求：根据值找键
# 解决：交换键值　：　　键 -> 值     值 -> 键
dict03 = { value:key for key,value in dict02.items()}
print(dict03)
# 缺点：容易丢失数据（值如果相同，反过来作为键，会丢失）
# [(键,值),(键,值)]

list04 = [(key,value) for key,value in dict02.items()]

print(list04)