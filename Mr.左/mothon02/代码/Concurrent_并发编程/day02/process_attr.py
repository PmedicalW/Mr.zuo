# 进程对象属性
from multiprocessing import Process
from time import sleep, ctime


def tm():
    for i in range(3):
        sleep(2)
        print(ctime())
# Sat May 11 09:41:44 2019
# Sat May 11 09:41:47 2019
# Sat May 11 09:41:49 2019


p = Process(target=tm, name='Mr.zuo')

p.daemon = True  # 设置父子进程的退出关系   父进程一退出，所有子进程也会退出

p.start()

print('Name:', p.name)  # 获取名称，可以更改
print('PID:', p.pid)  # 获取PID
print('is Alive:', p.is_alive())  # 查看子进程是否在生命周期

# p.join()
"""
Name: Mr.zuo
PID: 2849
is Alive: True
"""