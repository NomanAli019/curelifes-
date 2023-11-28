import mysql.connector
host = "127.0.0.1"
user = "root"
password = "root"
database_name = "curelifedb"

connection = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database_name
)
cursor = connection.cursor()

