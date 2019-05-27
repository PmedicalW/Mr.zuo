"""
编写程序完成效率测试
        使用单线程执行计算密集型函数10次，记录时间，执行io密集型函数10次，记录时间
        使用10个线程分别执行计算密集型函数１次，记录时间，执行io密集型函数１次，记录时间
        使用10个进程执行计算密集型函数１次，记录时间，执行io密集型函数１次，记录时间
"""
#　计算密集型函数 x y 传入１，１
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1

#　io密集型
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1500000):
        f.write("hello world\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()
