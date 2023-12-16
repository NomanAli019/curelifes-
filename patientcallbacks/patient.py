from database.db_operations import insert_patient
async def separete_patientdata(patient_Data):
    print("we here")
    p_list = []
    for i in patient_Data:
       
        p_list.append(patient_Data[i])
        

    await insert_patient(p_list[0],p_list[1],p_list[2],p_list[3],p_list[4],p_list[5],p_list[6],p_list[7],p_list[8],p_list[9],p_list[10],p_list[11])  

