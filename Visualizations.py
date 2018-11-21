import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import pandas as pd
import csv
import numpy as np
import os
import seaborn as sn
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from os import system
import graphviz


plt.style.use('fivethirtyeight')
matplotlib.rcParams['axes.labelsize'] = 12
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

# Display crime by time series graph between 2001 to current.
def ShowTimeSeries(filename):
    filename_timeseries = filename.strip('.csv') + '_timeseries.csv'
    data = pd.read_csv(filename, low_memory=False)
    data_year = data.groupby(['Year'])[['ID']].count()
    data_year.to_csv(filename_timeseries)
    data_year = pd.read_csv(filename_timeseries, low_memory=False)
    '''
    data_x = data_year['Year']
    data_y = data_year['ID']
    plt.plot(figsize=(20, 4))
    plt.plot(data_x, data_y)
    plt.show()
    '''
    data_year = data_year.set_index('Year')
    print(data_year.index)
    data_year.plot(figsize=(10, 6))
    plt.title('Crime reported in Chicago between year 2001 to 2018')
    plt.ylabel("# Crime count");
    plt.xlabel("Years");
    plt.legend();
    plt.show()

# Display crime count pie-chart (count between 2001 - Current)
def ShowCrimePieChart(filename):
    input_data = pd.read_csv(filename, header=0)
    df = pd.DataFrame(input_data)
    cs = cm.Set1(np.arange(40) / 40.)
    plt.figure(figsize=(16, 16))
    df['Primary Type'].value_counts(sort=True).plot.pie(title='Types of crimes', figsize=(16, 16), fontsize=8)
    plt.show()


# Draw graph for showing crime count by Chicago community names
def ShowCrimeBarPlotByCommunity(filename):
    DisplayCrimeByAreaBarChart(filename)
    input_data = pd.read_csv(filename, header=0)
    df = pd.DataFrame(input_data)
    cs = cm.Set1(np.arange(40) / 40.)
    plt.figure(figsize=(16, 16))
    df['Community Area Name'].value_counts(sort=True).plot.bar(title='Crimes in Community', figsize=(16, 16), fontsize=8)
    plt.show()

# This returns a Dataframe containing 2 columns - community code and community name.
def getChicagoCommunityName(filename):
    area_file = filename
    xl = pd.ExcelFile(area_file)
    # print(xl.sheet_names[0])
    df1 = xl.parse(xl.sheet_names[0])
    return df1;


# Loop through the dataset and add an additional column for community name (there was only community code not names by default).
def DisplayCrimeByAreaBarChart(filename):
    file_area = os.path.abspath("./data/Chicago_Area_Data.xlsx")
    df_area = getChicagoCommunityName(file_area)
    filename_byArea = filename.strip('.csv') + '_CrimeByArea.csv'
    header = ['', 'ID', 'Case Number', 'Date', 'Block', 'IUCR', 'Primary Type', 'Description', 'Location Description',
              'Arrest',
              'Domestic', 'Beat', 'District', 'Ward', 'Community Area', 'Community Area Name', 'FBI Code',
              'X Coordinate', 'Y Coordinate',
              'Year', 'Updated On', 'Latitude', 'Longitude', 'Location']
    with open(filename_byArea, 'w', newline='', encoding='utf8') as tempfile:
        writer = csv.DictWriter(tempfile, fieldnames=header)
        writer.writeheader()
        with open(filename, newline='') as csvfile:
            print("Generating Data...")
            reader = csv.DictReader(csvfile);
            for row in reader:
                area_code = int((row['Community Area']).split(".")[0])
                area_name = df_area.iloc[area_code, 0]

                writer.writerow({'': '', 'ID': row['ID'], 'Case Number': row['Case Number'], 'Date': row['Date'],
                                 'Block': row['Block'], 'IUCR': row['IUCR'],
                                 'Primary Type': row['Primary Type'], 'Description': row['Description'],
                                 'Location Description': row['Location Description'], 'Arrest': row['Arrest'],
                                 'Domestic': row['Domestic'],
                                 'Beat': row['Beat'], 'District': row['District'], 'Ward': row['Ward'],
                                 'Community Area': row['Community Area'], 'Community Area Name': area_name,
                                 'FBI Code': row['FBI Code'], 'X Coordinate': row['X Coordinate'],
                                 'Y Coordinate': row['Y Coordinate'], 'Year': row['Year'],
                                 'Updated On': row['Updated On'], 'Latitude': row['Latitude'],
                                 'Longitude': row['Longitude'], 'Location': row['Location']})
    os.remove(filename)
    os.rename(filename_byArea, filename)
    print("Done")
    csvfile.close()
    tempfile.close()

# Generate plot for crime location (home, road, mall etc)
def DisplayCrimeLocation(filename):
    input_data = pd.read_csv(filename, header=0)
    plt.figure(figsize=(15, 10))
    sn.countplot(y='Location Description', data=input_data, order=input_data['Location Description'].value_counts().iloc[:10].index)
    plt.show()

# Generate plot for Arrests made on yearly basis and monthly basis
def DisplayArrestTrend(filename):
    input_data = pd.read_csv(filename, index_col='Date')
    input_data.index = pd.to_datetime(input_data.index)
    ## Arrests per year
    arrest_count_yearly = input_data[input_data['Arrest'] == True]['Arrest']
    plt.subplot()
    # Get Yearly arrest trend
    arrest_count_yearly.resample('A').sum().plot()
    plt.title('Arrests trend by Yearly')
    plt.show()
    # Get Monthly arrest trend
    arrest_count_yearly.resample('M').sum().plot()
    plt.title('Arrests trend by Monthly')
    plt.show()

# Draw graph for domestic violence crime
def DisplayDometicViolenceCrime(filename):
    input_data = pd.read_csv(filename, index_col='Date')
    input_data.index = pd.to_datetime(input_data.index)
    domestic_crime_yearly = input_data[input_data['Domestic'] == True]['Domestic']
    plt.subplot()
    # Yearly trend - domestic violence
    domestic_crime_yearly.resample('A').sum().plot()
    plt.title('Yearly trend - domestic violence')
    plt.show()
    # Monthly trend - domestic violence
    domestic_crime_yearly.resample('M').sum().plot()
    plt.title('Monthly trend - domestic violence')
    plt.show()

