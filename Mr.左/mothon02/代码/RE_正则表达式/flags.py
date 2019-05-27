import re

s="""Hello world
你好,六月
"""

# # 只能匹配Ascii码字符
# regex = re.compile(r'\w+',flags=re.A) # ['Hello', 'world']

# # 忽略字母大小写
# regex = re.compile(r'[a-z]+',flags=re.I) # ['Hello', 'world']

# 匹配换行
# regex = re.compile(r'.+',flags=re.S)  # ['Hello world\n你好,六月\n']

# 匹配每行开头结尾
# regex = re.compile(r'^Hello',flags=re.M) # ['Hello']
# regex = re.compile(r'world$',flags=re.M)   # ['world']


# 正则添加注释
pattern = r"""\w+  #  第一部分
\s+  #  第二部分
\w+  #  第三部分
"""
regex = re.compile(pattern,flags=re.X)


l= regex.findall(s)
print(l)











