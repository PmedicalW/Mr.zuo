'''
#1
s01=set()
while True:
 str_input = input("请输入字符串:")
 if str_input=="q":
     break
 s01.add(str_input)
print(s01)


#2
manager=["曹操","刘备","孙权"]
technician=["曹操","刘备","张飞","关羽"]
s_manager=set(manager)
s_technician=set(technician)
s01=s_manager & s_technician
print("既是经理又是技术员的有:",s01)
s02=s_manager - s_technician
print("是经理不是技术员的有:",s02)
s03=s_technician - s_manager
print("是技术员不是经理的有:",s03)


# for r in range(2):
#     for c in range(6):
#         print("*",end="")
#     print()
#     for c in range(6):
#         print("#",end="")
#     print()


#
# for r in range(4):
#     for c in range(r+1):
#         print("*", end="")      #不换行
#     print()          #换行
#

# for r in range(4):
#     for c in range(r):
#         print(" ", end="")
#     for c in range(4-r):
#         print("*", end="")
#     print(" ")

# 判断列表是否有相同元素
# 思想:
# 取第一个元素和后面所有元素比较
# for i in range(1,len(list_)-1):
#     if list_[0] == list_[i]:
#         print()
# 取第二个元素和后面所有元素比较
# for i in range(2, len(list_) - 1):
#     if list_[1] == list_[i]:
#         print()
# 取第三个元素和后面所有元素比较
# for i in range(3, len(list_) - 1):
#     if list_[2] == list_[i]:
#         print()
list_ = [1, 2, 3, 4, 1, 2, 3, 7]
list01 = []
state = False
for l in range(len(list_) - 1):  # 取出前几个元素
    for i in range(l + 1, len(list_)):  # 与后面元素比较
        if list_[l] == list_[i]:  # 如果发现相同元素
            list01.append(list_[i])
            state = True
            break  # break 只能退出就近循环体
if state:
    print("具有相同元素", list01)
else:
    print("没有相同元素")


#对列表进行排序
list_ = [1, 2,4,8,9, 3, 7]
list01 = []
state = False
for l in range(len(list_) - 1):
    for i in range(l + 1, len(list_)):
        if list_[l] > list_[i]:  # 两两元素比较
           list_[l],list_[i]=list_[i],list_[l]  #两两交换
print(list_)


#列表推导式嵌套
#实现两个列表的全排列
list01=["香蕉","苹果","哈密瓜"]
list02=["可乐","牛奶"]
list03=[r+c for r in list01 for c in list02]
print(list03)

#定义一个矩形函数
def square(count_r,count_c,char):
    for r in range(count_r):
        for c in range(count_c):
            print(char, end="")
        print()
square(2,6,"-")


#定义一个直角三角形函数
def trigon(count_r,char):
    """
    定义:打印三角形
    :param count_r: 三角形边长
    :param char:    组成三角形的字符
    :return:
    """
    for r in range(count_r):
        for c in range(r+1):
            print(char, end="")
        print()
trigon(3,"*")

#####
def list_element_same(list_):
    list01 = []
    for l in range(len(list_) - 1):  # 取出前几个元素
        for i in range(l + 1, len(list_)):  # 与后面元素比较
            if list_[l] == list_[i]:  # 如果发现相同元素
                list01.append(list_[i])
                return True
    return False

re01=list_element_same([1,2,1])
print(re01)
'''

def month_number(month):
    if month < 1 or month > 12:
        return "输入有误"
    if month <=3:
        return"春天"
    if month <=6:
        return"夏天"
    if month <=9:
        return"秋天"
    return"冬天"


print(month_number(13))






