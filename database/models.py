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

# droping_Table = """DROP TABLE doctors"""

# create_table_query = """
# CREATE TABLE IF NOT EXISTS disease_Data (
#     Dis_id INT AUTO_INCREMENT PRIMARY KEY,
#     Dis_name VARCHAR(255),
#     Dis_detail LONGTEXT,
#     Dis_prec LONGTEXT,
#     Dis_rel_doc_spec LONGTEXT

# )
# """
# cursor.execute(create_table_query)
# create_table_sympots = """
#     CREATE TABLE IF NOT EXISTS symptoms_Data(
#     Sym_id INT AUTO_INCREMENT PRIMARY KEY , 
#     Sym_name VARCHAR(255),
#     Sym_detail LONGTEXT,
#     Sym_precaution LONGTEXT,
#     Sym_disease LONGTEXT,
#     Sym_Doctor LONGTEXT
#     )
# """



#  """

# CREATE TABLE IF NOT EXISTS doc_online_booking (
#     online_booking_id INT AUTO_INCREMENT PRIMARY KEY,
#     doctor_id INT,
#     d_online_fee INT,
#     d_online_days TEXT,
#     d_online_time TIME 
# );


# """

# boooking = """
# CREATE TABLE IF NOT EXISTS patients (
#     patient_id INT AUTO_INCREMENT PRIMARY KEY,
#     p_first_name VARCHAR(50) NOT NULL,
#     p_last_name VARCHAR(50) NOT NULL,
#     p_date_of_birth DATE NOT NULL,
#     p_gender VARCHAR(50) NOT NULL,
#     p_phone_number VARCHAR(20),
#     p_address VARCHAR(255),
#     p_registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     p_medical_history TEXT,
#     p_emergency_contact_name VARCHAR(100),
#     p_emergency_contact_phone VARCHAR(20),
#     p_email VARCHAR(100) UNIQUE,
#     p_password VARCHAR(10)
# );


#     CREATE TABLE IF NOT EXISTS doc_onsite_booking (
#     onsite_booking_id INT AUTO_INCREMENT PRIMARY KEY,
#     doctor_id INT,
#     d_onsite_fee INT,
#     d_onsite_days TEXT,
#     d_onsite_loc VARCHAR(255),
#     d_onsite_time TIME
# );
# CREATE TABLE Doc_profile(
# d_profile_id INT PRIMARY KEY AUTO_INCREMENT, 
# doc_id INT ,
# doc_profile_img LONGBLOB,
# doc_email VARCHAR(255)
# )
# CREATE TABLE doc_max_booking(
# booking_limit_id INT PRIMARY KEY AUTO_INCREMENT,
# d_id INT,
# onsite_booking_limit INT,
# online_booking_limit INT
# )
# """

# Rest of your code remains unchanged


query  = """
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    d_first_name VARCHAR(50) NOT NULL,
    d_last_name VARCHAR(50) NOT NULL,
    d_date_of_birth DATE NOT NULL,
    d_gender VARCHAR(50) NOT NULL,
    d_phone_number VARCHAR(20),
    d_address VARCHAR(255),
    d_registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    d_specialization VARCHAR(100) NOT NULL,
    d_license_number VARCHAR(20) UNIQUE,
    d_hospital_affiliation VARCHAR(255),
    d_experience_years INT,
    d_email VARCHAR(100) UNIQUE,
    d_password VARCHAR(10) -- Removed the extra comma
);

"""
cursor.execute(query)

connection.commit()


cursor.close()
connection.close()