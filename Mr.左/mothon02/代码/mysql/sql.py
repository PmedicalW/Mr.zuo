"""
sql语句传参练习
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu', # 数据库名
                     charset='utf8')
# 创建游标
cur=db.cursor()

while True:   # 手动输入
    name = input("Name:")
    age = input("Age:")
    genden = input("m or w:")
    score = input("Score:")

    # sql = "insert into class_1 (name,age,genden,score) values (%s,%d,%s,%f);"%(name,age,genden,score)
    sql = "insert into class_1(name,age,genden,score) values(%s,%s,%s,%s);"

    print(sql)
    try:
        # cur.execute(sql)
        # db.commit()
        cur.execute(sql,[name,age,genden,score])# 通过列表自动把手动输入的数据传入表中
        db.commit()

    except Exception as e:
        db.rollback()  # 失败回滚到操作之前的状态
        print("Faild:",e)
    else:
        print('添加成功')

cur.close()
db.close()