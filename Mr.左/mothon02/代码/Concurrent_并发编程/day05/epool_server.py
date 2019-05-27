"""
epoll多路复用
次重点
"""

from socket import *
from select import *

# 　设置套接字为关注ＩＯ
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 9999))
s.listen(5)

# 　创建eｐｏｌｌ
ep = epoll()

# 　建立查找字典 {fileno: io_obj}
fdmap = {s.fileno(): s}

# 　设置关注ＩＯ
ep.register(s, EPOLLIN | EPOLLERR)

print('Waiting connect...')

# 　循环监控ｉｏ事件发生
while True:
    events = ep.poll()  # 阻塞等待ＩＯ发生
    print(events)
    # 遍历列表处理ＩＯ　
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 　添加新的关注事件
            ep.register(c, EPOLLIN | EPOLLHUP | EPOLLET)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:  # 客户端发消息
            data = fdmap[fd].recv(1024)
            # 断开发生时data得到空此时EPOLLIN也会就绪
            if not data:
                ep.unregister(fd)  # 取消关注
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data.decode())
            fdmap[fd].send(b'OK')
