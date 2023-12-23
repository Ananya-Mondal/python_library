import student.student as stmaster
import book.book as btmaster
import issue.issue as isu
def main():
    i=1
    
    
    a=stmaster.student()
    b=btmaster.book()
    iss=isu.issue()
    
    while(i>0):
        
        print ("1> student")
        print ("2> book")
        print ("3> issue return ")
        print ("4> exit")
        n=int(input("Enter your choice"))
        if n==1:
            while(i>0):
                
                print ("1) add student")
                print ("2) update student")
                print ("3) del student")
                print ("4) search student")
                print ("5) all student")
                print ("6) back to main")
                n1=int(input("Enter your choice"))
                if n1==1:
                    name=input("Enter a Name")
                    roll=int(input("Enter a Roll no"))
                    a.entry(roll,name)
                elif n1==2:
                    rollc=int(input("Enter roll no"))
                    name=input("Enter a Name")
                    a.update(name,rollc)
                    
                elif n1==3:
                    rollc=int(input("Enter roll no"))
                    a.delete(rollc)
                    
                elif n1==4:
                    rollc=int(input("Enter roll no"))
                    rr=a.search(rollc)
                    if len(rr)>0:
                        print("Name={} Roll={}".format(rr[0][1],rr[0][0]))
                    else:
                        print("Not found")
                elif n1==5:
                    rr=a.display()
                    for k in rr:
                        print("Name={} Roll={}".format(k[1],k[0]))
                elif n1==6:
                    break
                else:
                    print ("invalide input , reinput your choice :")
        elif n==2:
            while(i>0):
                
                print ("1) add book")
                print ("2) update book")
                print ("3) del book")
                print ("4) search book")
                print ("5) all book")
                print ("6) back to main")
                n2=int(input("Enter your choice"))
                if n2==1:
                    bid=int(input("Enter Book Id:"))
                    bname=input("Enter a Book Name")
                    aname=input("Enter author Name")
                    nob=int(input("Enter no of Book"))
                    b.entry(bid,bname,aname,nob)
                elif n2==2:
                    bid=int(input("Enter Book Id:"))
                    bname=input("Enter a Book Name")
                    aname=input("Enter author Name")
                    nob=int(input("Enter no of Book"))
                    b.update(bid,bname,aname,nob)
                    
                elif n2==3:
                    rollc=int(input("Enter Book Id"))
                    b.delete(rollc)
                elif n2==4:
                    rollc=int(input("Enter Book ID"))
                    rr=b.search(rollc)
                    if len(rr)>0:       
                        for k in rr:
                            print("Book Name={} Book Id={} Book Author name ={} Quantity ={} Available Quantity ={}".format(k[1],k[0],k[2],k[3],k[4]))
                    else:
                        print("No record found")
                elif n2==5:
                    rr=b.display()
                    if len(rr)>0:       
                        for k in rr:
                            print("Book Name={} Book Id={} Book Author name ={} Quantity ={} Available Quantity ={}".format(k[1],k[0],k[2],k[3],k[4]))
                    else:
                        print("No record found")
                elif n2==6:
                    break
                else:
                    print ("invalide input , reinput your choice :")
        elif n==3:
            while(i>0):
                
                print ("1) issue book")
                print ("2) return book")
                print ("3) issued book")
                print ("4) back to main")
                n3=int(input("Enter your choice"))
                if n3==1:
                    aresure='N'
                    aresurebook='N'
                    rollc=0
                    booknn=0
                    while(aresure!='Y'):
                        rollc=int(input("Enter roll no"))
                        rr=a.search(rollc)
                        if len(rr)>0:
                            print("Name={} Roll={}".format(rr[0][1],rr[0][0]))
                        else:
                            print("No record found")    
                        aresure=input("Are you Sure?(Y/N):")
                        
                    while(aresurebook!='Y'):
                        booknn=int(input("Enter Book ID"))
                        rr=b.search(booknn)
                        
                        if len(rr)>0:       
                            for k in rr:
                                print("Book Name={} Book Id={} Book Author name ={} Quantity ={} Available Quantity ={}".format(k[1],k[0],k[2],k[3],k[4]))
                        else:
                            print("No record found")
                        aresurebook=input("Are you Sure?(Y/N):")
                        
                    if rollc>0 and booknn>0:
                        iss.issue(rollc,booknn)
                       
                    else:
                        print("Unable to issue")
                        
                    
                    
                    
                elif n3==2:
                    aresure='N'
                    aresurebook='N'
                    rollc=0
                    booknn=0
                    while(aresure!='Y'):
                        rollc=int(input("Enter roll no"))
                        rr=a.search(rollc)
                        if len(rr)>0:
                            print("Name={} Roll={}".format(rr[0][1],rr[0][0]))
                        else:
                            print("No record found")    
                        aresure=input("Are you Sure?(Y/N):")
                        
                    while(aresurebook!='Y'):
                        booknn=int(input("Enter Book ID"))
                        rr=b.search(booknn)
                        
                        if len(rr)>0:       
                            for k in rr:
                                print("Book Name={} Book Id={} Book Author name ={} Quantity ={} Available Quantity ={}".format(k[1],k[0],k[2],k[3],k[4]))
                        else:
                            print("No record found")
                        aresurebook=input("Are you Sure?(Y/N):")
                        
                    if rollc>0 and booknn>0:
                        iss.bookreturn(rollc,booknn)
                       
                    else:
                        print("Unable to return")
                elif n3==3:
                    rollc=int(input("Enter roll no"))
                    booknn=int(input("Enter Book ID"))
                    rr=iss.search(rollc,booknn)
                    if len(rr)>0:       
                        for k in rr:
                            print("Rollno={} Book Id={} Issue date ={} Return date ={}".format(k[1],k[2],k[3],k[4]))
                    else:
                        print("No record found")
                    
                elif n3==4:
                    break
                else:
                    print ("invalide input , reinput your choice :")
        elif n==4:
            break
        else:
            print ("invalide input , reinput your choice :")
            
if __name__=="__main__":
    main()
