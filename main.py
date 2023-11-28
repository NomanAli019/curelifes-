from fastapi import FastAPI
import uvicorn 
import random   
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
            
            dermo_doc_data.append(await dermo_doc_data_sepration(one_doc))
        
        return dermo_doc_data
    else:
        return None

# dermotologists data cleaner 
async def dermo_doc_data_sepration(one_doc):
    doc_name = one_doc.find("h3", class_="underline font-weight-bold text-marham text-md font-sm d-flex align-items-center")
    doc_link = one_doc.find("a" , class_="dr_appointment_listing_tap_name")
    doc_specilization = one_doc.find("p", class_="mb-0 text-sm-base")
    doc_degree = one_doc.find("p" , class_="mb-0 font-weight-normal text-sm-base text-three-base-truncate")
    doc_experience = one_doc.find("div" , class_="px-4 px-md-4 doc-Experience px-lg-5")
    doc_online_booking = one_doc.find("div" , class_="px-0 pt-3 pb-1 card-body ga-event-online-card-click BookingModalListing dr_oc_listing_tapped_hospital")
    
    doc_on_site_booking = one_doc.find("div" , class_="px-0 pt-3 pb-1 card-body phy-card-min-width phy-card-sm-min-width")
    doct_dict = {}

    if doc_name:
        doct_dict["doc_name"] = doc_name.text
    else:
        doct_dict["doc_name"] = None
    if doc_link:
        doct_dict["doc_link"] = doc_link.get("href")
    else:
        doct_dict["doc_link"] = None

    if doc_specilization:
        doct_dict["doc_specilization"] = doc_specilization.text
    else:
        doct_dict["doc_specilization"] = None
    if doc_degree:
        doct_dict["doc_degree"] = doc_degree.text
    else:
        doct_dict["doc_degree"]  = None
    if doc_experience:
        doct_dict["doc_experience"] = doc_experience.text
    else:
        doct_dict["doc_experience"] = None
    if doc_online_booking:
        doc_timing = doc_online_booking.find("p" , class_="mb-0 card-text text-sm-base gray-color font-weight-medium overflow-dotted text-truncate d-flex align-items-center")
        doc_card_title = doc_online_booking.find("p" , class_="mb-0 text-base card-title font-weight-medium")
        doc_availibility = doc_online_booking.find("p" , class_="mb-0 color-success text-sm-base font-weight-medium")
        doct_dict["online_booking_title"] = doc_card_title.text
        doct_dict["doc_online_booking_time"] = doc_timing.text
        doct_dict["Availability_online"]  = doc_availibility.text
    else:
        doct_dict["doc_online_booking"] = None

    if doc_on_site_booking:
        doc_on_site_loc = doc_on_site_booking.find("p", class_="mb-0 text-base card-title font-weight-medium")
        doc_on_site_time = doc_on_site_booking.find("p" , class_="mb-0 mr-3 card-text text-sm-base gray-color font-weight-medium d-flex align-items-center")
        doc_on_site_availibility = doc_on_site_booking.find("p" , class_="mb-0 color-success text-sm-base font-weight-medium")
        doct_dict["doc_on_site_loc"] = doc_on_site_loc.text
        doct_dict["doc_on_site_time"] = doc_on_site_time.text
        doct_dict["doc_on_site_avaibability"] = doc_on_site_availibility.text

    else:
        doct_dict["doc_on_site_booking"] = None

    return doct_dict


    
 


 
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

