"""
重点代码    链表程序实现

思路分析

1.创建节点类，生成节点对象，包含数据和下一个节点的引用
2.创建链表类，生成链表对象，包含可以对链表进行数据操作
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linklist:
    def __init__(self):
        # 头结点
        self.head = Node(None)

    # 尾部插入
    def append(self, data):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(data)

    # 打印
    def show(self):
        p = self.head.next
        while p is not None:
            print(p.data, end="  ")
            p = p.next
        print()
    # 获取列表长度
    def get_lenth(self):
        p = self.head
        n = 0
        while p.next is not None:
            n += 1
            p = p.next
        return  n
    # 中间插入
    def insert(self, index, data):
        if index < 0 or index > self.get_lenth():
            raise IndexError()
        p = self.head
        for i in range(index):
            p = p.next
        code = Node(data)
        code.next = p.next
        p.next = code
        #不能省略code,否则链表会丢失


li = Linklist()
li.append(1)
li.show()
li.append(2)
li.show()
li.append(3)
li.show()
li.insert(0, 5)
li.show()
print(li.get_lenth())

# print(li.show())
