import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='-silvana123S',
    database= 'prueba'
)

cursor = mydb.cursor()
# cursor.execute('show create table Usuario')
cursor.execute('select * from Usuario')
# sql = 'insert into Usuario(email, username, edad) values (%s, %s, %s)'
# values = ('luca@hotmail.com', 'lucatest', 20)

# cursor.execute(sql, values)

# mydb.commit()
# print(cursor.rowcount)
result = cursor.fetchall()
print(result)





