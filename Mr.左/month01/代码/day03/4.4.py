# 输入两个整数,一个作为开始值,一个作为结束值,请输出中间值
# num01 = int(input("请输入第一个整数:"))
# num02 = int(input("请输入第二个整数:"))
# num = None
# while num!=0:
#  if num01 >= num02:
#     num = num01 - 1
#     print(num)
#  else:
#     num = num02 - 1
#     print(num)
#

#输入学生姓名,姓名不能重复,如果输入esc,则停止输入,打印每位学生的姓名
list=[]
name=str(input("请输入学生姓名:"))
while name != "esc":

 list.append(name)
 print(list)
 if name  in "esc":
  break
