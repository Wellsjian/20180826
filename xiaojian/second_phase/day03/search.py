"""
search.py  基本查找方法训练(红黑树).

    二分法查找元素
"""


def search(list_targrt, key):

    low , high = 0 , len(list_targrt) - 1

    while low <= high:
        middle = (low + high) // 2
        if list_targrt[middle] < key:
            low = middle + 1
        elif list_targrt[middle] > key:
            high = middle - 1
        else:
            return middle


list = [1, 5, 21, 23, 48, 65, 82, 93, 97, 478, 7874, 14212]
print(search(list,65))