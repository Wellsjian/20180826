"""
队列的链式存储
重点代码

思路分析
    1.基于链表完成存储结构
    2.通过封装完成队头和队尾操作
    3.链表开端作为队头，尾端作为队尾
"""
#异常类
class Queue(Exception):
    pass

# 节点类
class Note:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class IQueue:
    def __init__(self):
        self.front = self.rear = Note(None)

    # 判断队列为空
    def is_empty(self):
         return self.front == self.rear

    #队列入队
    def enqueue(self,elem):
        self.rear.next = Note(elem)
        self.rear = self.rear.next
    # 队列出队
    def dequeue(self):
        if self.front == self.rear:
            raise Queue("Queue is empty")
        self.front = self.front.next
        return self.front.data


if __name__ == "__main__":

    iq = IQueue()
    iq.enqueue(10)
    iq.enqueue(20)
    iq.enqueue(30)
    while not iq.is_empty():
        print(iq.dequeue())

    











