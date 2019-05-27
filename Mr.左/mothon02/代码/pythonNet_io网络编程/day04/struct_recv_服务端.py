# １．从客户端输入一个学生的　id 姓名　年龄　分数
# ２．将其发送到服务端，有服务端写入到一个文件中
# ３．每个信息占一行
# ４．数据传输使用udp套接字完成
from socket import *
import struct

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 确定数据结果
st = struct.Struct('i32sif')

# 打开文件
f = open('student.txt', 'a')  # 创建一个student.txt文件，并且在后面追加内容

while True:
    data, addr = sockfd.recvfrom(1024)  # 接收

    # 对接收的数据进行解析
    data = st.unpack(data)

    info = "%d  %s  %d  %.2f\n" % (data[0], data[1].decode(), data[2], data[3])

    f.write(info)

# 关闭套接字
f.close()
sockfd.close()
