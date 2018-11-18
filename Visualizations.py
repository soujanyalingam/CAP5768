import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
plt.style.use('fivethirtyeight')
matplotlib.rcParams['axes.labelsize'] = 12
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'


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
    #print(data_year.index)
    data_year.plot(figsize=(10, 4))
    plt.title('Crime reported in Chicago between year 2001 to 2018')
    plt.ylabel("# Crime count");
    plt.xlabel("Years");
    plt.legend();
    plt.show()
