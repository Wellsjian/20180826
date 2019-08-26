"""
  集合set
  作用：不重复　　数学运算
  练习：exercise03.py
"""

# 创建集合
# 空
s01 = set()
# 具有默认值
s01 = {"a", "b"}
s01 = set("abadeag")

# 添加
s01.add("A")

# 删除
print(s01)
s01.remove("b")
print(s01)

# 定位元素
# set --> list
list01 = list(s01)
print(list01[:3])

# 数学运算
s02 = {1, 2, 3}
s03 = {2, 3, 4}

# 交集
print(s02 & s03)  # {2, 3}

# 并集
print(s02 | s03)  # {1, 2, 3, 4}

# 补集
print(s02 ^ s03)  # {1, 4}

print(s02 - s03)  # {1}

print(s03 - s02)  # {4}

# 子集　　超集
s04 = {1, 2}

# 子集　完全包含
print(s04 < s02)

# 超集
print(s02 > s04)
