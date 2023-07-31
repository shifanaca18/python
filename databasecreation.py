import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='')
cur=con.cursor()
if con:
    cur.execute("CREATE DATABASE HAI")
    print("Database Create Success")