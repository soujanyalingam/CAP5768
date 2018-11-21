import datetime
from colorama import init, Fore, Back, Style
from termcolor import colored
import os
from CAP5768.Project import Visualizations
from CAP5768.Project import InputDataSet

# Initializing the variables.
operation = '0'
count =10
now = datetime.datetime.now()
from_date = now - (datetime.timedelta(days=1))
to_date, from_date = str(now.date()), str(from_date.date())
filename = os.path.abspath("./data/data_small.csv")


while (operation != 'E'):
    #print(Style.BRIGHT + Fore.BLUE);print(Style.RESET_ALL)
    print("\n\nSelect options from below menu: (To exit, type E)-------- ")
    if (operation == 'E' or operation == '4'):
        print("Exiting the Menu. Bye...")
        break

    print("Select an Operation: (1) Visuallize/Analyze Data (2) Download Fresh Data  (3) Preprocess data (4) Exit.")
    operation = input("To select, type  1  2  3  or 4 : \n")

    if operation == '1':
        print("Select an Operation: (1) Display year wise trend (2) Display types of crime (3) Display Crime by Community (4) Display Domestic violence by year and month  (5) Display the location of Crime.")
        op_display = input("To select, type  1  2  3  or 4 : \n")
        if op_display == '1':  #Display Time Series of data
            Visualizations.ShowTimeSeries(filename)
        if op_display == '2':  # Display type of crimes and their relative frequencies.
            Visualizations.ShowCrimePieChart(filename)
        if op_display == '3':  # Crime by community area in Chicago
            Visualizations.ShowCrimeBarPlotByCommunity(filename)
        if op_display == '4':  # Domestic Violence by year and month
            Visualizations.DisplayDometicViolenceCrime(filename)
        if op_display == '5':
            Visualizations.DisplayCrimeLocation(filename)


    if operation == '2':
        print()# Download data - Placeholder

    if operation == '3':
        InputDataSet.CallPreProcessData()

    if operation == '4':
        break;

