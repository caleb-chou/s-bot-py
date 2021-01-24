import requests
import json
import pandas
import pickle
import os.path

from os import path

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

auth = {}

with open('../auth.json','r') as a:
    auth = json.load(a)

TICKER = str(input('Enter ticker: ')).rstrip()

if not path.exists('../cache/'+TICKER+'.pkl'):
    ts = TimeSeries(key=auth['RAPID_ALPHA_V_KEY'],rapidapi=True,output_format='pandas')
    #data, meta_data = ts.get_daily(TICKER)
    #print(data['2021-01-21'])
    data, meta_data = ts.get_intraday(symbol=TICKER,interval='1min', outputsize='full')
    print(data)
    data.to_pickle('../cache/'+TICKER+'.pkl')
    #meta_data.to_pickle('../cache/'+TICKER+'_meta.pkl')

    print('Data Saved')
    #plt.title('Intraday Times Series for the MSFT stock (1 min)')
    data['2. high'].plot()
    plt.show()
else:
    data = pandas.read_pickle('../cache/'+TICKER+'.pkl')
    #meta_data = pandas.read_pickle('../cache/'+TICKER+'_meta.pkl')
    print('Data loaded')
    print(data)
    data['2. high'].plot()
    plt.show()