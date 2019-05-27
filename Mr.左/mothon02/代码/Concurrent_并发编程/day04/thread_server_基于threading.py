# 基于threading的多线程网络并发     重点代码
from threading import Thread
from socket import *
import sys

# 创建监听套接字
HOST = "0.0.0.0"
PORT = 3189
ADDR = (HOST, PORT)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)


# 客户端处理函数
def handle(c):
    print("Connect from", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    # 创建新的线程处理客户端请求
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)  # 如果用join退出子线程主线程也会退出
    t.start()
