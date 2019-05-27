"""
gevent协程演示
"""
import gevent
from gevent import monkey

monkey.patch_all()
from socket import *


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 创建套接字
s = socket()
s.bind(('0.0.0.0', 3189))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Connect from', addr)
    # handle(c) # 循环方案
    gevent.spawn(handle, c)  # 协程方案

s.close()


"""
浏览器输入：IP:PORT
Connect from ('176.140.6.137', 45294)
GET / HTTP/1.1
Host: 176.140.6.137:3189
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
"""