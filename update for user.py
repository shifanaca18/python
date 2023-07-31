import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
cur=con.cursor()
a=input("Find Name")
if con:
    b=input("Enter Edited Name")
    cur.execute("UPDATE MARK SET NAME='%s' WHERE NAME='%s'"%(b,a))
    bb=cur.fetchall()
    con.commit()
    print("Succesfully Updated")

