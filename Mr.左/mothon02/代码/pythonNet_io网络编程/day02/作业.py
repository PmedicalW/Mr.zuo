"""
1.  编写一个程序完成如下。
    1. 每隔1秒向文件test.txt中写入一行数据，格式如下
        1.  2019-7-30  12:12:12
        2.  2019-7-30  12:12:13
        3.  2019-7-30  12:12:19
            .....
    2. 该程序无限循环，ctrl-c退出
    3. 当重启程序时，内容会继续向下写，序号能够接上之前的
"""
import time
f = open('time.txt', 'a+')
f.seek(0)  # 文件偏移量移动到开头
n = 1
for line in f:
    n += 1
while True:
    time.sleep(1)
    s = "%d.  %s\n" % (n, time.ctime())
    f.write(s)
    f.flush()
    n += 1