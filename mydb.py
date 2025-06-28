import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE Matrix")

print("All Done! :)")