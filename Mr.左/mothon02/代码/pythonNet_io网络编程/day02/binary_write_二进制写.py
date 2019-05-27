# 二进制文件写操作
# 以二进制方式写入
fd=open('test','wb')
fd.write(b"hello kitty")  # 必须写入字节串

fd.close()