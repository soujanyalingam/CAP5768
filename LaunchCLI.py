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

    print("Select an Operation: (1) Display Crime Trend by Year  (2) Load Tweets (On-demand)  (3) Preprocess data (4) Exit.")
    operation = input("To select, type  1  2  3  or 4 : \n")
    if operation == '1' :
        Visualizations.ShowTimeSeries(filename)

    if operation == '3':
        InputDataSet.CallPreProcessData()



