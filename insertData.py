import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password12345678_PSW',
    database= 'prueba'
)

cursor = mydb.cursor()
sql = 'insert into Usuario(email, username, edad) values (%s, %s, %s)'
values = ('luca@hotmail.com', 'lucatest', 20)

cursor.execute(sql, values)

mydb.commit()
print(cursor.rowcount)