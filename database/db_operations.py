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
 
async def insert_patient(p_first_name, p_last_name, p_date_of_birth, p_gender, p_phone_number, p_address, p_registration_date, p_medical_history, p_emergency_contact_name, p_emergency_contact_phone, p_email, p_password):
    patient_insert_query = """
    INSERT INTO patients(p_first_name, p_last_name, p_date_of_birth, p_gender, p_phone_number, p_address, p_registration_date, p_medical_history, p_emergency_contact_name, p_emergency_contact_phone, p_email, p_password)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (p_first_name, p_last_name, p_date_of_birth, p_gender, p_phone_number, p_address, p_registration_date, p_medical_history, p_emergency_contact_name, p_emergency_contact_phone, p_email, p_password)
    cursor.execute(patient_insert_query, values)
    connection.commit()
