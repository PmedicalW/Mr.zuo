# 练习
from threading import Thread
from time import sleep,ctime
class MyThread(Thread):
     def __init__(self,target=None,args=(),kwargs={},name="tarena"):
         super().__init__()
         self.target=target
         self.args=args
         self.kwargs=kwargs
         self.name=name


     def run(self):
         self.target(*self.args,**self.kwargs)

#--------------------------------
#通过完成上面的MyThread类让整个程序可以正常执行
#当调用start和player作为一个线程功能函数运行
#注意,函数名称和参数并不确定,player只是测试函数

def player(sec,song):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target=player,args=(3,),kwargs={'song':'凉凉'},name='happy')

t.start()
t.join()

#Playing 凉凉:Mon May 13 19:41:31 2019
#Playing 凉凉:Mon May 13 19:41:34 2019




