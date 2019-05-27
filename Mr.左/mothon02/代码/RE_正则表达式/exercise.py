import re
import sys

port=sys.argv[1]   # 终端输入  eg:python3 BVI100

fd = open('1.txt')

# 找到port段落
while True:
    data=''
    for line in fd:
        if line != '\n': #不是空行
            data += line
        else:
            break
    # print("段内容：",data_数据结构)
    if not data:# 文件结尾
        print("Not Found the %s"%port)
        break

    # 匹配字符串首个单词
    key_word = re.match(r'\S+',data).group()
    # print(key_word)
    if port == key_word:
        # 匹配目标内容
        # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        pattern = r'(\d{1,3}\.){3}\d{1,3}/\d+|Unknown'
        try:
            address = re.search(pattern,data).group()
            # print("address is:",address)
            print("Internet address is:",address)
            break
        except:
            print("No address")
        break
































