import struct
from socket import *

# 服务器地址
ADDR = ('176.140.6.137', 8888)

st = struct.Struct("i32sif")

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 消息收发
while True:
    print("*********************")
    id = int(input("id:"))
    name = input("name:")
    age = int(input("age:"))
    score = float(input("score:"))

    data = st.pack(id, name.encode(), age, score)

    sockfd.sendto(data, ADDR)

# 关闭套接字
sockfd.close()
