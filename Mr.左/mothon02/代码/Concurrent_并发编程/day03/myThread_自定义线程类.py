from threading import Thread

class ThreadClass(Thread):
    def __init__(self, attr):
        self.attr = attr
        super().__init__()

    # 多个方法配合实现具体功能
    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()

t = ThreadClass("xxx")
t.start()  # 自动运行run方法
t.join()

"""
步骤1
步骤2
"""