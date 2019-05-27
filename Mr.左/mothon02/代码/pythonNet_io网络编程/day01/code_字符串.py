"""
重点代码
"""
s = input(">>")
print("str:",s)# 字符串
print("bytes:",b"hello world")# 字节串

byte=s.encode()
print("字符串转换字节串:",byte)# 字符串---->字节串

str=byte.decode()
print("字节串转换字符串:",str)# 字节串---->字符串

# 通过字节串转换函数转换为字节串
print("int i:",bytes([1,2,3]))
#bytes()
# 参数：
# 整数ｎ  初始化一个长度为n的列表序列
# 字符串　　将字符串转换为字节串
# 0-255整数列表　　将列表整数转换bytes字节串







