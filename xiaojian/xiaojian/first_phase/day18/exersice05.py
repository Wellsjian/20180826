"""
练习：
    1.使用生成器函数，获取列表中所有偶数
      [34,4,54,5,7,8]
    2.自定义生成器函数my_enumrate

    3.自定义生成函数my_zip
    list01 = ["张无忌","赵敏","周芷若"]
      list02 = [101,102,103]
"""

def get_even(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item

# for item in enumerate(get_even( [34,4,54,5,7,8])):
#     print(item)

# def my_enumrate(list_target):
#     for i in range(len(list_target)):
#         yield (i,list_target[i])
# result = my_enumrate([34,4,54,5,7,8])
# for item in result:
#     print(item)

def my_zip(list01,list02):
    for i in range(min(len(list01),len(list02))):
        yield (list01[i],list02[i])

list01 = ["张无忌","赵敏","周芷若","小昭"]
list02 = [101,102,103]
for i in my_zip(list01,list02):
    print(i)