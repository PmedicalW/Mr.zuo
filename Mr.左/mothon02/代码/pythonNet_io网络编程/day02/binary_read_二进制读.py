# 二进制文件读取操作
# 以二进制方式打开
fd=open('test','rb')
data=fd.read()
print(data)   # b'hello\n\xe4\xbd\xa0\xe5\xa5\xbd\nkitty'　   #得到的是字节串
print(data.decode())# 转换为字符串　　# hello  你好  kitty

fd.close()

"""
test文本：
hello
你好
kitty
"""
