# 管道通信(Pipe)
from multiprocessing import Process, Pipe
import os, time

# 创建管道
fd1, fd2 = Pipe(False)


def fun(name):
    time.sleep(3)
    # 向管道写入内容
    fd2.send({name: os.getpid()})


jobs = []
for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

# 父进程读取
for i in range(5):
    # 读取管道
    data = fd1.recv()
    print(data)

for i in jobs:
    i.join()
"""
{1: 4298}
{0: 4297}
{2: 4299}
{3: 4300}
{4: 4301}
"""