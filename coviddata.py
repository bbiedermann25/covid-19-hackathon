import pandas as pd
import json
import requests
import os
from datetime import datetime, timedelta

os.chdir('/Users/brandoboomin/Desktop')
df = pd.read_csv('Coronavirus_by_County.csv')
df1 = df[['region','state_fips','fips','county','state']]
df = df.drop(['region','state_fips','fips','county','state'], axis=1)

data = pd.DataFrame(columns = ['Date', 'State','County','Confirmed Cases',
                                      'Probable Cases','Confirmed Deaths', 'Probable Deaths', '7 Day Rolling Average'])
nrow = df.shape[0]
index = 0
date = datetime(2020, 1, 20)
for i in df1['county']:
    county = i
    date = 
    
    

        

#datetime.today() - timedelta(days=3)


    
