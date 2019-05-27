#练习:对象计数器
#创建老婆类(名字),随意实例化对象
#统计老婆数量(定义方法),画出内存图
# class Wife:
#
#     count=0
#     def __init__(self,name="",age=0,height=0):
#         self.name = name
#         self.age=age
#         self.height=height
#         Wife.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return Wife.count
#
# w01=Wife("刘亦菲",18)
# w01=Wife("杨幂",20,170)
# print("老婆数量:",Wife.get_count())


# class Enemy:
#     """
#     敌人
#     """
#     def __init__(self,name="",hp=0,atk=0,speed=0):
#         # self.name=name
#         # self.hp=hp
#         # self.atk=atk
#         # self.atk_speed=atk_speed
#           self.set_name(name)
#           self.set_hp(hp)
#           self.set_atk(atk)
#           self.set_speed(speed)
#
#     def get_name(self):
#         return self.__name
#     def set_name(self,value):
#         self.__name=value
#
#     def get_hp(self):
#         return self.__hp
#
#     def set_hp(self,value):
#         if 0<= value <= 100:
#            self.__hp=value
#         else:
#             self.__hp=0      #当赋予值不在范围内,赋予它一个默认值
#             print(value,"当前赋值不在范围内")
#
#     def get_atk(self):
#         return self.__atk
#     def set_atk(self,value):
#         self.__atk=value
#
#     def get_speed(self):
#         return self.__speed
#
#     def set_speed(self, value):
#         if 0 <= value <= 10:
#            self.__speed = value
#         else:
#             self.__speed =0
#             print(value,"当前赋值不在范围内")
#
# e01=Enemy("哥斯拉",200,50,20)
# print(e01.get_name(),e01.get_hp(),e01.get_atk(),e01.get_speed())

# #最终代码(用属性封装的方法)
# class Enemy:
#     """
#     敌人
#     """
#     def __init__(self,name,hp):
#           self.name=name
#           self.hp=hp
#
#     @property         #读取name的变量
#     def name(self):
#         return self.__name
#
#     @name.setter      #写入name的变量
#     def name(self,value):
#         self.__name=value
#
#     @property
#     def hp(self):
#         return self.__hp
#
#     @hp.setter
#     def hp(self,value):
#         if 0<= value <= 100:
#            self.__hp=value
#         else:
#             self.__hp=0      #当赋予值不在范围内,赋予它一个默认值(不然会报错)
#             print(value,"当前赋值不在范围内")
#
# e01=Enemy("哥斯拉",200)
# print(e01.name,e01.hp)

"""
    静态方法引入
    00   01   02    03
    10   11   12    13
    20   21   22    23

    需求：在某个元素基础上，获取每个方向，指定数量的元素．
          10               向右　　　　　３　　　　--> 11 12  13
          21               向上　　　　　２　　　　--> 11 01
          .....
"""
class Vector2:
    """
        向量
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        # #　实例方法
        # def fun01(self):
        #     pass
        #
        # # 类方法
        # @classmethod
        # def fun02(cls):
        #     pass
        #
        # # 静态方法：得不到对象地址／也得不到类名
        # @staticmethod
        # def fun03():
        #     pass


# v01 = Vector2()
# v01.fun01()# 隐式传递对象地址
#
# Vector2.fun02()# 隐式传递类名
#
# Vector2.fun03()


def right():
    return Vector2(0,1)

def up():
    return Vector2(-1,0)

# ...



# 在某个元素基础上，获取每个方向，指定数量的元素．
def get_elements(list_target, v_pos, v_dir, count):
    result = []
    for i in range(count):
        # 位置　＋＝　方向
        # 1 0        0 1   －－＞ 1 1
        # 1 1        0 1         1 2
        # 1 2        0 1         1 3
        v_pos.x += v_dir.x
        v_pos.y += v_dir.y
        result.append(list_target[v_pos.x][v_pos.y])
    return result


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

#  10               向右　　　　　３　　　　－－> 11 12  13
# re01 = get_elements(list01,Vector2(1,0),Vector2(0,1),3)
#  21               向上　　　　　２　　　　-->11   01
# re02 = get_elements(list01,Vector2(2,1),Vector2(-1,0),2)


# 直接调用向左，向上函数
re01 = get_elements(list01,Vector2(1,0),right(),3)
print(re01)
re02 = get_elements(list01,Vector2(2,1),up(),2)
print(re02)



























