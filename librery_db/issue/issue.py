from datetime import date
from datetime import timedelta
import mysql.connector as mydb
class issue:
    def opendb(self):
        self.__db=mydb.connect(host="localhost",user="root",password="Am@130304",database="newdb")
        self.__mycur=self.__db.cursor()
        
    def closedb(self):
        self.__mycur.close()
        self.__db.close()
        
    def issue(self,rn,bn):
        self.opendb()
        issdt=date.today()
        rtdt=issdt+timedelta(days=7)
       

        sql="Select Available from book where bookid =%s"
        var=(bn,)
        self.__mycur.execute(sql,var)
        res=self.__mycur.fetchone()
        
        if res[0]>0:
            sql="insert into issue(rollno,bookid,issuedate,returndate) values(%s,%s,%s,%s);"
            var=(rn,bn,issdt,rtdt)
            self.__mycur.execute(sql,var)
            self.__db.commit()
            if self.__mycur.rowcount>0:
                sql="update book set Available=Available-1 where bookid =%s"
                var=(bn,)
                self.__mycur.execute(sql,var)
                self.__db.commit()
                print("Issued Successful")
        else:
            print("Book is not available now")
            
        self.closedb()
       
            
    def search(self,rn,bn):
        self.opendb()
        sql="Select * from issue where 5=5 "
        var=()
        if rn>0:
            sql+=" and rollno =%s"
            var=var+(rn,)
        if bn>0:
            sql+=" and bookid =%s"
            var=var+(bn,)
            
        
        self.__mycur.execute(sql,var)
        res=self.__mycur.fetchall()
        self.closedb()
        return res
         
       
    def bookreturn(self,rn,bn):
        self.opendb()
        csdt=date.today()
        fine=0
             

        sql="Select returndate from issue where rollno=%s and bookid=%s;"
        var=(rn,bn)
        self.__mycur.execute(sql,var)
        res=self.__mycur.fetchone()
        
        if len(res)>0:
            deff=csdt-res[0]
            d=deff.days
            if d>0:
                fine=d*5
                print("You got a fine of Rs {}".format(fine))
                
            sql="delete from issue where rollno=%s and bookid=%s;"
            var=(rn,bn)
            self.__mycur.execute(sql,var)
            
            self.__db.commit()
            if self.__mycur.rowcount>0:
                sql="update book set Available=Available+1 where bookid =%s;"
                var=(bn,)
                self.__mycur.execute(sql,var)
               
                self.__db.commit()
                print("Returned Successful")
        else:
            print("no book issued")
       
        self.closedb()
    
    
    
