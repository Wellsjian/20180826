def sort(list_target):
    for i in range(len(list_target)):  # 循环n次
        for j in range(i + 1, len(list_target)):  # 循环 (1+1+n)*n/2
            if list_target[i] > list_target[j]:
                list_target[i], list_target[j] = list_target[j], list_target[i]
    return list_target


list = [1, 82, 478, 23, 48, 93]
print(sort(list))


def sort1(list_target):
    max = list_target[0]
    i = 1
    while i < len(list_target) - 1:
        if max > list_target[i]:
            max, list_target[i] = list_target[i], max
            max = list_target[i]
        i += 1


list = [1, 82, 478, 23, 48, 93]
print(sort(list))


# 冒泡排序
def bubble(list_target):
    # 外层循环计算比较的轮数
    for i in range(len(list_target) - 1):
        # 内层循环把控计较次数
        for j in range(len(list_target) - 1 - i):
            if list_target[j] > list_target[j + 1]:
                list_target[j], list_target[j + 1] = list_target[j + 1], list_target[j]


list = [1, 82, 478, 23, 48, 93]
bubble(list)
print(list)
print(list)


# 选择排序
def select(list_target):
    # 外层循环计算比较的轮数
    for i in range(len(list_target) - 1):
        min = i  # 假设list[i]为最小值
        # 内层循环把控计较次数
        for j in range(i + 1, len(list_target)):
            if list_target[min] > list_target[j]:
                min = j
        # 如果i不是最小值就交换
        if min != i:
            list_target[min], list_target[i] = list_target[i], list_target[min]


list = [1, 82, 478, 23, 48, 93]
select(list)
print(list)


# 插入排序
def insert(list_target):
    for i in range(1, len(list_target)):
        x = list_target[i]
        j = i - 1
        while j >= 0 and list_target[j] > x:
            list_target[j + 1] = list_target[j]
            j -= 1
        list_target[j + 1] = x


# 完成一轮排序过程
def sub_sort(list_target, low, high):
    # 基准数
    x = list_target[low]
    while low < high:

        while list_target[high] >= x and high > low:
            high -= 1
        list_target[low] = list_target[high]

        while list_target[low] < x and low < high:
            low += 1
        list_target[high] = list_target[low]
    #将基准数插入
    list_target[low]  = x
    return  low

# 快速排序
# low表示第一个序列号，high是最后一个序列号
def quick(list_target, low, high):
    if low < high:
        key = sub_sort(list_target, low, high)
        quick(list_target, low, key - 1)
        quick(list_target, key + 1, high)


# list = [1, 82, 478, 23, 48, 93, 65, 97, 14212, 7874, 21, 5]


def insert1(list_target):
    min = list_target[len(list_target) - 1]
    for i in range(len(list_target) - 2, -1, -1):
        if min < list_target[i]:
            list_target[i] = min


list = [1, 82, 478, 23, 48, 93, 65, 97, 14212, 7874, 21, 5]
quick(list,0,len(list)-1)
print(list)
