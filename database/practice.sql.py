import pymysql
HOST='127.0.0.1'
USER='root'
PASSWORD='8787521'
DATA_BASE='test'
try:
    db=pymysql.connect(host=HOST,user=USER,password=PASSWORD,database=DATA_BASE)
    print("connect to mysql database successfully!")
    yb=db.cursor()
    sql_insert='INSERT INTO sc(sno,cno,grade) values(%s,%s,%s)'
    for _ in range(6):
        value=tuple(input().split())
        yb.execute(sql_insert,value)
        db.commit()
        print('insert data successfully!')
    print("insert  data completion!")
except pymysql.Error as e:
    print('failed to operate to mysql database! error: '+str(e))
    db.rollback()
yb.close()
db.close()
