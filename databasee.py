import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
name=input("Enter Your name")
m1=int(input("Enter mark1"))
m2=int(input("Enter mark2"))
m3=int(input("enter mark3"))
cur=con.cursor()
if con:
    cur.execute("INSERT INTO MARK VALUE('%s',%s,%s,%s)"%(name ,m1,m2,m3))
    con.commit()
    print("Data added succesfully")
    
 