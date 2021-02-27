import mysql.connector as sqltor
mydb=sqltor.connect(host='localhost',user='root',passwd='root',database='main')
cursor=mydb.cursor()
