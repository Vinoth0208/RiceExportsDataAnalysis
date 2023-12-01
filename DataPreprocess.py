import os
import pandas as pd
import streamlit as st

def data():
    datapath=r"C:\Users\Vinoth\PycharmProjects\RiceExportsDataAnalysis\Data"
    datafiles=os.listdir(datapath)
    data=pd.concat([pd.read_csv(datapath+"/"+file) for file in datafiles], ignore_index=True)

    print(data.head())
    print(data.info())
    print(data.shape)
    data.drop_duplicates()
    for i in ["VOLUME UNIT","PREPORT","US STATE","US PORT2","FINAL US PORT","FINAL FOREIGN PORT","FINAL COUNTRY","PORT OF DEPARTURE.1","SHIPPER COUNTRY","Final Qty"]:
        del data[i]
    print(data.columns)
    print(data.isna().sum())

    data["ARRIVAL DATE"] = pd.to_datetime(data["ARRIVAL DATE"])

    frequenctly_occured_PRODUCT_DETAILS = data["PRODUCT DETAILS"].mode()
    frequently_occured_CITY_STATE = data["CITY STATE"].mode()
    frequently_occured_CURRENCY = data["CURRENCY"].mode()
    frequently_occured_QUANTITY_UNIT = data["QUANTITY UNIT"].mode()
    frequently_occured_PACKAGES_UNIT= data["PACKAGES UNIT"].mode()
    frequently_occured_PORT_OF_DEPARTURE= data["PORT OF DEPARTURE"].mode()
    frequently_occured_PORT_OF_ARRIVAL= data["PORT OF ARRIVAL"].mode()

    data["HS CODE DESCRIPTION"].fillna(data["PRODUCT DETAILS"],inplace=True)
    data["IMPORTER NAME"].fillna("No Importer name given", inplace=True)
    data["IMPORTER ADDRESS"].fillna("No Importer address", inplace=True)
    data["IMPORTER ADDRESS"].replace(".","No Importer address", inplace=True)
    data["CITY STATE"].fillna(frequently_occured_CITY_STATE[0], inplace=True)
    data["E-MAIL"].fillna("No E-MAIL", inplace=True)
    data["E-MAIL"].replace(".","No E-MAIL", inplace=True)
    data["WEB"].fillna("No Web available",inplace=True)
    data["WEB"].replace(".","No Web available",inplace=True)
    data["EXPORTER NAME"].fillna("No Exporter name given", inplace=True)
    data["EXPORTER ADDRESS"].fillna("No Exporter address", inplace=True)
    data["EXPORTER ADDRESS"].replace("-","No Exporter address", inplace=True)
    data["CURRENCY"].fillna(frequently_occured_CURRENCY[0],inplace=True)
    data["PRODUCT DETAILS"].fillna(frequenctly_occured_PRODUCT_DETAILS[0], inplace=True)
    data["INCOTERMS"].fillna("No Incoterms available", inplace=True)
    data["NOTIFY PARTY"].fillna("No Notify party available", inplace=True)
    data["NOTIFY ADDRESS"].fillna("No Notify address available", inplace=True)
    data["QUANTITY UNIT"].fillna(frequently_occured_QUANTITY_UNIT[0], inplace=True)
    data["NET WEIGHT UNIT"].fillna("Kg",inplace=True)
    data["GROSS WEIGHT UNIT"].fillna("Kg",inplace=True)
    data["PACKAGES UNIT"].fillna(frequently_occured_PACKAGES_UNIT[0], inplace=True)
    data["PORT OF DEPARTURE"].fillna(frequently_occured_PORT_OF_DEPARTURE[0], inplace=True)
    data["PORT OF ARRIVAL"].fillna(frequently_occured_PORT_OF_ARRIVAL[0], inplace=True)
    data["TEL"].fillna("No TEL DATA AVAILABLE", inplace=True)
    data["TEL"].replace(".","No TEL DATA AVAILABLE", inplace=True)
    data["FAX"].fillna("No FAX DATA AVAILABLE", inplace=True)
    data["FAX"].replace(".","No FAX DATA AVAILABLE", inplace=True)
    data["PLACE OF DELIVERY"].fillna("No Place of delivery available", inplace=True)
    data["BRAND NAME"].fillna("No Brand name available", inplace=True)
    data["MANUFACTORING COMPANY"].fillna("No Manufactoring company available", inplace=True)
    data['IMPORT VALUE CIF'] = data['IMPORT VALUE FOB']+ data['IMPORT VALUE FOB'] * (20 / 100) + data['IMPORT VALUE FOB'] * (1.125 / 100)
    data['year'] = data['ARRIVAL DATE'].apply(lambda date: date.year)


    print(data.isna().sum())

    st.write(data)
    data.to_csv(r"Data.csv")
    Data=pd.read_csv(r'Data.csv')
    File=Data.to_csv()
    st.download_button(
                label="Download data as CSV",
                data=File,
                file_name='Rice Exporters Consolidated.csv',
                mime='text/csv',)
