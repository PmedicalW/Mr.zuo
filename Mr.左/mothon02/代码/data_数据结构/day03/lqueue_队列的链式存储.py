"""
队列的链式存储
"""
# 队列异常
class QueueError(Exception):
    pass

# 创建结点类
class Node(object):
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next

# 完成队列操作
class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    # 判断是否为空
    def is_empty(self):
        return self.front is self.rear

    # 入队
    def enqueue(self, elem):
        self.rear.next = Node(elem)
        self.rear = self.rear.next

    # 出对
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("stack is empty")
        self.front = self.front.next
        return self.front.val

    # 清空
    def clear(self):
        self.front = self.rear


if __name__ == "__main__":
    lq = LQueue()
    print(lq.is_empty())
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty():
        print(lq.dequeue())
