"""
io多路复用select实现多个客户端通信
重点代码
"""
from socket import *
from select import select

# 设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 9999))
s.listen(3)

# 设置关注io
rlist = [s]
wlist = []
xlist = []

while True:
    # 监控io的发生
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历三个返回值列表，判断哪个io发生
    for r in rs:
        # 如果套接字就绪则处理连接
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)  # 循环加入新的关注io
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b'OK')
            wlist.append(r)  # 主动处理这个ｉｏ

    for w in ws:
        w.send(b'OK,Thanks')
        wlist.remove(w)

    for x in xs:
        pass
