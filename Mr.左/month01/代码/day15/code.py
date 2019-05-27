"""
#练习１．("悟空","八戒","沙僧","唐僧")
list01=["悟空","八戒","沙僧","唐僧"]
iterator = list01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break
print("..........................................")
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
dict01={"张三丰":101,"张无忌":102,"赵敏":102}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key,dict01[key])
    except:
        break
#练习２．
class Employee:
    pass
class EmployeeIteration:
    def __init__(self, target):
        self.target = target
        self.index = 0
    def __next__(self):
        # 如果索引越界　则抛出异常
        if self.index > len(self.target) - 1:
            raise StopIteration()
        # 返回下一个元素
        item = self.target[self.index]
        self.index += 1
        return item
class EmployeeManager:
    def __init__(self,employees):
        self.all_employee=employees
    def __iter__(self):
        return EmployeeIteration(self.all_employee)

manager=EmployeeManager([Employee(),Employee()])
for item in manager:
    print(item)
"""
class MyRangeManagor:
    def __init__(self, stop):
        self.stop= stop
        self.star=0
    def __next__(self):
        if self.star+1 > self.stop:
            raise StopIteration()
        temp=self.star
        self.star+=1
        return temp
class MyRange:
    def __init__(self,stop):
        self.stop=stop

    def __iter__(self):
        return MyRangeManagor(self.stop)

# for item in range(5):
#     print(item)

for item in MyRange(5):
    print(item)




























