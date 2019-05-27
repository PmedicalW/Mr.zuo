# 文件的读操作
# 打开文件返回文件对象
fd=open('test','r')
# #读操作
while True:
    data01=fd.read(8)
    # 如果文件读到空表示文件已经读完
    if not data01:
        break
    print("read读取到的内容：")
    print(data01)    # 换行也算一个字符


# 读取一行内容
data02=fd.readline(4)
#data02=fd.readline()   # 会读取上一行剩下的字符   # o
print("readline读取到的内容：")
print(data02)# hell


# 将读取内容作为列表返回
data03=fd.readlines()
print("readlines读取到的内容：")
print(data03)# ['hello\n', 'kitty\n', '你好\n']


# fd 为可迭代对象，使用for循环每次获取一行内容
for line in fd:
    print("每行内容：",line)# 每行内容： hello

                          # 每行内容： kitty

                          # 每行内容： 你好

# 关闭文件
fd.close()










