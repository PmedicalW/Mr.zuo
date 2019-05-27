"""
二进制文件存储
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

# # 向数据库中存储文件
# with open('/home/tarena/图片/個人壁纸/mysql.jpg','rb') as fd:
#     data_数据结构 = fd.read()
#
# try:
#     sql = "insert into Images values(1,'mysql.jpg',%s);"
#     cur.execute(sql,[data_数据结构])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)
# else:
#     print("存储成功")


# 获取文件
sql = "select * from Images where filename='mysql.jpg';"

cur.execute(sql)
image = cur.fetchone()
with open(image[1], 'wb') as fd:# image[1]用的是数据库原有的文件名字 　　列表：[1,图片.jpg,data_数据结构]
    fd.write(image[2])

cur.close()
db.close()
