class Student:
    def __init__(self, name, sex, age, score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score

    def __str__(self):
        return "%s--%s--%d--%d" % (self.name,self.sex ,self.age,self.score)

list_stu = [Student("张无忌", "男",28,90),
            Student("赵敏", "女", 25, 98),
            Student("周芷若", "女", 26, 89)]


def get_sex(target):
    for item in target:
        if item.sex == "女":
            yield item



iter01=get_sex(list_stu)
for item in iter01:
    print(item)

# def get_score(target):
#     for item in target:
#         if item.score >= "90":
#             yield item
#
#
# iter01 = get_score(list_stu)
# for item in iter01:
#     print(item)
