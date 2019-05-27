"""
UDP套接字服务端
重点代码
"""
from socket import *

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 消息收发
while True:
    data, addr = sockfd.recvfrom(1024)  # 先接收
    print("收到的客户端消息：", data.decode())  # 打印收到的消息
    data = input("服务器输入：")
    sockfd.sendto(data.encode(), addr)  # 后发送　　　回复消息


# 关闭套接字
sockfd.close()
