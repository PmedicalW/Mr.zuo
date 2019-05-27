"""
单链表学习程序（重点程序）
链式线性思路：
        １．结点如何表示
            自定义对象：对象即属性，对象属性即数据元素
            数据元素：包含有用数据和记录下一个对象地址的数据
        ２．如何建立关联
        ３．实现生么样的链表操作
            链表的初始化
            链表的遍历

作业：１．实现在链表的尾部插入一个新的结点
     ２．顺序存储和链式存储的差别
     ３．线性结构特点
"""


# 创建结点类
class Node(object):
    def __init__(self, val, next=None):
        self.val = val # 有用数据
        self.next = next

# 链表的操作
class Linklist(object):
    def __init__(self):
        self.head = Node(None)  # 链表开头(让它永远不变)－－－－＞初始化

    def init_list(self, list):
        p = self.head  # 可移动变量(让p作为第一个（head）)
        for i in list:
            p.next = Node(i)  # p 指向下一个对象（列表数据）
            p = p.next

    # 尾部插入新的结点
    def append(self, item):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(item)

    # 获取链表长度
    def get_length(self):
        n = 0
        p = self.head
        while p.next is not None:
            n += 1
            p = p.next
        return n

    # 判断链表是否为空
    def is_empty(self):
        if self.get_length() == 0:
            return True
        return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 获取索引值
    def get_item(self, index):
        p = self.head.next
        i = 0
        # 没有到对应索引号并且遍历索引没有到最后就循环
        while i < index and p is not None:
            i += 1
            p = p.next
        # 如果因为ｐ到最后了则说明越界
        if p is None:
            raise IndexError("list index out of range")  # 越界报错
        # ｉ 不小于　ｉｎｄｅｘ说明找到索引结点了
        else:
            return p.val

    # 指定位置插入
    def insert(self, index, item):
        if index < 0 or index > self.get_length():
            raise IndexError("list index out of range")
        # 让ｐ移动到待插入位置的前一个
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1
        node = Node(item)  # 创建新的结点
        node.next = p.next  # 插入结点
        p.next = node

    # 删除
    def remove(self, item):
        p = self.head
        while p.next is not None:
            # 　如果值相等则越过中间的结点
            if p.next.val == item:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("x not in list")

    def show(self):
        p = self.head.next
        while p != None:
            print(p.val, end=" ")
            p = p.next
        print()
#---------------测试-----------------
if __name__ == "__main__":
    # 创建链表对象
    link = Linklist()
    # 创建初始数据
    list = [1, 2, 3, 4, 5, 6]
    link.init_list(list)  # 初始数据插入链表
    link.show()  # 遍历链表  # 1  2  3  4  5  6
    link.append(8)  # 尾加
    link.show()  # 1  2  3  4  5  6  8
    count = link.get_length()
    print("链表长度:",count)  # 链表长度:7
    # link.clear()
    print("是否空值：",link.is_empty())  # 是否空值： False
    print("索引:",link.get_item(3)) # 索引
    link.show() # 1 2 3 4 5 6 8
    link.insert(1,15)
    link.show()# 1 15 2 3 4 5 6 8
    link.remove(5)
    link.show()# 1 15 2 3 4 6 8