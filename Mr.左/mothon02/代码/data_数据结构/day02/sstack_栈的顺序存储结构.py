"""
栈的顺序存储结构
重点代码
"""
# 自定义异常
class StackError(Exception):
    pass

# 基于列表实现顺序栈
class SStack:
    def __init__(self):
        # 约定最后一个为栈顶元素
        self._elems = []

    def top(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems[-1]

    # 判断栈是否为空
    def is_empty(self):
        return self._elems == []   # 空为True,反之False

    # 入栈
    def push(self,elem):
        self._elems.append(elem)

    # 出栈
    def pop(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop()

if __name__ == "__main__":
    st = SStack()  # 初始化栈
    #print(st.top())
    print(st.is_empty()) # True
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())  # 30
                         # 20
                         # 10

