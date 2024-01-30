from fastapi import FastAPI,Query
import uvicorn 
from patientcallbacks.patient import separete_patientdata
from typing import Dict
from blogData.get_disease import cleaning_Disease , cleaning_symptoms
import random 
import json
from doctorDataCleaning.doctClean import doc_data_sepration 
from doctorcallbacks.doctor import inserting_doctor_Data , Dset_online_booking , Dset_onsite_booking,getting_doctor
from typing import List
app = FastAPI()
import requests

from bs4 import BeautifulSoup
@app.get("/")
async def index_dermo():
    a = "yes"
    return {"the api worked! ": a }

# dermotologists data fatching route 
@app.get("/doctormarham/{city}/speciality/{speciality}/page{pageno}")
async def dermotologist_lahore(city:str , speciality:str , pageno:int):
    speciality = speciality.lower()
    speciality = speciality.replace(" " ,"-")
    response = requests.get(f"https://www.marham.pk/doctors/{city}/{speciality}?page={str(pageno)}")
    response.raise_for_status()  # Add parentheses to raise_for_status()
    if response:
        
        dero_respo_all = response.text
        soup = BeautifulSoup(dero_respo_all, "html.parser")
        class_name_for_doc_details = "row shadow-card"
        data = soup.find_all("div", class_=class_name_for_doc_details)
        
        dermo_doc_data = []
        for one_doc in data:
            
            dermo_doc_data.append(await doc_data_sepration(one_doc))
        
        return dermo_doc_data
    else:
        
        return None

# patient insert 
@app.post("/patient_datainsert")
async def patient_data(signup_data: List[str]):
    if signup_data:
        print("we here")
        await separete_patientdata(signup_data)
        return {"data_entered": "yes"}
    else:
        return {"data_entered":"No"}

# doctor insert
@app.post("/doctors_datainsert")
async def doctor_data(data:dict):
    if data:
        await inserting_doctor_Data(data)
        return {"data_entered":"yes"}
    else:
        return {"data_entered":"no"}

@app.post("/doconline_booking/{doctor_id}/doc_fee/{d_online_fee}/doc_online_days/{days}/doc_timing/{time}")
async def doconline_booking(doctor_id:int ,d_online_fee:int, days:str , time:str):
    if doctor_id:
        await Dset_online_booking(doctor_id,d_online_fee,days,time)
        return {"data_entered":"yes"}
    else:
        return {"data_entered":"no"}

@app.post("/docoffline_booking/{doctor_id}/docfee/{doc_fee}/days/{days}/location/{locat}/time/{time}")
async def docoffline_booking(doctor_id:int,doc_fee:int,days:str,locat:str,time:str):
    if doctor_id:
        await Dset_onsite_booking(doctor_id,doc_fee,days,locat,time)
        return {"data_entered":"yes"}
    else:
        return {"data_entered":"no"}

@app.get("/getdoctor_fromdb/{city}/specilization/{specaility}")
async def getdoctor_fromdb(city:str,specaility:str):
    city = city.lower()
    specaility = specaility.lower()
    doctor_data =  await getting_doctor(city,specaility)
    if doctor_data == "no":
        return {"doctor found":"no"}

    return doctor_data

@app.get("/get_disease/{disease}")
async def get_disease(disease: str): 
    print(disease)
    disease_detial = await cleaning_Disease(disease)
    return disease_detial

@app.get("/symptomsblog/{symptom}")
async def get_symptom(symptom:str):
    symptom_Detail = await cleaning_symptoms(symptom)
    return symptom_Detail



 
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=7000, reload=True)

