def get_score():
    while True:
        try:
           number=int(input("请输入成绩："))
        except:
            print("输入有误")
            continue
        return number

get_score()

