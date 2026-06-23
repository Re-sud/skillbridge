import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Use a buffered cursor so previous SELECT results are consumed
# and `mysql.connector.errors.InternalError: Unread result found` is avoided.
cursor = connection.cursor(buffered=True)

print("Database Connected!")