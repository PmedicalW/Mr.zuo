'''
 在控制台中录入5个学生信息(姓名／年龄／性别)
数据结构：列表中嵌套字典
[{"name":xx,
  "age":xx,
  "sex":xx,},
{"name":xx,
 "age":xx,
 "sex":xx,}.......]
'''
# list=[]
# d01={}
# for i in range(2) :
#     d01[i]={"name":str(input("请输入姓名:")),
#             "age":int(input("请输入年龄:")),
#             "sex":str(input("请输入性别:"))}
#     list.append(d01[i])
# for d01 in list:
#  for key,value in d01.items():
#    print("%s - - %s"%(key,value))

# 6.扩展练习：
# 　猜拳
#   规则：系统随机出拳，在控制台中循环猜测．
#   提示：(1)将胜利的策略存入容器
#               (("石头","剪刀"),
#                ("剪刀","布"),
#                ("布","石头"))
#        (2) 将用户猜的拳与系统出拳形成一个元组
#


list_student_info = []
for i in range(2):
    # 每次循环创建一个新字典表示一个新学生
    dict_student = {}
    dict_student["name"] = input("请输入姓名：")
    dict_student["age"] = int(input("请输入年龄："))
    dict_student["sex"] = input("请输入性别：")
    # 向学生列表追加学生信息
    list_student_info.append(dict_student)
# 获取所有学生信息
for dict_stu in list_student_info:
    for key,value in dict_stu.items():
        print("%s -- %s"%(key,value))
print(list_student_info)















