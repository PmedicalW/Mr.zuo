'''
day02作业:
1.温度换算器(华氏度,摄氏度,开氏度)
华氏度=摄氏度*1.8+32
摄氏度=(华氏度-32)/1.8
开氏度=摄氏度+273.15
输入华氏度,计算摄氏度
输入摄氏度,计算华氏度
输入摄氏度,计算开氏度
h = float(input("请输入华氏度:"))
print("得到的摄氏度:", (h - 32) / 1.8)
s = float(input("请输入摄氏度:"))
print("得到的华氏度:", s * 1.8 + 32)
s = float(input("请输入摄氏度:"))
print("得到的开氏度:", s + 273.15)


#2.输入圆的半径,计算圆的面积(3.14*r的平方)与周长(2*3.14*r)
r = float(input("请输入圆的半径:"))
print("该圆的面积:",3.14 * r**2,"该圆的周长:",2 * 3.14 *r)
注:round(数据,位数)
   此可以表示需要保留的位数
# 3.输入单价,数量,总额,算出找额,如果金额不足,提示还差多少钱,如果金额够,提示应找回多少
num = float(input("请输入商品单价:"))  # 输入单价
price = int(input("请输入商品数量:"))  # 输入数量
money = float(input("请输入收的现金:"))  # 输入顾客给了多少钱
xufu = num * price  # 需要支付多少钱
sum = money - xufu * 0.8  # 找零
if xufu >= 100:
    if money < xufu:
        print("消费满百元享八折优惠,总计:", xufu, "折后需付:", xufu * 0.8, "元,收你:", money, "元,还差", (xufu * 0.8 - money), "元")
    elif money > xufu:
        print("消费满百元享八折优惠,总计:", xufu, "折后需付:", xufu * 0.8, "元,收你:", money, "元,找回:", sum, "元")
else:
    if money < xufu:
        print("总计需付:", xufu, "元,收你:", money, "元,还差", xufu - money, "元")
    elif money > xufu:
        print("总计需付:", xufu, "元,收你:", money, "元,找回:", money - xufu, "元")


num = float(input("请输入商品单价:"))  # 输入单价
price = int(input("请输入商品数量:"))  # 输入数量
money = float(input("请输入收的现金:"))  # 输入顾客给了多少钱
xufu = num * price  # 需要支付多少钱
sum = money - xufu * 0.8  # 找零
if money < num*price and num*price < 100:
    print("总计需付:", xufu, "元,收你:", money, "元,还差", xufu - money, "元")

elif money >= num*price and num*price < 100:
    print("总计需付:", xufu, "元,收你:", money, "元,找回:", money - xufu, "元")

elif money < num*price and num*price >= 100:
    print("消费满百元享八折优惠,总计:", xufu, "折后需付:", xufu * 0.8, "元,收你:", money, "元,还差", (xufu * 0.8 - money), "元")

else:
    print("消费满百元享八折优惠,总计:", xufu, "折后需付:", xufu * 0.8, "元,收你:", money, "元,找回:", sum, "元")

#调试:让程序在指定的行中断,然后逐语句执行,我们审查程序运行过程,以及变量取值
#1.可能出错的行加入断点
#2.开始调试 alt+shift+f9
#3.命中断点后(断点行是蓝色),逐语句执行F7
# 判断执行过程,以及变量取值
#4.停止调试ctrl+F2

#
yf = int(input("请输入月份:"))
if yf >= 1 and yf <=3:
    print("春")
elif yf >= 4 and yf <=6:
    print("夏")
elif yf >= 7 and yf <= 9:
    print("秋")
elif yf >= 10 and yf <= 12:
    print("冬")
else:
    print("你的输入有误,请重输")


#输入一个月份,返回该月有多少天
yf = int(input("请输入月份:"))
if yf == 1 or yf ==3 or yf ==5 or yf ==7 or yf ==8 or yf ==10 or yf ==12:
    print("该月有31天")
elif yf == 4 or yf ==6 or yf ==9 or yf ==11 :
    print("该月有30天")
elif yf==2:
    print("该月有28天")
else:
    print("你的输入有误,请重输")

#求最大值
num1 = 8
num2 = 6
num3 = 10
num4 = 5
max = num1
if max < num2:
    max = num2
    print(max)
elif max < num3:
    max = num3

elif max < num4:
    max = num4
    print(max)
'''







