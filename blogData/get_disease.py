
from database.db_operations import get_disease_Data  , get_symptom_Data
async def cleaning_Disease(disease):
    print(disease , "we here in cleaner ")
    disease_data = await get_disease_Data(disease)
    print(disease_data)
    if disease_data:
        d_id, d_name, d_detail, d_precaution, d_doctor = disease_data[0]
        disease_dict = {
            'd_id': d_id,
            'd_name': d_name,
            'd_detail': d_detail,
            'd_precaution': d_precaution,
            'd_doctor': d_doctor
        }
        print(disease_dict , "we here ")
        return disease_dict
    

async def cleaning_symptoms(symptom):
    print(symptom , "we here in cleaner ")
    symptom_data = await get_symptom_Data(symptom)
    print(symptom_data)
    if symptom_data:
        d_id, d_name, d_detail, d_precaution, d_disease , d_doctor = symptom_data[0]
        symptom_dict = {
            'd_id': d_id,
            'd_name': d_name,
            'd_detail': d_detail,
            'd_precaution': d_precaution,
            'd_disease':d_disease,
            'd_doctor': d_doctor
        }
        print(symptom_dict , "we here ")
        return symptom_dict
    