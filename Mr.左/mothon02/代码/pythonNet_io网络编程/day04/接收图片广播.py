# sercer
# 接收图片广播

from socket import *

s = socket(AF_INET, SOCK_DGRAM)

# 　让套接字可以接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

s.bind(('0.0.0.0', 9993))

fd = open('/home/tarena/pythonNet_io网络编程/day04/recv.jpg', 'wb')

while True:
    msg, addr = s.recvfrom(1024)

    data = fd.write(msg)  # 写入图片

s.close()
