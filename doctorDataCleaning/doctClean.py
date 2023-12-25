async def doc_data_sepration(one_doc):
    doc_name_etc_Data = one_doc.find("div" , class_="col-9 col-md-10")
    
    doc_experience = one_doc.find("div" , class_="text-bold text-sm")
    doc_online_booking = one_doc.find("div" , class_="mb-2 mr-10 product-card col-9 col-md-5 col-lg-3 col-sm-5 cursor-pointer")
    
    doc_on_site_booking = one_doc.find("div" , class_="mb-2 mr-10 product-card card-hospital cursor-pointer")
    doct_dict = {}

    if doc_name_etc_Data:
        doc_name = doc_name_etc_Data.find("h3", class_="mb-5 text-underline")
        doc_link = doc_name_etc_Data.find("a" , class_="text-blue")
        doc_specilization = doc_name_etc_Data.find("p", class_="mb-0 text-sm")
        doc_degree = doc_name_etc_Data.find_all("p" , class_="text-sm")
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
            i = 0 
            for doc in doc_degree:
                i = i+1
                if i == 2:
                    doct_dict["doc_degree"] = doc.text
        else:
            doct_dict["doc_degree"]  = None
    if doc_experience:
        doct_dict["doc_experience"] = doc_experience.text
    else:
        doct_dict["doc_experience"] = None
    if doc_online_booking:
        doc_availibility = doc_online_booking.find("p" , class_="mb-0 text-sm")
        doc_online_fee = doc_online_booking.find("p" , class_="mb-0 price text-sm")
        
        doct_dict["Availability_online"]  = doc_availibility.text
        doct_dict["doc_online_fee"] = doc_online_fee.text
        
    else:
        doct_dict["doc_online_booking"] = None

    if doc_on_site_booking:
        
        doc_onsite_Address = doc_on_site_booking.find("p" , class_="mb-0 text-bold text-blue text-sm")
        doc_on_site_fee = doc_on_site_booking.find("p" , class_="mb-0 price text-sm")
        doc_on_site_availibility = doc_on_site_booking.find("p" , class_="mb-0 text-sm")
        doct_dict["doc_on_site_avaibability"] = doc_on_site_availibility.text
        doct_dict["doc_on_site_fee"] = doc_on_site_fee.text
        doct_dict["doc_location"] = doc_onsite_Address.text

    else:
        doct_dict["doc_on_site_booking"] = None

    return doct_dict