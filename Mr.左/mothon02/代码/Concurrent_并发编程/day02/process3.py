from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec) # 每过２ｓ执行一次
        print("I'm %s" % name)
        print("I'm working...")


# p = Process(target=worker,args=(2,'Baron')) # 给target函数位置传参(元组)
# p = Process(target=worker,kwargs={'name':"Abby",'sec':2}) # 给target函数键值传参(字典)
p = Process(target=worker, args=(2,), kwargs={'name': "Abby"})  # 两个一起使用（元组＋字典）

p.start()
p.join()

"""
I'm Abby
I'm working...
I'm Abby
I'm working...
I'm Abby
I'm working...
"""