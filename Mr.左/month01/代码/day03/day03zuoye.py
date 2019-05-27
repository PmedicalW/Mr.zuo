# day03作业:

# 1.一个球从100m的高度落下,每次弹回原高度的一半,总共弹多少次?
# 假定最小高度为0.01m,总共弹了多少米
h = 100  # 开始高度
cishu = 0  # 弹的次数
zongchang = 0  # 一共弹的总长
while h > 0.01:
    zongchang += h + 1 / 2 * h
    h *= 1 / 2
    cishu += 1
print("总共弹了", cishu - 1, "次", "总共弹了", zongchang, "米")
"""


# 2.输入一个整数,判断是否为素数(只能被1和自身整除的数字,不能被其他数整除)
# 提示:循环出2到该数字减一之间的数,再判断能否被之间的数整除
num = int(input("请输入一个整数:"))
if num <2:
   print("不是素数")
else:
   for i in range(2, num,1):
       if num % i == 0:
           print("这不是素数")
           break          #如果有结果了就不需要再和后面的数字比较了
   else:
       print("这是素数")

"""



