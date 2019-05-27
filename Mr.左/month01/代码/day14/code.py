def get_score():
    while True:
        try:
           number=int(input("请输入成绩："))
        except:
            print("输入有误")
            continue
        if 1<=number<=100:
            return number
        print("成绩不在范围内")

get_score()












