"""
队列的顺序存储
重点代码

思路分析
    1.基于列表完成存储结构
    2.通过封装完成队头和队尾操作
"""

#异常类
class QueueError(Exception):
    pass

#队列操作类
class SQueue:

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def enquene(self,elem):
        self._elems.append(elem)

    def dequene(self):
        if not self._elems:
            raise QueueError("queue is error")
        return self._elems.pop(0)




if __name__ == "__main__":
    sq = SQueue()
    sq.enquene(10)
    sq.enquene(20)
    sq.enquene(30)
    while not sq.is_empty():
        print(sq.dequene())





