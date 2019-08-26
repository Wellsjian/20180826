"""
二叉树的实现

思路分析：
    1.使用链式存储
        节点类设计出两个属性，包括左孩子和右孩子
"""
from day02.s_queue import SQueue
#节点类
class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 二叉树操作类
class Bitree:
    """
    完成二叉树的遍历
    """
    def __init__(self, root=None):
        self.root = root
        self.list = []

    # 先序遍历
    def pre_order(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)


    #中序遍历
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data, end=" ")
        self.in_order(node.right)



    # 后序遍历
    def be_order(self, node):
        if node is None:
            return
        self.be_order(node.left)
        self.be_order(node.right)
        print(node.data, end=" ")

    # 层次遍历
    # def level_order(self,node):
    #     self.list.append(node)
    #     while  not self.list == []:
    #         code = self.list.pop(0)
    #         print(code.data, end=" ")
    #         if code.left:
    #             self.list.append(code.left)
    #         if code.right:
    #             self.list.append(code.right)

    # 层次遍历
    def level_order(self,node):
        st = SQueue()
        st.enquene(node)
        while not st.is_empty():
            code = st.dequene()
            print(code.data, end=" ")
            if code.left:
                st.enquene(code.left)
            if code.right:
                st.enquene(code.right)


if __name__ == "__main__":
    # 后续遍历 B F G D I H E C A
    b = TreeNode("B")
    f = TreeNode("F")
    g = TreeNode("G")
    d = TreeNode("D",f,g)
    i = TreeNode("I")
    h = TreeNode("H")
    e = TreeNode("E",i,h)
    c = TreeNode("C",d,e)
    a = TreeNode("A",b,c)
    #初始化对象得到树根
    bt = Bitree(a)
    # bt.pre_order(bt.root)
    # print()
    # bt.in_order(bt.root)
    # print()
    # bt.be_order(bt.root)
    # print()
    bt.level_order(bt.root)
    print()
















