import pandas as pd
import json
from coviddata import new_data

data_dict = {}
Counties = []
mapdf = pd.DataFrame(columns = ['County','Confirmed Cases'])
for i in new_data:
    cases = i['tstpos']
    deaths =  i['mort']
    dates = i['day']
    Counties.append({'label':i['county'], 'value':i['county']})
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
    c = pd.Series(cases).diff().tolist()
    d = pd.Series(deaths).diff().tolist()
    c[0] = 0
    d[0] = 0
    svdyc = pd.Series(c).rolling(7).mean().tolist()
    svdyd = pd.Series(d).rolling(7).mean().tolist()
    data_dict[i['county']] = {'cases':cases,'deaths':deaths,'svdyc':svdyc[6:],'svdyd':svdyd[6:],'dates':dates}
    if '(state)' not in i['county']:
        mapdf = mapdf.append({'County':i['county'],'fips':i['fips'][-5:],'Confirmed Cases':cases[-1], 'Confirmed Deaths':deaths[-1]},ignore_index = True)


mapdf = mapdf[:-1]



