import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm_db")

print("Database created successfully.")