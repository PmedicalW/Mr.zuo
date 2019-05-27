#定义父类－－－宠物，名字，行为：吃
#定义子类－－－狗，工作，行为：防守
#定义子类－－－鸟，工作，行为：飞
#创建相应对象，调用相应方法，测试isinstance,issubclass
'''class Chongwu:
    def __init__(self,name):
        self.name=name

    def chi(self):
        print("吃")

class Dog(Chongwu):
    def __init__(self,name,work):
        super().__init__(name)
        self.work=work

    def fagshou(self):
        print("吃屎咯")

class Niao(Chongwu):
    def fei(self):
        print("飞咯")

c01=Chongwu("常威")
d01=Dog("常威","doing")
print(d01.name)
print(d01.work)
d01.fagshou()


print(issubclass(Dog,Niao))
print(issubclass(Dog,Chongwu))
print(issubclass(Niao,Chongwu))
'''
class PatternManerge:
    def __init__(self):
        pass

    number = input("请输入几边形：")
    def Add(self,value):
       pass

class Patterning:
    def __init__(self,value):
        self.value=value

class Round(Patterning):
    def round_area(self,value):
        return 3.14*value**2

class Rectangle(Patterning):
    def rectangle_area(self,a,b):
        return a*b



