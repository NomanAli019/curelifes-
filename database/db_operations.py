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
cursor =  connection.cursor()
 
async def insert_patient(p_first_name, p_last_name, p_date_of_birth, p_gender, p_phone_number, p_address, p_registration_date, p_medical_history, p_emergency_contact_name, p_emergency_contact_phone, p_email, p_password):
    check_user_existance_query = f"Select * from patients where p_email = {p_email}"
    cursor.execute(check_user_existance_query)
    result = cursor.fetchone()
    if result:
        print("user already exists")
    else:
        patient_insert_query = """
        INSERT INTO patients(p_first_name, p_last_name, p_date_of_birth, p_gender, p_phone_number, p_address, p_registration_date, p_medical_history, p_emergency_contact_name, p_emergency_contact_phone, p_email, p_password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (p_first_name, p_last_name, p_date_of_birth, p_gender, p_phone_number, p_address, p_registration_date, p_medical_history, p_emergency_contact_name, p_emergency_contact_phone, p_email, p_password)
        cursor.execute(patient_insert_query, values)
        connection.commit()

async def insert_doctor(doctor_list):
    print(doctor_list)
    doctor_insert_query = """
        INSERT INTO doctors(d_first_name, d_last_name, d_date_of_birth, d_gender,
                           d_phone_number, d_address, d_registration_date,
                           d_specialization, d_degree,  d_license_number, d_hospital_affiliation,
                           d_experience_years, d_email, d_password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """

    values = (
        doctor_list[0], doctor_list[1], doctor_list[2], doctor_list[3],
        doctor_list[4], doctor_list[5].lower(), doctor_list[6], doctor_list[7].lower(),
        doctor_list[8], doctor_list[9], doctor_list[10], doctor_list[11],
        doctor_list[12],doctor_list[13]
    )
    cursor.execute(doctor_insert_query, values)
    connection.commit()

async def set_doctor_booking(doc_id , d_onlinefee ,days,time ):
    query_to_enteronlinebookingtime = """
                    INSERT INTO doc_online_booking(doctor_id,d_online_fee,d_online_days,d_online_time)
                    VALUES(%s,%s,%s,%s )"""
    values = (doc_id, d_onlinefee, days,time)
    cursor.execute(query_to_enteronlinebookingtime, values)
    connection.commit()

async def set_doctor_offlinebooking(doc_id , d_offlinefee , days, locat, time):
    query_to_enterofflinebooking = """
                    INSERT INTO doc_onsite_booking(doctor_id,d_onsite_fee,d_onsite_days,d_onsite_loc,d_onsite_time)
                    VALUES(%s,%s,%s,%s,%s)"""
    values = (doc_id, d_offlinefee , days , locat,time)
    cursor.execute(query_to_enterofflinebooking , values)
    connection.commit()


async def get_doctors(city,specilization):
    queryto_get_doc = f"""
                Select * from doctors 
                where d_address = %s AND d_specialization = %s;
                """
    values = (city,specilization)
    cursor.execute(queryto_get_doc,values)
    result = cursor.fetchall()
    return result

async def get_online_docbooking(doc_id):
    doc_id = int(doc_id)
    query = """Select * from doc_online_booking
            where doctor_id = %s; 
            """
    values = (doc_id,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    return result 

async def get_offline_docbooking(doc_id):
    doc_id = int(doc_id)
    query = """select * from doc_onsite_booking
            where doctor_id = %s;
            """
    values = (doc_id,)
    cursor.execute(query , values)
    result = cursor.fetchall()
    return result


async def get_disease_Data(disease):
    query = """select * from disease_Data
            where Dis_name = %s;"""
    values = (disease,)
    cursor.execute(query,values)
    result = cursor.fetchall()

    return result

async def get_symptom_Data(symptom):
    query = """select * from symptoms_data
        where Sym_name = %s;"""
    values = (symptom,)
    cursor.execute(query, values)
    result  = cursor.fetchall()
    return result