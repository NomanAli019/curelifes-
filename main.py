from fastapi import FastAPI,Query
import uvicorn 
from patientcallbacks.patient import separete_patientdata
from typing import Dict
import random 
import json
from doctorDataCleaning.doctClean import doc_data_sepration
from patientcallbacks import patient  
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
        class_name_for_doc_details = "py-3 mt-2 bg-white col-md-11 col-lg-10 col-12 center doc-card-shadow doctor-card"
        data = soup.find_all("div", class_=class_name_for_doc_details)
        
        dermo_doc_data = []
        for one_doc in data:
            
            dermo_doc_data.append(await doc_data_sepration(one_doc))
        
        return dermo_doc_data
    else:
        return None

@app.post("/patient_data")
async def patient_data(data: dict):
        # Assuming data is a dictionary
    if data:
        await separete_patientdata(data)
        return {"data_entered": "yes"}
    else:
        return {"data_entered":"No"}

    
 


 
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

