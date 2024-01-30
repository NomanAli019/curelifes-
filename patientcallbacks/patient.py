from database.db_operations import insert_patient
from datetime import datetime
async def separete_patientdata(patient_Data):
    print("we here")
    current_time = datetime.now()
    formated_current_date = current_time.strftime("%Y-%m-%d")

    await insert_patient(patient_Data[0],patient_Data[1],patient_Data[2],patient_Data[3],patient_Data[4],patient_Data[5],formated_current_date,patient_Data[6],patient_Data[7],patient_Data[8],patient_Data[9],patient_Data[10])  

