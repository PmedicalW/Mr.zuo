from socket import *
# 创建tcp套接字
s = socket()
s.bind(('0.0.0.0', 8000))
s.listen(5)

c, addr = s.accept()
print("Connect from", addr)
data = c.recv(4096)
print(data)

# 格式
data = """HTTP/1.1 200 OK   
Connect-Type:text/html

<h1>hello world</h1>
<h1>hello kitty</h1>
"""
c.send(data.encode())

c.close()
s.close()

# 运行后在浏览器输入本地地址：端口号
# eg:176.140.6.137:8000
