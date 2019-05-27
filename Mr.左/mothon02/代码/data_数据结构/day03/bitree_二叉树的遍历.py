"""
二叉树的遍历
"""
from squeue_队列的顺序存储 import *

# 二叉树的结点类
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data  # 结点
        self.left = left  # 左子树
        self.right = right  # 右子树

# 二叉树类
class Bitree:
    def __init__(self, root=None):
        self.root = root  # 获取起始的根

    # 判断是否为空
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    # 先序遍历　
    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    # 中序遍历
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)

    # 后序遍历
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=' ')

    # 层次遍历
    def levelorder(self, node):
        qu = SQueue()
        qu.enqueue(node)  # 先将根结点入队
        while not qu.is_empty():
            node = qu.dequeue()  # 出对时打印
            print(node.data, end=' ')
            if node.left:
                qu.enqueue(node.left)
            if node.right:
                qu.enqueue(node.right)


if __name__ == "__main__":
    # 按照后序遍历增加结点(代码更清晰简洁)
    b = TreeNode('B')
    f = TreeNode('F')
    g = TreeNode('G')
    d = TreeNode('D', f, g)
    i = TreeNode('I')
    h = TreeNode('H')
    e = TreeNode('E', i, h)
    c = TreeNode('C', d, e)
    a = TreeNode('A', b, c)  # 根节点

    bt = Bitree(a)  # 初始化树对象，传入根节点

    print("先序遍历:")
    bt.preorder(bt.root)

    print()
    print("中序遍历:")
    bt.inorder(bt.root)

    print()
    print("后序遍历:")
    bt.postorder(bt.root)

    print()
    print("层次遍历:")
    bt.levelorder(bt.root)
