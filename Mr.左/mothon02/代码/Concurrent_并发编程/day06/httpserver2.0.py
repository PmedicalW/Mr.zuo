"""
http server v2.0
＊io 并发处理(连接多个客户端)
＊基本的request解析
＊使用类封装
"""
from socket import *
from select import select


# 将具体http server功能封装
class HttpServer:
    def __init__(self, server_address, static_dir):
        # 添加属性
        self.server_address = server_address
        self.static_dir = static_dir
        self.rlist = []  # 变成属性变量，这样每个函数就都能使用了
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.port = self.server_address[1]

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)
        # 循环监听
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from", addr)
                    self.rlist.append(c)
                else:
                    # 处理浏览器请求
                    self.handle(r)

    # 处理客户端请求
    def handle(self, connfd):
        # 接收http请求
        request = connfd.recv(4096)
        if not request:  # 防止客户端断开
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 请求解析
        request_line = request.splitlines()[0].decode()  # 将request按行分割取第一行
        info = request_line.split(' ')[1]
        print(connfd.getpeername(), ':', info)

        # info　分为访问网页和其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

        self.rlist.remove(connfd)
        connfd.close()

    # 处理网页
    def get_html(self, connfd, info):
        if info == '/':
            # 网页文件
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + info
        try:
            fd = open(filename)  # 打开网页文件
        except Exception:
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += '\r\n'
            responseBody = "<h1>Sorry,Not Found the page</h1>"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'  # 换行
            responseBody = fd.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    # 其他情况
    def get_data(self, connfd, info):
        responseHeaders = "HTTP/1.1 200 OK\r\n"
        responseHeaders += '\r\n'
        responseBody = "<h1>Waiting httpserver 3.0</h1>"
        response = responseHeaders + responseBody
        connfd.send(response.encode())


# 如何使用HttpServer类
if __name__ == '__main__':
    # 用户自己决定：地址，内容
    server_address = ('0.0.0.0', 8888)
    static_dir = "./static"  # 网页存放位置/路径(当前路径的static文件夹)

    httpd = HttpServer(server_address, static_dir)  # 生成实例对象
    httpd.server_forever()  # 启动服务(浏览器输入ip:port/网页即可启动服务)
