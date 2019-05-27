# 写入操作
fd = open('test','w')
fd.write("hello 死鬼\n")
fd.write("来了老弟\n")
# test文本会写入：
# hello 死鬼
#来了老弟


# 写入一个列表内容
fd.writelines(["hello world\n","hello kitty\n"])
# test文本会写入：
# hello world
# hello kitty

fd.close()













