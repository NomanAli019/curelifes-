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

# droping_Table = """DROP TABLE disease_Data"""

create_table_query = """
CREATE TABLE IF NOT EXISTS disease_Data (
    Dis_id INT AUTO_INCREMENT PRIMARY KEY,
    Dis_name VARCHAR(255),
    Dis_detail LONGTEXT,
    Dis_prec LONGTEXT,
    Dis_rel_doc_spec LONGTEXT

)
"""
cursor.execute(create_table_query)
create_table_sympots = """
    CREATE TABLE IF NOT EXISTS symptoms_Data(
    Sym_id INT AUTO_INCREMENT PRIMARY KEY , 
    Sym_name VARCHAR(255),
    Sym_detail LONGTEXT,
    Sym_precaution LONGTEXT,
    Sym_disease LONGTEXT,
    Sym_Doctor LONGTEXT
    )
"""

cursor.execute(create_table_sympots)
connection.commit()
cursor.close()
connection.close()