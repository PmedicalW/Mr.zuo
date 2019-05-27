"""
day06 作业：
1. 参照下列代码，定义判断是否是奇数的方法．
def verdict(number):
    if type(number) != int:
        return "输入有误"
    if number % 2 == 0:
        return "偶数"
    return "奇数"
print(verdict(3))

# 2.参照下列代码，定义根据月份返回天数的方法．
#   要求：考虑２月，如果是闰年返回２９天，否则返回２８天．
def month_input(year,month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        if year%400==0 or year % 4 ==0 and year % 100 != 0:
           return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31
print(month_input(400,2))

#3.参照下列代码，定义获取最小值方法．
def get_min(list_):
    min = list_[0]
    for i in range(1, len(list_)):
        # 发现更小的，则替换假设的．
        if min > list_[i]:
            min = list_[i]
    return min
print(get_min([7,9,1,4,3]))

#4. 定义函数，判断字符串中存在的中文字符数量．
#   中文编码范围：0x4E00   ord(字符)    0x9FA5

#list_=[]
number=0
list01=list_(input("请输入字符串:"))
# str_number = input("请输入字符串:")
# for item in str_number:
#     list_.append(item)
print(list01)
for i in range(len(list01)-1):
   if ord(list01[i]) <=0x9FA5 and ord(list01[i]) >= 0x4E00:
      number += 1
print(number)
"""
def character_count(str_number):
   number=0
   list01=list(str_number)
   print(list01)
   for i in range(len(list01)-1):
     if ord(list01[i]) <=0x9FA5 and ord(list01[i]) >= 0x4E00:
        number += 1
   return "有"+str(number)+"个中文"

print(character_count("我是肚子疼hhh"))

#5. 扩展练习(定义函数，返回指定范围内的素数)
#例如：１－－１００　　