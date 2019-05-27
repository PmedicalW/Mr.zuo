# client
# 发送图片广播

from socket import *
from time import *

# 广播地址
dest = (('176.140.6.255', 9993))

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

fd = open('/home/tarena/pythonNet_io网络编程/day04/22.jpg', 'rb')  # 打开需要发送的图片

while True:
    data = fd.read(1024)
    s.sendto(data, dest)

s.close()
