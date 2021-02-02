# 引入mysql
import pymysql

# 创建数据库连接
db = pymysql.connect(host="127.0.0.1",user="root",password="123456",database="ry")

# 创建游标对象
cursor =db.cursor()
# 创建执行SQL语句
cursor.execute("SELECT teacher_name,phone FROM t_info_teacher")

#显示所有数据
# print(cursor.fetchall())

#逐条显示数据
# one = cursor.fetchone()
# two = cursor.fetchone()
# print(one)
# print(two)

#使用for循环显示数据

#获取表内记录条数
cursor.execute("SELECT COUNT(*) FROM t_info_teacher")
num = cursor.fetchone()
cursor.execute("SELECT * FROM t_info_teacher")
for i in range(num[0]):
    msg = cursor.fetchone()
    s = str(i)
    print("第{}条数据是".format(s),msg)
