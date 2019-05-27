from socket import *

# 创建套接字
sockfd = socket()

# 请求连接
sockfd.connect(('176.140.6.137',8888))

f = open('img.jpg', 'rb')

# 消息收发
while True:
    data = f.read(1024)
    if not data:  # 结束
        break
    sockfd.send(data)  # 发送消息

f.close()
sockfd.close()
