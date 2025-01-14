import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "43.201.113.85",
    "port": 3306,
    "user": "ubuntu",
    "password": "0910",
    "database": "polyglot_db"
}

try:
    connection = mysql.connector.connect(**DB_CONFIG)
    if connection.is_connected():
        print("Successfully connected to the database")
    else:
        print("Connection failed")
except Error as e:
    print(f"Error: {e}")
finally:
    if connection and connection.is_connected():
        connection.close()
