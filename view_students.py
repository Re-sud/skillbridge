import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password2110",
    database="skillbridge"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()


for student in students:
     print("ID:", student[0])
     print("Name:", student[1])
     print("Email:", student[2])
     print("Password:", student[3])
     print()
   