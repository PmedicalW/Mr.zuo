# 从终端输入一个文件名称（可以夹带路径），将该文件复制到当前目录下，
# 并且重命名为ｘｘｘ，要求可以复制所有类型文件
filename = input("请输入文件名称:")
try:
    fr = open(filename, 'rb')
except FileNotFoundError as e:
    print(e)
else:
    fw = open('myfile', 'wb')  # xxx重命名为myfile
    # 循环读取文件内容写入到myfile文件
    while True:
        data = fr.read(1024)
        # 　读到文件结尾
        if not data:
            break
        fw.write(data)

    fr.close()
    fw.close()
