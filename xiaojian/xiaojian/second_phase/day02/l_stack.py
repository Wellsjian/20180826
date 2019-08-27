"""
栈的链式存储


重点代码：
    1.基于的实现模型源于   链表
    2.栈顶位置
"""


# 异常类
class StackError(Exception):
    pass


# 节点类
class Note:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 栈操作类
class Lstack:
    def __init__(self):
        # 定义栈顶位置属性
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        self._top = Note(elem, self._top)
        # self._top = Note(elem)
        # self._top = self._top.next
        #
    def pop(self):
        if self._top is None:
            raise StackError("stamc is empty ")
        value = self._top.data
        self._top = self._top.next
        return value

    def top(self):
        if self._top is None:
            raise StackError("stamc is empty ")
        return self._top.data


if __name__ == "__main__":
    ls = Lstack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    print(ls.top())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())

