# day15 作业
# １．创建技能类(编号，技能名称，冷却时间，攻击力，消耗法力)
# 　　创建技能列表．
# 　　－－　定义函数：查找编号是１０１的技能对象
# 　　－－　定义函数：查找冷却时间为０的所有技能对象
# 　　－－　定义函数：查找攻击力大于５的所有技能对象
# 　　－－　定义函数：查找攻击力大于１０，并且不需要消耗法力的所有技能．
#
class SkillManager:
    def __init__(self,id,name,time,atk,mp):
        self.id=id
        self.name=name
        self.time=time
        self.atk=atk
        self.mp=mp

    def __str__(self):
        return "%d--%s--%d--%d--%d" % (self.id,self.name, self.time ,self.atk, self.mp)
#－－－－－－－－－－－－－－－测试------------------------------
skill_list=[SkillManager(100,"降龙十八掌",0,11,30),
            SkillManager(101,"九阴白骨爪",7,12,0),
            SkillManager(103,"般若功",6,7,35),
            SkillManager(102,"逍遥普攻",0,3,40),
            SkillManager(104,"逍遥剑法",5,9,40)]

def get_id(target):
    for item in target:
        if item.id == 101:
            yield item


def get_time(target):
    for item in target:
        if item.time == 0:
            yield item

def get_atk(target):
    for item in target:
        if item.atk>= 5:
            yield item

def get_atk_mp(target):
    for item in target:
        if item.atk>= 10 and item.mp==0:
            yield item

for item in get_id(skill_list):
            print("编号是１０１的技能对象:",item)


for item in get_time(skill_list):
            print("冷却时间为０的所有技能对象:",item)


for item in get_atk(skill_list):
            print("攻击力大于５的所有技能对象:",item)

for item in get_atk_mp(skill_list):
            print("攻击力大于１０，并且不需要消耗法力的所有技能:",item)































