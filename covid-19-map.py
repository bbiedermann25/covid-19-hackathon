import plotly
from plotly import graph_objs as go
import us
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests


df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + '01-20-2021' + '.csv')

for col in df.columns:
    df[col] = df[col].astype(str)


df.rename(columns={'Province_State': 'StateName'}, inplace=True)


df=df[df['Country_Region'].str.contains("US")]


states_dic=us.states.mapping('name', 'abbr')
df.StateName.map(states_dic)
df['code'] = df.StateName.map(states_dic)


df = df.dropna()

df['text'] = df['StateName'] + '<br>' + \
    'Confirmed: ' + df['Confirmed'] + '<br>' + \
    'Deaths: ' + df['Deaths']



fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['Confirmed'].astype(float),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=df['text'], 
    marker_line_color='white', 
    colorbar_title="Hundreds"
))

fig.update_layout(
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, 
        lakecolor='rgb(255, 255, 255)'),
)

fig.show()