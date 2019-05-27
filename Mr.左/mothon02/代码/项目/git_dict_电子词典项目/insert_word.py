"""
将dict.txt的单词插入列表words当中
"""
import pymysql
import re

f = open('dict.txt')
# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='dict_sql',
                     charset='utf8')
# 获取游标
cur = db.cursor()

sql = 'insert into words(word,mean) values(%s,%s)'

for line in f:
    tup = re.findall(r'(\w+)\s+(.*)', line)[0]
    try:
        # 数据操作
        cur.execute(sql, tup)
        # 将修改内容提交到数据库
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

# 关闭游标和数据库连接
cur.close()
db.cursor()
