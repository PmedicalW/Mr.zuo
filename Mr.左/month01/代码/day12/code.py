'''
class StudentModel:
    """
        学生数据模型类
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "编号：%d,名字：%s,年龄：%d,成绩：%d"%(self.id,self.name,self.age,self.score)

    def __repr__(self):
        return 'StudentModel(%d,"%s",%d,%d)'%(self.id,self.name,self.age,self.score)

s01=StudentModel("老杜",18,60)
print(s01)
s02=eval(s01.__repr__())
print(s02)
list01=[s01,s02]
print(list01)
'''''
class Vector:
    def __init__(self,x):
        self.x=x

    def __str__(self):
        return "向量x的变量是：%d"%self.x

    def __mul__(self, other):
        return Vector(self.x*other)

    def __pow__(self, power, modulo=None):
        return Vector(self.x*power**modulo)

    def __sub__(self, other):
        return Vector(self.x*other)

    def __isub__(self, other):
        self.x -= other
        return self

v01=Vector(8)
# v02=v01*10
# print(v02)

# v03=v01*2**3
# print(v03)
#
# v04=5*v01.x
# print(v04)
#
# v05=Vector(10)
# v06=v01.x*v05.x
# print(v06)
print(v01)
print(id(v01))
v01 -= 5
print(v01)
print(id(v01))



























