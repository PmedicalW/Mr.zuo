from socket import *
import os

# 确认两边使用相同的套接字文件
sock_file = "./sock" # 两个程序之间通过创建的一个sock套接字文件对数据进行收发

sockfd = socket(AF_UNIX, SOCK_STREAM)

sockfd.connect(sock_file)

# 循环发送
while True:
    msg = input(">>")
    if not msg:
        break
    sockfd.send(msg.encode())

sockfd.close()
