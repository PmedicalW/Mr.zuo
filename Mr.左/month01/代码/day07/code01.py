#
# def fun01(num01):
#     num01=2
#     print("num01:"+str(num01))
#
# number01=1
# fun01(number01)
# print("number01:"+str(number01))
# print("number01:"+str(fun01(number01)))
#统计一个方法的调用次数
# count=0
# def fun():
#  global count
#  count+=1
#
# fun()
# fun()
# fun()
# print(count)
#================================================
#
# def fun(a,b,c):
#  print(a)
#  print(b)
#  print(c)
#  #位置传参:实参与形参的位置依次对应
# fun(1,2,3)
#
#       #序列传参:用*将序列拆分后与形参的位置依次对应
                 #可以进行时,根据某些逻辑决定传入的数据(列表)
# fun(*(4,5,6))
# fun(*[4,5,6])
# fun(*{4,5,6})
# fun(*{4:5,6:7,8:9})
#
#  #关键字传参:实参根据形参的名称进行对应
# fun(b=4,a=5,c=6)
#
#       #字典传参:用**将字典拆解后与形参的名字进行对应
                #可以进行时,根据某些逻辑决定传入的数据(字典)
# fun(**{"a":'AA',"b":'BB',"c":'CC'})


# #默认传参(让调用者可以有选择性的传递需要的信息)
# def fun2(a=0,b=0,c=0):
#  print(a)
#  print(b)
#  print(c)
#  #不写参数,使用默认值
# fun2()
# fun2(1,2)
# #关键字传参 与 默认传参相结合
# fun2(c=3)

# #练习:定义函数,根据天/小时/分钟,计算总秒数
# def get_second(day=0,hour=0,minte=0):
#   return day*24*60*60+hour*60*60+minte*60
#
# print(get_second(1))
# print(get_second(1,2))
# print(get_second())

# #定义函数,整数相加的函数
# # def int_sum(*args):
# #   sum=0
# #   for item in args:
# #     sum+=item
# #   return sum
# #
# # print(int_sum(11,2,3,4,5))
# #星号元组形参          对于方法内部而言,就是元组,  对于调用者而言,可以传递数量无限的位置形参
# def fun(*args,b):
#   print(args)
#   print(b)
# fun()
# #双星字典形参     对于方法内部而言,就是字典,  对于调用者而言,可以传递数量无限的关键字形参
# def fun(*kwargs,b):
#   print(kwargs)
#   print(b)
#
def fun(a,b,*args,c,d,**kwargs):
  print(a)
  print(b)
  print(args)
  print(c)
  print(d)
  print(kwargs)

fun(1,2,3456,c='A',d='B')







