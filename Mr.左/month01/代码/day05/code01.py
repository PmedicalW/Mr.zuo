# import copy
# list01 = [1,[2,3]]
# list02=copy.deepcopy(list01)
# list01[1][0]=200
# print(list02[1][0])


# 练习1.使用range生成1-10之间的数字,
# 存入list01,使用列表推导式把奇数存入list02
"""
list01 = []
list02 = []
for i in range(10):
 list01.append(i)
 print(i)
 if i%2==0:
  list02.append(i)
print(list02)

#2.输入几月几日,计算总天数
(1)
result = 0
month=int(input("请输入月份:"))
day=int(input("请输入日:"))
month_day=(31,28,31,30,31,30,31,31,30,31,30,31)
for i in range(month-1):
  result += month_day[i]
result +=day
print(result)

(2)
month = int(input("请输入月份:"))
day = int(input("请输入日:"))
month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
result = sum(month_day[:month - 1])
result += day
print(result)


#3.0
dict={1:"有1,2,3月",
      2:"有4,5,6月",
      3:"有7,8,9月",
      4:"有10,11,12月"
 }
print(dict)
season = int(input("请输入季度:"))
#if season<1 or season>4:
if season not in dict:
    print("输入有误")
else:
    value = dict[season]
    print(value)

#4.输入一个字符串,判断每个字符出现的次数
dict={}       #key  字符    value  次数
str_input=str(input("请输入字符串:"))
for item in str_input:         #逐一判断字符出现的次数
    if item not in dict:      #如果没有统计过该字符
        dict[item]=1
    else:
        dict[item] +=1
print(dict)


dict={}
list=["张三丰","无忌","赵敏"]
for item in list:
    dict[item]=len(item)
print(dict)
"""
dict={}
list01=["张三丰","无忌","赵敏"]
list02=[101,102,103]
key=list[0]

dict={"张三丰":101,"无忌":102,"赵敏":103}


print(dict)