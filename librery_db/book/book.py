import mysql.connector as mydb
class book:
    aquantity=0
    
    def opendb(self):
        self.__db=mydb.connect(host="localhost",user="root",password="Am@130304",database="newdb")
        self.__mycur=self.__db.cursor()
        
    def closedb(self):
        self.__mycur.close()
        self.__db.close()
    
    def entry(self,bi,bn,an,nb):
        self.opendb()
        sql="Select count(*) from book where bookid=%s"
        var=(bi,)
        self.__mycur.execute(sql,var)
        res=self.__mycur.fetchone()
        
        if res[0]==0:
            self.aquantity +=nb
            sql="insert into book(bookid,bookname,AuthorName,noofBook,Available) values(%s,%s,%s,%s,%s);"
            var=(bi,bn,an,nb,self.aquantity)
            self.__mycur.execute(sql,var)
            self.__db.commit()
            if self.__mycur.rowcount>0:
                print("Added Successful")
        else:
            print("Book alreday exsit")
        self.closedb()
        
        
    def display(self):
        self.opendb()
        sql="select * from book ;"
        self.__mycur.execute(sql)
        result=self.__mycur.fetchall()
        self.closedb()
        return result
    def search(self,k):
        self.opendb()
        
        sql="select * from book where bookid=%s;"
        var=(k,)
        self.__mycur.execute(sql,var)
        result=self.__mycur.fetchall()
        self.closedb()
        return result
        
        
    def update(self,bi,bn,an,nb,ab=0):
        self.opendb()
        var=(nb,)
        sql="update book set noofBook=noofBook+%s "
        if nb!=0:
            ab=nb
        if ab!=0:
            sql+=" ,Available=Available+%s"
            var = var + (ab,)
        if bn!="":
            sql+=" ,bookname=%s"
            var = var + (bn,)
        if an!="":
            sql+=" ,AuthorName=%s"
            var = var + (an,)
        
            
        sql +=" where bookid=%s;"
        var = var + (bi,)
        
        self.__mycur.execute(sql,var)
        self.__db.commit()
        if self.__mycur.rowcount>0:
            print("Successfuly Updated")
        else:
            print("Book id not found re enter your correct roll...")
        self.closedb()
        
    def delete(self,r):
        self.opendb()
        sql="delete FROM book where bookid=%s;"
        var=(r,)
        self.__mycur.execute(sql,var)
        self.__db.commit()
        if self.__mycur.rowcount>0:
            print("Successfuly deleted")
        else:
            print("Book no not found re enter your correct roll...")
        self.closedb()
