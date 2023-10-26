import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '9669'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE CRM')

print("All Done!")