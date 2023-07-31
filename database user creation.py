import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='')
name=input("enter database name")
cur=con.cursor()
if con:
    cur.execute("CREATE DATABASE "+name)
    print("Database Create Success")