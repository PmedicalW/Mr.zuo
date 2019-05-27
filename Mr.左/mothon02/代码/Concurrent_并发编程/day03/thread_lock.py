from threading import Thread, Lock

a = b = 0

lock = Lock()  # 创建锁对象

def value():
    while True:
        lock.acquire()# 上锁
        if a != b:
            print("a= %d,b = %d" % (a, b))
        lock.release()# 解锁

t = Thread(target=value)

t.start()

while True:
    with lock:   # with代码块结束自动解锁
        a += 1
        b += 1

t.join()
