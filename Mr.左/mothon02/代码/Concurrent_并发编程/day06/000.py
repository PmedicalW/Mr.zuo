# http功能演示
# 将网页发送给浏览器展示

from socket import *

# 处理浏览器请求
def handle(connfd):
    print("Request from", connfd.getpeername())  # 打印连接套接字客户端地址
    request = connfd.recv(4096)  # 接收http请求
    if not request:  # 防止客户端断开
        return
    request_line = request.splitlines()[0].decode()  # 将request按行分割取第一行
    print(request_line)

    # 获取请求内容
    info = request_line.split(' ')[1]
    print(info)
    if info == '/':  # 判断请求内容不为空
        f = open('index.html')  # 打开创建好的网页文件
        # 格式
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += '\r\n'  # 换行
        response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += '\r\n'
        response += "<h1>Sorry...</h1>"
    connfd.send(response.encode())  # 向浏览器发送内容


# 搭建tcp网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(('0.0.0.0', 8001))
    sockfd.listen(5)
    print("Linsten the port 8001...")  # 打印监听的端口号
    while True:
        connfd, addr = sockfd.accept()  # 循环接收连接
        handle(connfd)  # 处理浏览器请求
        connfd.close()


if __name__ == '__main__':
    main()# 调用函数

# 最后在浏览器输入地址：端口号