# 进程池实现
from multiprocessing import Pool
from time import sleep


# 进程池事件
def worker(msg):
    sleep(2)
    print(msg)


# 创建进程池
pool = Pool(2)  # 不写数据会按系统默认(4个)分配进程数量

# 向进程池添加事件
for i in range(10):
    msg = 'Hello %d' % i
    pool.apply_async(func=worker, args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()

"""
Hello 0
Hello 1
Hello 3
Hello 2
Hello 4
Hello 5
Hello 6
Hello 7
Hello 8
Hello 9
"""