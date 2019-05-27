# 1.输入一个字符串,输出每个字符的编码值
# int_char=str(input("请输入一个字符:"))
# print(ord(int_char))


# 2.循环输入编码值,显示字符,直到输入负数时退出

# while True:
#   int_char = int(input("请输入一个编码值:"))
#   if int_char < 0:
#     break
#   print(chr(int_char))
#

# 3.显示120秒倒计时
# num = 120
# while True:
#  if  num >=+- 0:
#     fz = num.- // 60
#     miao = num % 60
#     num -= 1
#     print("%02d:%02d"%(fz,miao))

# 练习:输入一个字符串,
# 1.打印第一个字符
# 2.打印最后一个字符
# 3.如果是奇数,打印中间的字符
# 4.打印倒数三个字符
# 5.倒叙打印字符
# int_str = str(input("请输入一个字符串:"))
# print("第一个是:", int_str[1])
# print("最后一个是:", int_str[len(int_str) - 1])
# if len(int_str) % 2 == 1:
#    print("中间的字符:",int_str[len(int_str)//2])
# print("倒数三个:", int_str[-3:])
# print("倒叙打印字符:",int_str[::-1])


# #输入一个整数,打印矩形
# num = int(input("请输入一个整数串:"))
# print(num * "*")      #头
# for i in range(num -3):    #中间
#    print("*"+" "*(num-2)+"*")
# print(num * "*")      #尾




#输入学生成绩,计算总分,最高分,最低分
# studen=int(input("请输入学生总数:"))
# list=[]
# for i in range(1,studen+1):
#     list.append(int(input("请输入第%d位同学成绩:"%(i))))
#     print(list)
# print("总分:%d."%(sum(list)))
# print("最高分:%d." % (max(list)))
# print("最低分:%d." % (min(list)))

#输入学生姓名,姓名不能重复,如果输入esc,则停止输入,打印每位学生的姓名
# list=[]
# while True:
#  name = str(input("请输入第%d个学生姓名:"%(len(list)+1)))
#  if name =="esc":
#    break
#      #如果姓名不存在:
#  if name not in list:
#     list.append(name)
#
# for item in list:
#   print(item)





#求最大值
# list01=[12,10,15,48,36,56,88,99,11,14]
# max = list01[0]
# if max < list01[1]:
#   max = list01[1]
# if max < list01[2]:
#   max = list01[2]
# if max < list01[3]:
#   max = list01[3]
# if max < list01[4]:
#   max = list01[4]
# if max < list01[5]:
#   max = list01[5]
# if max < list01[6]:
#   max = list01[6]
# if max < list01[7]:
#   max = list01[7]
# if max < list01[8]:
#   max = list01[8]
# if max < list01[9]:
#   max = list01[9]
#
# print(max)
#方法二:
list01=[12,10,15,48,36,56,88,99,11,14]
max=list01[0]    #假设第一个最大
for i in range(1,len(list01)):#依次与第二个开始比较
  if max < list01[i]:
    max= list01[i]
print(max)                   #(shift+F6可以重命名变量)