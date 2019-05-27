"""
数据库写操作
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')

# 创建游标
cur = db.cursor()

try:
    # 插入操作
    sql = "insert into interest values(5,'Lily','sing','A','9999','优秀');"
    cur.execute(sql)

    # 修改操作
    sql = "update interest set price=8686 where name = 'Jam';"
    cur.execute(sql)

    # 删除操作
    sql = "delete from class_1 where id > 7;"
    cur.execute(sql)

    db.commit()

except Exception as e:
    db.rollback()
    print(e)
else:
    print("操作成功")

cur.close()
db.close()
