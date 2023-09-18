import pymysql
HOST="localhost"
USER="root"
PW="8787521"
DATABASE_NAME="hzs"
try:
    db=pymysql.connect(host=HOST,user=USER,password=PW,database=DATABASE_NAME)
    print("connect to database successfully!")
    yb=db.cursor()
    '''创建表操作：'''
    # yb.execute("DROP TABLE IF EXISTS student")
    # sql_create="CREATE TABLE student(sno CHAR(20) PRIMARY KEY NOT NULL,name CHAR(20),sex CHAR(2),age INT)"
    # yb.execute(sql_create)
    # yb.execute("DROP TABLE IF EXISTS course")
    # sql_create="CREATE TABLE coursel(cno CHAR(20) PRIMARY KEY NOT NULL,cname CHAR(40) NOT NULL,credit SMALLINT);"
    # yb.execute(sql_create)
    # yb.execute("DROP TABLE IF EXISTS sc")
    # sql_create="CREATE TABLE sc(sno CHAR(20),cno CHAR(20),GRADE SMALLINT,PRIMARY KEY(sno,cno),FOREIGN KEY(sno) REFERENCES student(sno),FOREIGN KEY(cno) REFERENCES course(cno))"
    # yb.execute(sql_create)
    # print("create table sc successfully!")
    '''修改表：'''
    # sql_change='ALTER TABLE coursel RENAME TO course'
    # yb.execute(sql_change)
    # print('修改表名成功')
    '''插入操作：'''
    # sql_insert="INSERT INTO student(sno,name,sex,age) VALUES(%s,%s,%s,%s)"
    # value=('231121','李四','女',21)
    # yb.execute(sql_insert,value)
    # db.commit()
    '''修改操作：'''
    # sql_change='UPDATE student SET name=%s WHERE sno=%s'
    # value=('刘二','202111104114')
    # yb.execute(sql_change,value)
    # db.commit()
    '''删除操作：'''
    # sql_delete="DELETE FROM student WHERE sno=%s"
    # value=('2021')
    # yb.execute(sql_delete,value)
    # db.commit()
    '''查询操作：'''
    # sql_query="SELECT * FROM student"
    # yb.execute(sql_query)
    # results=yb.fetchall()
    # for i in results:
    #     sno=i[0]
    #     name=i[1]
    #     sex=i[2]
    #     age=i[3]
    #     print("学号：%s 姓名：%s 性别：%s 年龄：%d" % (sno,name,sex,age))
#     for i in range(5):
#         value=tuple(input().split())
#         sql_insert='INSERT INTO sc(sno,cno,GRADE) VALUES(%s,%s,%s)'
#         yb.execute(sql_insert,value)
#         db.commit()
#     print("insert data successfully!")
# except pymysql.Error as e:
#     print("operate database unsuccessfully! error: "+str(e))
#     db.rollback()