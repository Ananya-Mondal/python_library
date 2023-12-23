import mysql.connector as mydb
db=mydb.connect(host="localhost",user="root",password="Am@130304",database="newdb")
mycur=db.cursor()
'''sql="insert into table1(roll,name) values(%s,%s);"
var=(1,'jnanesh')
mycur.execute(sql,var)
sql="update table1 set name='ananya' where roll=1;"'''
sql1="select * from table1 ;"
mycur.execute(sql1)
result=mycur.fetchall()
#db.commit()
for j in result:
    print (j[0])
    
