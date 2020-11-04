import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password12345678_PSW',
    database= 'prueba'
)

cursor = mydb.cursor()

sql = 'update Usuario set email = %s where id = %s'

values = ('newupdate@email.com', 4)

cursor.execute(sql, values)

mydb.commit()

print(cursor.rowcount)