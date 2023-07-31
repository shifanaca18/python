import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
cur=con.cursor()

if con:
    cur.execute("UPDATE MARK SET NAME='Anju' WHERE NAME='ammu'") 
    con.commit()
    print("Succesfully Updated")

