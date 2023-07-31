import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
cur=con.cursor()
n=input("enter a name")
if con:
    cur.execute("SELECT * FROM MARK where name='%s'"%n)
    data=cur.fetchall()
    for a in data:
        print(a)


