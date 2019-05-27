import re

# s = "Levi:1994,Sunny:1993"
# # pattern = r"\w+:\d+"# 没有子组　　  ['Levi:1994', 'Sunny:1993']
# # pattern = r"(\w+):\d+"# 有子组     ['Levi', 'Sunny']
# pattern = r"(\w+):(\d+)"# 有子组     [('Levi', '1994'), ('Sunny', '1993')]

# # re模块调用
# l=re.findall(pattern,s)
# print(l)

# # compile对象调用
# regex = re.compile(pattern)
# l = regex.findall(s)
# print(l)


# s= "hello world how are  you  L-boby"
# l= re.split(r'[^\w]+',s)
# print(l)

# # 替换字符串
# s="时间：2019/10/12"
# ns=re.sub(r'/','-',s)
# print(ns)


# s="5月,再见，6月,你好"
# pattern = r"\d+"
# # 返回包含匹配结果的迭代器
# it=re.finditer(pattern,s)
# for i in it:
#     print(i.group())


# # 完全匹配
# # m=re.fullmatch(r'\w+',"hello-1973")
# m=re.fullmatch(r'\w+',"hello1973")# 可以用来验证密码
# print(m.group())


# # 匹配开始位置
# m=re.match(r'[A-Z]\w*',"Hello world")
# print(m.group())


# # 匹配第一处
# m = re.search(r'\S+', "好\n嗨 哟")
# print(m.group())


pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
# 获取match对象
obj = regex.search("abcdefghi",pos=0,endpos=7)
# 属性变量
print(obj.pos)# 目标字符串开头位置
print(obj.endpos)# 目标字符串结束位置
print(obj.re)# 正则
print(obj.string)# 整个目标字符串
print(obj.lastgroup)# 最后一组名称
print(obj.lastindex)# 最后一组序列号

print("*******************************************")
# 属性方法
print(obj.start())# 开始
print(obj.end())# 结束
print(obj.groupdict())# 捕获组字典
print(obj.groups())# 子组对应内容
print(obj.group(1))# 序列号
print(obj.group('pig'))# 组名


