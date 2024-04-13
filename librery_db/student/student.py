import mysql.connector as mydb

class student:
    def opendb(self):
        self.__db=mydb.connect(host="localhost",user="root",password="Am@130304",database="newdb")
        self.__mycur=self.__db.cursor()
        
    def closedb(self):
        self.__mycur.close()
        self.__db.close()
        
    def entry(self,r,n):
        self.opendb()
        sql="Select count(*) from students where roll=%s"
        var=(r,)
        self.__mycur.execute(sql,var)
        res=self.__mycur.fetchone()
        if res[0]==0:
            sql="insert into students(roll,name) values(%s,%s);"
            var=(r,n)
            self.__mycur.execute(sql,var)
            self.__db.commit()
            if self.__mycur.rowcount>0:
                print("Added Successful")
        else:
            print("Student alreday exsit")
            
        self.closedb()

    def display(self):
        self.opendb()
        sql="select * from students ;"
        self.__mycur.execute(sql)
        result=self.__mycur.fetchall()
        self.closedb()
        return result
    def search(self,r):
        self.opendb()
        sql="select * from students where roll=%s;"
        var=(r,)
        self.__mycur.execute(sql,var)
        result=self.__mycur.fetchall()
        self.closedb()
        return result
    def update(self,n,r):
        self.opendb()
        sql="update students set name=%s where roll=%s;"
        var=(n,r)
        self.__mycur.execute(sql,var)
        self.__db.commit()
        if self.__mycur.rowcount>0:
            print("Successfuly Updated")
        else:
            print("Roll no not found re enter your correct roll...")
        self.closedb()
    def delete(self,r):
        self.opendb()
        sql="delete FROM students where roll=%s;"
        var=(r,)
        self.__mycur.execute(sql,var)
        self.__db.commit()
        if self.__mycur.rowcount>0:
            print("Successfuly deleted")
        else:
            print("Roll no not found re enter your correct roll...")
        self.closedb()
