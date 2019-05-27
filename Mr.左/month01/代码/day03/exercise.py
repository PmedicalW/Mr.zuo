"""
#1.用真值表达式判断奇偶数
num = "偶数" if int(input("请输入整数:")) % 2 == 0 else "奇数"
print(num)
#2.输入一个年份,是闰年给变量day赋值29,赋值28
year = int(input("请输入年份:"))
day = 29 if year%400==0 or year % 4 ==0 and year % 100 != 0 else 28
print(day)

# 输入两个整数,一个作为开始值,一个作为结束值,请输出中间值
num01 = int(input("请输入第一个整数:"))
num02 = int(input("请输入第二个整数:"))
num = None
while True:
 if num01 >= num02:
    num = num01 - 1
    print(num)
 else:
    num = num02 - 1
    print(num)
    if num=0:
       break
#
ks = int(input("请输入第一个整数:"))
js = int(input("请输入第二个整数:"))
while ks < js-1:
    ks += 1
    print(ks)

# 一张纸厚度0.01mm,请问对着多少次可以超过珠穆拉玛峰8844.43m
zihou = 0.01
cishu = 0
while zihou < 8844.43 * 1000:
    cishu += 1
    zihou = 0.01 * 2 ** cishu  # 初始纸厚不变
print(cishu)

# 1.猜数字,系统随机产生1-100,让用户重复猜,知道猜中为止,要有提示

import random
random_number = random.randint(1, 100)
while 1:
    num = int(input("请输入你猜的数字:"))
    if num > random_number:
        print("你猜的数字太大了")
    elif num < random_number:
        print("你猜的数字太小了")
    else:
        print("猜对了")
        break

# 2.猜数字,系统随机产生1-100,让用户重复猜,直到猜中为止,要有提示,且最多可以猜10次
import random
random_number = random.randint(1, 100)
count = 0
while count < 10:
    count += 1
    num = int(input("请输入你猜的数字:"))
    if num > random_number:
        print("你第",count,"猜的数字太大了")
    elif num < random_number:
        print("你第",count,"猜的数字太小了")
    else:
        print("恭喜你,你第",count,"猜对了")
        break
else:
    print("你的10次机会已用完!")

#下列代码执行五次
input01=input("请输入第一个变量:")
input02=input("请输入第二个变量:")
input01,input02=input02,input01

#
for i in range(5):
    input01 = input("请输入第一个变量:")
    input02 = input("请输入第二个变量:")
    input01, input02 = input02, input01

#随机加法考试,随机产生两个数字,输入两个数的相加结果,如果输入正确累加10分,错误扣5分,总共五题
import random
chenji=0
for i in range(5):
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    print("第一个数为:",random_number01)
    print("第二个数为:",random_number02)
    sum = random_number01+random_number02
    num = int(input("请输入你的答案:"))
    if num == sum:
        chenji += 10
    else:
        chenji -= 5
print(chenji)

#累加1-100之间能被三整除的整数和
sum = 0
for num in range(1,100):
    if num % 3 == 0:
     sum+=num
    continue
print(sum)

"""














