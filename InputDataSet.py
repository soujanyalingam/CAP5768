import pandas as pd
import numpy as np
import csv
import os
from datetime import datetime
from CAP5768.Project import PreProcessData


#Set File Path URL
#url = "./data/Chicago_Crimes_2001_2018.csv"
url = "./data/data_small.csv"
filename = os.path.abspath("./data/data_small.csv")

#Set Column Names
names = ['ID','Case Number','Date','Block','IUCR','Primary Type','Description','Location Description','Arrest','Domestic','Beat','District','Ward',
         'Community Area','FBI Code','X Coordinate','Y Coordinate','Year','Updated On','Latitude','Longitude','Location']

names_extra = ['','ID', 'Case Number', 'Date', 'Block', 'IUCR', 'Primary Type', 'Description', 'Location Description',
             'Arrest', 'Domestic', 'Beat', 'District', 'Ward', 'Community Area', 'FBI Code', 'X Coordinate', 'Y Coordinate', 'Year', 'Updated On', 'Latitude',
             'Longitude', 'Location']

dtypes = {'ID':str,'Case Number':str,'Date':datetime,'Block':str,'IUCR':str,'Primary Type':str,'Description':str,'Location Description':str,'Arrest':str,'Domestic':str,
          'Beat':str,'District':str,'Ward':str, 'Community Area':str,'FBI Code':str,'X Coordinate':str,'Y Coordinate':str,'Year':str,
          'Updated On':str,'Latitude':str,'Longitude':str,'Location':str}

#data = pd.read_csv(url, names=names,  parse_dates=['Date'], encoding = 'iso-8859-1', index_col=0, infer_datetime_format=True)
#print(data['Date'].iloc[1])
#datetime_object = datetime.strptime(data['Date'].iloc[1], "%m/%d/%Y %H:%M:%S %p")
#data['Date'] = datetime.strptime(data['Date'], "%m/%d/%Y %H:%M:%S %p")
#for index, row in data.iterrows(): #data['Date'].iloc[index] = datetime.strptime(data['Date'].iloc[index], "%m/%d/%Y %H:%M:%S %p")

def LoadData():
    print() #Do nothing. This is placeholder

def CallPreProcessData():
    PreProcessData.RemoveNullValues(filename)
    PreProcessData.SetDateTimeFormat(filename, names_extra)




