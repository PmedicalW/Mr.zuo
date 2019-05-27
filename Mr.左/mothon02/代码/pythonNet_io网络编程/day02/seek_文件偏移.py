# 文件偏移量
fd=open('test','r+')
# 相对开头位置向后偏移了多少
print("当前文件偏移量位置：",fd.tell())#0
print(fd.read(2))   # he
print("当前文件偏移量位置：",fd.tell())#2
print(fd.read(2))   # ll

# 人为调整文件偏移
fd.seek(0,0)# 相对开头位置向后偏移０个
print(fd.read(5))   # hello

fd.seek(5,0)#相对开头位置向后偏移5个
print(fd.read(2))   # 你　　　（换行也算一个字符）


fd.close()

"""
test文本：
hello
你好
kitty
"""
