import csv 
from db_operations import cursor , connection

def disease_fromcsv_db():
    data_list = []
    with open('database\diseases.csv', mode="r", newline="") as D_file:
        csv_reader = csv.DictReader(D_file)
        for row in csv_reader:
            data_list.append(dict(row))

    for data in data_list:
        dis_name = data["D_Name"].strip().lower()
        dis_detail = data["D_Detail"].strip().lower()
        dis_precaution = data["D_Precautions"].strip().lower()
        dis_specilist = data["D_Doctor"].strip().lower()

        queryto_run = """INSERT INTO disease_Data(Dis_name, Dis_detail, Dis_prec, Dis_rel_doc_spec)
        VALUES (%s, %s, %s, %s)"""
        values = (dis_name, dis_detail, dis_precaution, dis_specilist)


        cursor.execute(queryto_run , values)
        connection.commit()


def symptoms_fromcsv_db():
    data_list = []
    with open('database\symptons.csv' , mode='r' , newline="")as S_file:
        csv_reader = csv.DictReader(S_file)
        for row in csv_reader:
            data_list.append(dict(row))
    for data in data_list:
        sym_name = data["S_name"].strip().lower()
        sym_detail = data["S_detail"].strip().lower()
        sym_pre = data["S_precaution"].strip().lower()
        sym_dis = data["S_disease"].strip().lower()
        sym_doc = data["S_doctor"].strip().lower()

        queryto_run = f"""INSERT INTO symptoms_Data(Sym_name , Sym_detail , Sym_precaution, Sym_disease ,Sym_Doctor)
        VALUES(%s , %s , %s,%s ,%s)"""
        values = (sym_name , sym_detail , sym_pre ,sym_dis,sym_doc)
        cursor.execute(queryto_run, values)
        connection.commit()

disease_fromcsv_db()
symptoms_fromcsv_db()

cursor.close()
connection.close()