"""
  字典推导式
  练习：exercise01.py
       exercise02.py
"""

# 1 2 3 4 ... 10  -->  数:平方

dict01 = {}
for item in range(1, 10):
  dict01[item] = item ** 2

print(dict01)

dict02 = {item: item ** 2 for item in range(1, 10)}
print(dict02)
