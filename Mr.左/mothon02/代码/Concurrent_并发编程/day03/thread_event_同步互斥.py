from threading import Thread, Event
from time import sleep

s = None  # 全局变量
e = Event()  # 创建Event对象

def 座山雕():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 共享资源操作完毕　　阻塞等待e被set

t = Thread(target=座山雕)
t.start()
print("口令")

e.wait(3)  # 阻塞等待
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("来了老弟")
else:
    print("弄死他")
t.join()
