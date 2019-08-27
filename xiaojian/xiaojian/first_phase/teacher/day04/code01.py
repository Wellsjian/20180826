"""
  for : 相比while更适合做预定次数的循环.
  while :相比for更适合根据条件执行的循环.
  练习:exercise01.py
      exercise02.py
"""

# for 变量 in 可迭代对象:
#   语句

for item in "我爱python":
  print(item)


# while 循环对折5次
thickness = 0.00001
count = 0
while count<5:
  thickness *= 2
  count+=1
print(thickness)

thickness = 0.00001
# for 循环对折5次
for count in range(5):
  thickness *= 2
print(thickness)




