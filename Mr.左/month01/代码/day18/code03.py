"""
为学生的学习方法，添加新的功能（打印时间）
"""
import time

def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        result= func(*args, **kwargs)
        execute_time=time.time()-start_time
        print("执行时间",execute_time)
        return result
    return wrapper

class Student:
    def __init__(self,name):
        self.name=name

    @print_execute_time
    def study(self):
        print("开始学习了")
        time.sleep(2)   #模拟学习了两秒

s01=Student("zs")
s01.study()

















