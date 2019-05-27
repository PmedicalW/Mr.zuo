"""
套接字非阻塞示例
"""
from socket import *
from time import sleep, ctime

# 日志文件
f = open('log.txt', 'a+')

# ｔｃｐ套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 超时检测
sockfd.settimeout(3)

while True:
    print('Waiting for connect...')
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        # 每隔２ｓ写入一条日志
        sleep(2)
        f.write('%s: %s\n' % (ctime(), e))
        f.flush()
    else:
        data = connfd.recv(1024).decode()
        print(data)
# Waiting for connect...
# Waiting for connect...
# Waiting for connect...
# Waiting for connect ...
# Waiting for connect...
# Waiting for connect...
"""
log.txt日志内容:
Wed May 15 18:59:55 2019: timed out
Wed May 15 19:00:00 2019: timed out
Wed May 15 19:00:05 2019: timed out
Wed May 15 19:00:10 2019: timed out
Wed May 15 19:00:15 2019: timed out
Wed May 15 19:00:20 2019: timed out
"""