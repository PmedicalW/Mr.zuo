"""
1. 使用tcp服务和客户端编程，
将一个文件从客户端发送到服务端，
文件类型为图片或者普通文本皆可。
思路：客户端读取，服务端写入
"""
import socket

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8888))  # 此地址可以被其他主机访问

# 设置监听
sockfd.listen(5)

# 等待处理客户端连接请求

connfd, addr = sockfd.accept()
print("Connect from:", addr)

f = open('w_img.jpg', 'wb')

# 接收内容，写入文件
while True:
    data = connfd.recv(1024)  # 接受客户端
    if not data:
        break
    f.write(data)

# 关闭套接字
f.close()
connfd.close()
sockfd.close()
