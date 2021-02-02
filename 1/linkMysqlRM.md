使用python语言做系统开发时，必不可以地需要与数据库进行数据读写操作。
在开始前，需要将Mysql的包引入到代码叫。
import pymysql
在引入mysql后，如果右侧显示红色小横条，则表示引入时报异常。需要对包先进行安装操作。
点击File->settings->project XXX->Python interpreter
在此界面找到+号，查询pymysql，进行安装。完成安装后即可进行数据后续数据库的读写操作。
1、创建数据库连接:
使用connect()连接数据库，在（）中输入数据库的地址、用户名、密码和库名称即可；
db = pymysql.connect(host="127.0.0.1",user="root",password="123456",database="ry")
2、创建数据库游标对象：
游标，你可以认为是数据表里的指针，可根据需要去指向所需的某条数据；
cursor =db.cursor()
此时，就完成了数据库的连接和数据游标的创建工作。接下来就可以执行数据库的查询操作了。
此例对数据库的操作，旨在实现将数据库中某张表里的数据全部显示出来。
在此，有三种实现方式，在实际项目中可适用的方法去使用。
使用execute() 创建执行SQL语句
cursor.execute("SELECT teacher_name,phone FROM t_info_teacher")
1）一次性显示出表中所有数据：fetchall()


2）逐条显示数据:fetchone()


3)使用for循环显示数据
