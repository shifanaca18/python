import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
cur=con.cursor()
print(1,"INSERT",2,"DELETE",3,"DISPLAY",4,'UPDATE')
n=int(input("Enter a number"))
def insert():
    if n==1:
        name=input("Enter Your name")
        m1=int(input("Enter mark1"))
        m2=int(input("Enter mark2"))
        m3=int(input("enter mark3"))
        cur.execute("INSERT INTO MARK VALUE('%s',%s,%s,%s)"%(name ,m1,m2,m3))
        con.commit()
        print("Data added succesfully")
def delete():
    if n==2:
        a=input("enter a name")
        cur.execute("DELETE FROM MARK WHERE NAME='%s'" %a) 
        con.commit()
        print("Deleted Successfully") 
def display():
    if n==3:
        c=input("enter a name")
        cur.execute("SELECT * FROM MARK where name='%s'"%c)
        data=cur.fetchall()
        for a in data:
            print(a)
def update():
    if n==4:
        a=input("Find a name")
        b=input("Enter Edited Name")
        cur.execute("UPDATE MARK SET NAME='%s' WHERE NAME='%s'"%(b,a))
        cur.execute("SELECT * FROM MARK")
        bb=cur.fetchall()
        con.commit()
        print("Succesfully Updated")    
insert()
delete()
display()
update()
