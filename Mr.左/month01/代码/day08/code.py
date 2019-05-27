# class Wife:
#     """
#     老婆
#     """
#     #1.数据成员:姓名,年龄,性别
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     #2.方法成员:做饭
#     def cooking(self):
#         print("做饭")
# #创建对象
# #调用__init__(self,name,age,sex)
# w01=Wife()

#(1)学生student是一个类，具有姓名，年龄等数据；
'''
#具有学习study，工作work等行为。
class Student:
    """
    学生
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print(self.name+"学习,"+str(self.age))

    def work(self):
        print(self.name+"工作,"+str(self.age))

w01=Student("悟空同学",28)
w01.study()
w01.work()

w02=Student("八戒同学",29)
w02.study()
w02.work()
'''

class Enemy:
    """
    敌人
    """
    def __init__(self,name="",hp=0,atk=0,atk_speed=0):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.atk_speed=atk_speed

    def print_self(self):
        print(self.name,self.hp,self.atk,self.atk_speed)


#1.在控制台中输入3个敌人,存入列表
list=[]
for i in range(3):
    e=Enemy()
    e.name=str(input("请输入第%d次的名字:"%(i+1)))
    e.hp = int(input("请输入%d次的血量:"%(i+1)))
    e.atk = float(input("请输入%d次的攻击力:"%(i+1)))
    e.atk_speed = float(input("请输入%d次的攻击速度:"%(i+1)))
    list.append(e)
for item in list:
    item.print_self()


# 练习３：定义函数，在敌人列表中，根据姓名查找敌人对象．
# e01 = Enemy("zs",100,10,2)
# e02 = Enemy("ls",200,5,3)
# e03 = Enemy("ww",300,8,5)
#
# list_enemy = [e01,e02,e03]

def get_enemy_for_name(list_enemy,name):
    # 遍历敌人列列表
    for item in list_enemy:
        # 如果有指定名称的敌人对象
        if item.name == name:
            # 则返回对象地址
            return item

list01 = [
    Enemy("zs",100,10,2),
    Enemy("ls", 200, 5, 3),
    Enemy("ww",300,8,5)
]

re = get_enemy_for_name(list01,"ls")
if re != None:
    re.print_self()
else:
    print("没有找到")









