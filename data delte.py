import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
cur=con.cursor()

if con:
    a=input("enter a name")
    cur.execute("DELETE FROM MARK WHERE NAME='%s'" %a) 
    con.commit()
    print("Deleted Successfully")   