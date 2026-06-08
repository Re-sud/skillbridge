import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password2110",
    database="skillbridge"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

for row in cursor:
    print(row)