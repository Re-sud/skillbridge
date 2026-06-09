import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password2110",
    database="skillbridge"
)

cursor = connection.cursor()

name = input("Enter name: ")
email = input("Enter email: ")
password = input("Enter password: ")

query = """
INSERT INTO students(name,email,password)
VALUES(%s,%s,%s)
"""

values = (name, email, password)

cursor.execute(query, values)

connection.commit()

print("Student added successfully!")