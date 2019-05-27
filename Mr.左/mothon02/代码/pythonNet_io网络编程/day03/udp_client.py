"""
UDP套接字客户端
重点代码
"""
from socket import *

# 服务器地址
HOST = '176.140.6.137'  # 定义全局变量，方便后期的修改
PORT = 8888
ADDR = (HOST, PORT)

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 消息收发
while True:
    data = input("Msg>>")  # 客户端发送的消息
    if not data:  # 结束
        break
    sockfd.sendto(data.encode(), ADDR)  # 先发送
    msg, addr = sockfd.recvfrom(1024)   # 后接收
    print("Form server:", msg.decode())

# 关闭套接字
sockfd.close()
