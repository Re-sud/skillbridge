import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password2110",
    database="skillbridge"
)

cursor = connection.cursor()

print("Database Connected!")