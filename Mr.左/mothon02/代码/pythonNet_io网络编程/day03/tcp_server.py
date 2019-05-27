"""
TCP套接字服务端
重点代码
"""
import socket

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 两个参数都是默认值，可以不写

# 绑定地址
sockfd.bind(('0.0.0.0', 8888))   # 此地址可以被其他主机访问

# 设置监听
sockfd.listen(5)

# 等待处理客户端连接请求
while True:  # 可以按顺序的连接多个客户端，注意：并不是同时连接
    print("Waiting for connect......") # 提示：正在等待连接
    try:
        connfd, addr = sockfd.accept()
        print("Connect from:", addr)   # 打印连接的客户端地址
    except KeyboardInterrupt:  # 捕捉键盘的ctrl+c的异常
        print("退出服务")
        break

    # 消息收发
    while True:
        data = connfd.recv(1024)  # 接受客户端消息
        # 得到空则退出循环
        if not data:
            break
        print("接收到的客户端消息：", data.decode())
        data = input("服务器回复：")  # 回复客户机
        n = connfd.send(data.encode())  # 发送消息   需转换为字节串
        print("共发送了%d个字节数据" % n)

# 关闭套接字
connfd.close()
sockfd.close()
