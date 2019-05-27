"""
#在控制台输入学生信息
#在一行输出
#格式:我的姓名是:xxx,年龄是:xxx,性别是:xx,成绩是:xxx.
str_name = str(input("请输入姓名:"))
age = int(input("请输入年龄:"))
str_sex = str(input("请输入性别:"))
float_score = float(input("请输入成绩:"))
#print("我的姓名是:"+str_name+",年龄是:",age,",性别是:"+str_sex+",成绩是:",float_score)
print("我的姓名是:"+str_name+",年龄是:"+str(age)+",性别是:"+str_sex+",成绩是:"+str(float_score))
"""


"""
#1.输入单价,数量,总额,算出找额
num = float(input("请输入商品单价:"))
price = int(input("请输入商品数量:"))
money = float(input("请输入总额:"))
xufu = num*price
sum =money-xufu
print("总计需付:",xufu,"元,收你:",money,"找回:",sum)


#2.输入小时,分钟,秒,计算总秒数
h = float(input("请输入小时:"))
m = float(input("请输入分钟:"))
s = float(input("请输入秒:"))
sum = h * 3600 + m *60 + s
print(sum)


#3.古代一斤16两,现输入两数,换算出几斤几两
num = int(input("你输入的两数:"))
jin = num // 16
liang = num % 16
print("结果:",jin,"斤",liang,"两")




#1.闰年判断
#条件1:年份能被4整除,但是不能被100整除
#条件二:年份能被400整除
#在控制台输入年份
#判断是否为闰年,如果是显示True,否则显示false
year = int(input("请输入年份:"))
print(year%400==0 or year % 4 ==0 and year % 100 != 0)


#2.输入四位整数,计算每位相加和
num = int(input("请输入四位整数:"))
gewei = num % 10
shiwei = num % 100 // 10
baiwei = num % 1000 // 100
qianwei = num // 1000
sum = gewei + shiwei + baiwei + qianwei
print("结果:",sum)

#输入一个总秒数,转换成几小时几分钟,几秒钟
int_zm = int(input("请输入总秒数:"))
h = int_zm // 3600
m = int_zm % 3600 // 60
s = int_zm % 60
print(h,":小时",m,":分钟",s,":秒")

#输入一个整数,判断奇偶数
int_num=int(input("请输入一个整数:"))
if int_num % 2 == 0:
    print("这是一个偶数")
else:
    print("这是一个奇数")
"""
#输入一个整数,判断是否是闰年
year = int(input("请输入年份:"))
if year%400==0 or year % 4 ==0 and year % 100 != 0:
    print("这是闰年")
else:
    print("这不是闰年")
















