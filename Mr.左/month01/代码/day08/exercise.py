'''
#创建２个类，２个对象
class Handsome_boy():
    """
    帅哥
    """
    def __init__(self,name="",sex="",height=0):
        self.name=name
        self.sex=sex
        self.height=height

    def work(self):
        print("IT")

h01=Handsome_boy("A","男",170)
print(id(h01))
h01.work()
h02=Handsome_boy("B","男",160)
print(id(h02))
h02.work()

'''
# 创建学生类
#    －－　数据：姓名，性别，年龄，成绩．
#    －－　行为：print_self()
# 画出学生列表内存图
#   定义函数：
#        －－　定义函数，在学生列表中，根据姓名查找学生对象．
#        －－　定义函数，在学生列表中，根据性别查找所有学生对象．
#        －－　查找年龄大于20，成绩大于60的所有学生对象．


class Student:
    """
    学生
    """
    def __init__(self,name="",sex="",age=0,score=0):
        self.name = name
        self.sex=sex
        self.age = age
        self.score=score

    def print_self(self):
        print(self.name,self.sex,self.age,self.score)

s01=Student("A","男",18,90)
s01.print_self()
s02=Student("B","女",22,90)
s02.print_self()







