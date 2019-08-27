"""
  字典
  练习:exercise03.py
      exercise04.py
"""
# 1. 创建字典
# 空
dict01 = {}
dict01 = dict()

# 具有默认值
dict01 = {"zc":65,"yl":80,"mz":90}
dict01 = dict([("a","b"),["c","d"]])


# 2. 添加（不存在key）
dict01["qtx"] = 100

# 3. 获取
# 如果查找不存在的key,则异常
if "xx" in dict01:
  print(dict01["xx"])

# 4. 修改（存在key）
dict01["zc"] = 90
print(dict01)

# 5. 删除
if "xx" in dict01:
  del dict01["xx"]
print(dict01)

# print(dict01[:])# un hash able   类型: '切片'

# 6. 遍历
# 得到的是键
# for key in dict01:
#   print(key)
#   print(dict01[key])

# 得到的是键值对的元组
for item in dict01.items():
  print(item[0])
  print(item[1])

for key,value in dict01.items():
  print(key)
  print(value)

# 获取所有值
for value in dict01.values():
  print(value)




