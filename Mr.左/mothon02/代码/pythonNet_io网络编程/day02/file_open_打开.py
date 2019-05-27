# 文件操作：打开，读写，关闭

# 打开文件
try:
    fd=open("test")
except FileNotFoundError as e:
    print(e)
else:
    print("打开'File.py'文件成功！")

# 开始你的读写


# 关闭文件
    fd.close()














