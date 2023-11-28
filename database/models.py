import mysql.connector
host = "127.0.0.1"
user = "root"
password = "root"
database_name = "curelifedb"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database_name
)

cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS disease_Data (
    Dis_id INT AUTO_INCREMENT PRIMARY KEY,
    Dis_name VARCHAR(255),
    Dis_detail VARCHAR(255),
    Dis_prec VARCHAR(255),
    Dis_rel_doc_spec VARCHAR(255)

)
"""
cursor.execute(create_table_query)
connection.commit()
cursor.close()
connection.close()