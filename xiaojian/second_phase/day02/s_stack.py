"""
栈模型顺序存储
重点代码.


思路分析：
    1.列表即顺序存储。但是接口太多，不符合栈模型
    2.利用列表，封装类，仅提供单一的接口
"""
#自定义异常类
class StackError(Exception):
    pass

# 顺序栈类封装
class SStack:
    def __init__(self):
        # 属性为空列表，表示栈的存储空间
        # 列表最后一个元素为栈顶元素
        self._elements = []

    # 判断栈是否为空
    def is_empty(self):
        return self._elements == []
        # return len(self._elements) == 0

    # 入栈
    def push(self, elem):
        self._elements.append(elem)

    #出栈
    def pop(self):
        if not self._elements:
            raise StackError("stack is empty.")
        #弹出列表最后一个元素
        return self._elements.pop()

    #查看栈顶元素
    def top(self):
        if not self._elements:
            raise StackError("stack is empty.")
        return self._elements[-1]


1#主程序是否匹配的验证工作

if __name__ == "__main__":
    st = SStack()
    print(st.is_empty())
    st.push(10)
    st.push(30)
    st.push(20)
    print(st.top())
    while not st.is_empty():
        print(st.pop())
    # st._elements.append(5)
    # print(st._elements)
