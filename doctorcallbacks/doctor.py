from database.db_operations import insert_doctor , get_doctors,set_doctor_booking,set_doctor_offlinebooking
async def inserting_doctor_Data(doctor_data):
    d_list = []
    for i in doctor_data:
        d_list.append(doctor_data[i])

    await insert_doctor(d_list)

async def Dset_online_booking(doc_id , d_onlinefee ,days,time ):
    await set_doctor_booking(doc_id , d_onlinefee ,days,time )

async def Dset_onsite_booking(doc_id , d_offlinefee , days, locat, time):
    await set_doctor_offlinebooking(doc_id , d_offlinefee , days, locat, time)


async def getting_doctor(city , specaility):
    data_doctor  = await get_doctors(city , specaility)
    if data_doctor:
        columns = ["id", "d_first_name", "d_last_name", "d_date_of_birth", "d_gender",
               "d_phone_number", "d_address", "d_registration_date", "d_specialization",
               "d_license_number", "d_hospital_affiliation", "d_experience_years",
               "d_email", "d_password"]
        doctors_list = []

        for row in data_doctor:
            doctor_dict = dict(zip(columns, row))
            print(doctor_dict['id'])
            
            doctors_list.append(doctor_dict)
            

        
        
        return "yes"
    else:
        return "no"
