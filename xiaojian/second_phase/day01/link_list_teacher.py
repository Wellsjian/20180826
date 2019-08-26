"""
重点代码    链表程序实现

思路分析

1.创建节点类，生成节点对象，包含数据和下一个节点的引用
2.创建链表类，生成链表对象，包含可以对链表进行数据操作
"""


# 节点类

class Note:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 链表类
class LinkList:
    """
    建立链表模型
    进行链表操作
    """

    def __init__(self):
        """
        初始化链表，生成一个头节点，表示链表开始节点
        """
        self.head = Note(None)

    # 初始添加一组链表节点
    # def init_list(self, list_):
    #     """
    #     添加一组链表节点
    #     :param list_:
    #     :return:
    #     """
    #     p = self.head
    #     for i in list_:
    #         p.next = Note(i)
    #         p = p.next
    #
    # # 打印链表
    def show(self):
        """
        打印链表
        :return:
        """
        p = self.head.next
        while p is not None:
            print(p.data, end=" ")
            p = p.next
        print()

    # 获取链表长度
    def get_length(self):
        """
        判断链表的长度
        :return:
        """
        count = 0
        p = self.head
        while p.next is not None:
            count += 1
            p = p.next
        return count

    # 判断链表是否为空
    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        if self.get_length() == 0:
            return True
        return False

    # 清空链表
    def clear(self):
        """
        清空列表
        :return:
        """
        self.head.next = None

    # 尾部插入链表
    def append(self, data):

        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Note(data)

    # 选择位置插入节点
    def insert(self, index, data):
        if index < 0:
            index = 0
        elif index > self.get_length():
            index = self.get_length()
        p = self.head
        for i in range(index):
            p = p.next
        node = Note(data)
        node.next = p.next
        p.next = node

    # 删除节点
    def delete(self, data):
        p = self.head

        while p.next and p.next.data != data:
            p = p.next
        if p.next is None:
            raise ValueError("Value is error")
        else:
            p.next = p.next.next

    # 获取节点值
    def get_item(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("index out of range")
        p = self.head.next
        for i in range(index):
            p = p.next
        return p.data

        # 链表对象


# link ---->>  head
# link.head ---->>  date == None
# link.head ---->>  next == None
link = LinkList()
# node = Note()
# link.head.next = node

# list = [1, 2, 3, 4, 5]
# link.init_list(list)
# link.show()
# print(link.get_length())
link.append(6)
link.show()
link.insert(3, 8)
link.show()
# l