"""
数据库读操作
select
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

sql = "select * from class_1 where age >= 19;"

# 执行语句  cur拥有查询结果
cur.execute(sql)

# 获取查找结果第一个
one_row = cur.fetchone()
print(one_row)  # (1, '老杜', 33, 'w', 59.5)

# 获取查找结果前n个
many_row = cur.fetchmany(2)
print(many_row)  # ((1, '老杜', 33, 'w', 59.5), (2, '左哥', 20, 'm', 99.0))

# 获取所有查找结果
all_row = cur.fetchall()
print(all_row)
# ((1, '老杜', 33, 'w', 59.5),
# (2, '左哥', 20, 'm', 99.0),
# (3, '老徐', 19, 'm', 88.0),
# (10, 'Lily', 22, 'w', 75.5))

cur.close()
db.close()
