# 死锁事例二

# 重复上锁造成死锁
from threading import Thread,RLock
import time

num = 0 # 共享资源
lock = RLock()   # 解决方法,使用重载锁,可以允许重复上锁

class MyThread(Thread):

    def fun01(self):
        global num
        with lock:
            num -= 1

    def fun02(self):
        global num
        if lock.acquire():
            num += 1
            if num >5:   # 当条件num大于５时，本身上锁的情况下
                self.fun01()# 又会调用fun01的with lock上锁，从而造成死锁
            print("Num = ",num)
            lock.release()

    def run(self):
        time.sleep(2)
        self.fun02()

for i in range(10):

    t = MyThread()

    t.start()

    t.join()


















