"""
TCP套接字客户端
重点代码
"""
from socket import *

# 创建套接字
sockfd = socket()

# 请求连接
server_addr = ('176.140.6.137', 3189)  # 访问本机主机IP地址　端口
sockfd.connect(server_addr)

# 消息收发
while True:
    data = input("消息：")
    if not data:  # 结束
        break
    sockfd.send(data.encode())  # 发送消息
    data = sockfd.recv(1024)  # 接收消息
    print("Form server:", data.decode())

# 关闭套接字
sockfd.close()
