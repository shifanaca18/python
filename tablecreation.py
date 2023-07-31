import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='', database='shifana')
cur=con.cursor()
if con:
    cur.execute("CREATE TABLE MARK(NAME CHAR(20), MAL INT, MATH INT, ENG INT)")
    print("Table Create Success")