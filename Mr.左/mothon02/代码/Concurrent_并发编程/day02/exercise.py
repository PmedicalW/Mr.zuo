# 1. multiprocess创建两个进程，
# 同时复制一个文件的上下两半部分，
# 各自复制到一个新的文件里
from multiprocessing import Process
from time import sleep
import os

len_size = os.path.getsize('test')
size = len_size // 2


# 创建两个进程
def fun01():
    file01 = open('test', 'rb')
    file01.seek(0, 0)
    data01 = file01.read(size)
    # 写入
    w01 = open('up_file', 'wb')
    w01.write(data01)
    w01.close()
    file01.close()
    return


def fun02():
    file02 = open('test', 'rb')
    file02.seek(size, 0)
    data02 = file02.read(len_size - size)
    w02 = open('down_file', 'wb')
    w02.write(data02)
    w02.close()
    file02.close()
    return


things = [fun01, fun02, ]
jobs = []
for fun in things:
    p = Process(target=fun)
    jobs.append(p)
    p.start()

# 防止僵尸进程产生
for i in jobs:
    i.join()
