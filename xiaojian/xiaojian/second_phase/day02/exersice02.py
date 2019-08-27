
"""
编写dc程序
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

# from day02.l_stack import Lstack

ls = Lstack()

def add():
    while True:
        elem = input()
        tmp = elem.split(" ")
        for i in tmp:
            if i not in ["+","-","p"]:
                ls.push(float(i))
            elif i == "+":
                ls.push((ls.pop()+ls.pop()))
            elif i == "-":
                y = ls.pop()
                x = ls.pop()
                ls.push((x - y))
            elif i == "p":
                print(ls.top())




print(add())
