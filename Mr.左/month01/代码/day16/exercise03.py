# 　将不变的部分提取到find_all中，将变化的提取到一个方法中
class SkillManager:
    def __init__(self, id, name, time, atk, mp):
        self.id = id
        self.name = name
        self.time = time
        self.atk = atk
        self.mp = mp

    def __str__(self):
        return "%d--%s--%d--%d--%d" % (self.id, self.name, self.time, self.atk, self.mp)
# －－－－－－－－－－－－－－－测试------------------------------
skill_list = [SkillManager(100, "降龙十八掌", 0, 11, 30),
              SkillManager(101, "九阴白骨爪", 7, 12, 0),
              SkillManager(103, "般若功", 6, 7, 35),
              SkillManager(102, "逍遥普攻", 0, 3, 40),
              SkillManager(104, "逍遥剑法", 5, 9, 40)]
# 相同点
def find_all(target, func):
    for item in target:
        if func(item):
            yield item

# # 不同点
# def get_id(item):
#     return item.id == 101
#
# def get_time(item):
#     return item.time == 0
#
# def get_atk(item):
#     return item.atk >= 5
#
# def get_atk_mp(item):
#     return item.atk >= 10 and item.mp == 0

for item in find_all(skill_list, lambda item:item.id==101):
    print(item)

for item in find_all(skill_list, lambda item:item.time==0):
    print(item)

for item in find_all(skill_list, lambda item: item.atk >= 5):
    print(item)

for item in find_all(skill_list, lambda item: item.atk >10 and item.mp==0):
    print(item)

for item in find_all(skill_list, lambda item: item == 0):
    print(item)