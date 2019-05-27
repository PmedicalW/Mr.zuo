# 线程属性
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t=Thread(target=fun,name='Mr.zuo')

# 主线程退出分支线程也退出
t.setDaemon(True)

t.start()

# 线程名称
t.setName('tarena')# 设置线程名称(也可以在参数传入修改)
print('Thread name:',t.getName())# 获取线程名称

# 线程生命周期
print("is alive:",t.is_alive())

#Thread name: tarena
#is alive: True    没有t.start(),所以周期为True









