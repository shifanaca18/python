import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
cur=con.cursor()
a=input("enter a name")
if con:
    cur.execute("SELECT * FROM MARK WHERE NAME='%s'" %a)
    b=cur.fetchall()
    for a in b:
        print("Name ",a[0])