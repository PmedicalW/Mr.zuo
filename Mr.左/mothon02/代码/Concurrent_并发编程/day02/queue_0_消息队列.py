# 消息队列通信
from multiprocessing import Queue, Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(3)


def request():
    for i in range(20):
        x = randint(0, 100)
        y = randint(0, 100)
        q.put((x, y)) # 存入


def handle():
    while True:
        sleep(0.5)
        try:
            x, y = q.get(timeout=3) # 取出
        except:
            break
        else:
            print("%d + %d = %d" % (x, y, x + y))


p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()

"""
97 + 4 = 101
40 + 50 = 90
8 + 71 = 79
92 + 42 = 134
70 + 58 = 128
81 + 6 = 87
66 + 33 = 99
78 + 33 = 111
2 + 96 = 98
......

"""