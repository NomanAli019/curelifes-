from database.db_operations import insert_doctor , get_doctors,set_doctor_booking,set_doctor_offlinebooking
from database.db_operations import get_online_docbooking,get_offline_docbooking
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
    print(len(data_doctor))
    if data_doctor:
        doctors_list = []
        data_dict = {}
        for i , row in enumerate(data_doctor):
            doctr_id, d_first_name, d_last_name, d_date_of_birth, d_gender, d_phone_number, d_address, d_registration_date, d_specialization, d_degree, d_license_number, d_hospital_affiliation, d_experience_years, d_email, d_password = data_doctor[i]
            doc_online_booking = await get_online_docbooking(doctr_id)
            booking_id, doc_id, amount, days, time_range = doc_online_booking[0]
            # for onsite visite 
            doc_offline_booking = await get_offline_docbooking(doctr_id)
            onsiteid , ondocid, onamount , onday,onloc , ontime = doc_offline_booking[0]
            data_dict['dfullname'] = d_first_name+d_last_name
            data_dict['dspeciality'] = d_specialization
            data_dict['ddegree'] = d_degree
            data_dict['experience'] = d_experience_years
            data_dict['onlinefee'] = amount 
            data_dict['onlinedays'] = days
            data_dict['onlinetime'] = time_range
            data_dict['offlinefee'] = onamount 
            data_dict['offlinedays'] = onday
            data_dict['offlineloc'] = onloc
            data_dict['offlinetime'] = ontime

            
            doctors_list.append(data_dict)
            

        
        
        return doctors_list
    else:
        return "no"
