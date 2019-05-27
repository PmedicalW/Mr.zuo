"""
线程事例一
"""
import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    global a
    print("a=", a)
    a = 10000
    for i in range(5):
        sleep(2)
        print(os.getpid(), "播放：爱的供养")  # pid一样,说明都同属同一个线程

# 创建线程对象
t = threading.Thread(target=music)
t.start()

# 主线程任务
for i in range(3):
    sleep(3)
    print(os.getpid(), "播放：学猫叫")

t.join()

print("Main thread a:", a)
