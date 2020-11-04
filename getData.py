import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password12345678_PSW',
    database= 'prueba'
)

cursor = mydb.cursor()
# with all data
cursor.execute('select * from Usuario')

# whit limit users
cursor.execute('select * from Usuario limit 1')

result = cursor.fetchall()
print(result)