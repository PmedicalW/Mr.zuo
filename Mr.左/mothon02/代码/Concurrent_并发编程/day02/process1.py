# multiprocess事例
# 可以方便的创建多个子进程
import multiprocessing as mp
from time import sleep

a = 1  # 全局变量


def fun():
    print("子进程开始执行")
    global a
    a = 10000
    print("a =", a)
    # sleep(3)
    print("子进程执行完毕")


# 创建进程对象
p = mp.Process(target=fun)

# 启动进程
p.start()  # 执行子进程

sleep(2)  # 执行父进程
print("父进程执行ing")

# 回收进程
p.join()

print("parent a", a)

"""
子进程开始执行
a = 10000
子进程执行完毕
父进程执行ing
parent a 1
"""
