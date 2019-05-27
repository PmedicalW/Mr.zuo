import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='wangzherongyao',
                     charset='utf8')

# 获取游标
cur=db.cursor()

# 数据操作
cur.execute("insert into data_数据结构 values(5,'兰陵王','m','刺客',10,'致命一击');")

# 将修改内容提交到数据库
db.commit()

# 关闭游标和数据库连接
cur.close()
db.cursor()















