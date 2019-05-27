# 基于multiprocessing的多进程网络并发     重点代码
from multiprocessing import Process
from socket import *
import sys
import signal

# 创建监听套接字
HOST = "0.0.0.0"
PORT = 3189
ADDR = (HOST, PORT)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 僵尸进程的处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


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
    p = Process(target=handle, args=(c,))
    p.daemon = True  # 如果用join退出子线程主线程也会退出
    p.start()
