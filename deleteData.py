import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password12345678_PSW',
    database= 'prueba'
)

cursor = mydb.cursor()

sql = 'delete from Usuario where id = %s'

values = (2, )

cursor.execute(sql, values)

mydb.commit()

print('deleted')




