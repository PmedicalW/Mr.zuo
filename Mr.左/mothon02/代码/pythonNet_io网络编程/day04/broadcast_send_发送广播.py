# 发送广播
from socket import *
from time import *

# 广播地址
dest = (('176.140.6.255', 3189))

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

data = """ 
    ***************
    　　共产党万岁
    ***************

"""
while True:
    sleep(2)  # ２s发送一次
    s.sendto(data.encode(), dest)

s.close()
