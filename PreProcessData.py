import pandas as pd
import numpy as np
import csv
import os
from datetime import datetime


def SetDateTimeFormat(filename, header):
    temp_filename = filename.strip('.csv') + '_temp.csv'
    with open(temp_filename, 'w', newline='', encoding='utf8') as tempfile:
        writer = csv.DictWriter(tempfile, fieldnames=header)
        writer.writeheader()
        with open(filename, newline='') as csvfile:
            print("Preprocessing Data...")
            reader = csv.DictReader(csvfile);
            for row in reader:
                row_date = datetime.strptime(row['Date'], "%m/%d/%Y %H:%M:%S %p")
                row_update_on = datetime.strptime(row['Updated On'], "%m/%d/%Y %H:%M:%S %p")
                row_year = datetime.strptime(row['Year'], "%Y")
                #writer.writerow({'': '', 'ID': row['ID'], 'Case Number': row['Case Number'], 'Date': row_date})
                writer.writerow({'':'','ID':row['ID'],'Case Number':row['Case Number'],'Date':row_date,'Block':row['Block'],'IUCR':row['IUCR'],
                                 'Primary Type':row['Primary Type'],'Description':row['Description'],
                                 'Location Description':row['Location Description'],'Arrest':row['Arrest'],'Domestic':row['Domestic'],
                                 'Beat':row['Beat'],'District':row['District'],'Ward':row['Ward'], 'Community Area':row['Community Area'],
                                 'FBI Code':row['FBI Code'],'X Coordinate':row['X Coordinate'],'Y Coordinate':row['Y Coordinate'],'Year':row_year,
                                 'Updated On':row_update_on,'Latitude':row['Latitude'],'Longitude':row['Longitude'],'Location':row['Location']})
    os.remove(filename)
    os.rename(temp_filename, filename)
    print("Done")
    csvfile.close()
    tempfile.close()

def percentEmpty(dataFrame):
    NullSumDF=dataFrame.isnull().sum()
    totalRows=len(dataFrame)
    print("totalRows",totalRows)
    perDframe = pd.DataFrame((NullSumDF/totalRows)*100, columns=['percent'])
    perDframe['colName'] = perDframe.index
    return perDframe

def RemoveNullValues(filename):

    data = pd.read_csv(filename, low_memory=False)
    #print(data.tail)
    NullSumDF = data.isnull().sum()  # Check is there are Null values in data
    #print(NullSumDF)
    #print(percentEmpty(data))   # To check percentage of Null data in columns
    data.dropna(subset=['Case Number', 'District', 'Latitude'], how='any', inplace=True)
    # print(percentEmpty(data))
    data = data.sort_values('Date')  # Sort via Date
    #data.drop(data.tail(1).index, inplace=True)  # Drop last row (header is appended in last row is removed, no data loss)
    os.remove(filename)
    data.to_csv(filename)


