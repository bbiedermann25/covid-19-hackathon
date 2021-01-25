import pandas as pd
import json
from coviddata import new_data

data_dict = {}
mapdf = pd.DataFrame(columns = ['fips','Confirmed Cases'])
for i in new_data:
    
    cases = i['tstpos']
    deaths =  i['mort']
    dates = i['day']
    c = []
    d = []
    dt = []
    index = 0
    while index < len(dates):
        if cases[index] != '':
            if deaths[index] != '':
                c.append(cases[index])
                d.append(deaths[index])
                dt.append(dates[index])
        index += 1
    cases =  list(map(float, c))
    deaths =  list(map(float, d))
    dates = dt
    svdyc = pd.Series(cases).rolling(7).mean().tolist()
    svdyd = pd.Series(deaths).rolling(7).mean().tolist()
    if i['state'] not in data_dict:
        data_dict[i['state']] = [{'county': i['county'], 'cases':cases,'deaths':deaths,'svdyc':svdyc,'svdyd':svdyd,'dates':dates}]
    else:
        data_dict[i['state']].append({'county': i['county'], 'cases':cases,'deaths':deaths,'svdyc':svdyc,'svdyd':svdyd,'dates':dates})
    if '(state)' not in i['county']:
        mapdf = mapdf.append({'fips':i['fips'][-5:],'Confirmed Cases':cases[-1]},ignore_index = True)  




