import pandas as pd
import json

df = pd.DataFrame(columns = ['County,State', 'cases', 'deaths', '7 day cases','7 day deaths'])
for i in new_data:
    cases = i['tstpos'][-8:]
    deaths =  i['mort'][-8:]
    [i.strip() for i in cases]
    [i.strip() for i in deaths]
    try:
        cases =  list(map(float, cases))
    except ValueError:
        cases = ['N/A']
        rlavgc = 'N/A'
    try:
        deaths =  list(map(float, deaths))
    except ValueError:
        deaths = ['N/A']
        rlavgd = 'N/A'
    try:
        rlavgc = (cases[-1] - cases[1])/7
    except (TypeError, IndexError):
        rlavgc = 'N/A'
    try:
        rlavgd = (deaths[-1] - deaths[1])/7
    except (TypeError, IndexError):
        rlavgd = 'N/A'
    df = df.append({'County,State': i['county'],'cases':cases[-1],'deaths':deaths[-1],'7 day cases':rlavgc,'7 day deaths':rlavgd},ignore_index = True)

result = df.to_json(orient="index")
parsed = json.loads(result)
json.dumps(parsed, indent=4)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(parsed, f, ensure_ascii=False, indent=4)
