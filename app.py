import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from data_to_dict import mapdf,data_dict,Counties
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

plotdf = pd.DataFrame()
plotdf2 = pd.DataFrame()
plotdf['New York City, New York'] = data_dict['New York City, New York']['svdyc']
plotdf['Los Angeles County, California'] = data_dict['Los Angeles County, California']['svdyc']
plotdf2['New York City, New York'] = data_dict['New York City, New York']['svdyd']
plotdf2['Los Angeles County, California'] = data_dict['Los Angeles County, California']['svdyd']



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})
result = mapdf.append(df)
fig = px.choropleth(result, geojson=counties, locations='fips', color='Confirmed Cases',
                           color_continuous_scale="Plotly3",
                           range_color=(0, mapdf['Confirmed Cases'].mean()),
                           scope="usa",
                           labels='County'
                          )
fig2 = px.choropleth(result, geojson=counties, locations='fips', color='Confirmed Deaths',
                           color_continuous_scale="Tropic",
                           range_color=(0, mapdf['Confirmed Deaths'].mean()),
                           scope="usa",
                           labels='County'
                          )

fig3 = make_subplots(rows=1, cols=2)

fig3 = px.line(plotdf, x=plotdf.index.tolist(), y='Los Angeles County, California', title='Los Angeles County, California')
fig4 = px.line(plotdf, x=plotdf.index.tolist(), y='New York City, New York', title='New York City, New York')
fig5 = px.line(plotdf2, x=plotdf2.index.tolist(), y='Los Angeles County, California', title='Los Angeles County, California')
fig6 = px.line(plotdf2, x=plotdf2.index.tolist(), y='New York City, New York', title='New York City, New York')
app.layout = html.Div(children=[
    html.Div([
        html.H1(children='County Wide Covid-19 Confirmed Cases'),
        dcc.Graph(
            id='graph1',
            figure=fig
        ),  
    ]),
    html.Div([
        html.H1(children='County Wide Covid-19 Confirmed Deaths'),
        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ]),
    html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options= Counties,
        value="Los Angeles County, California",
        ),
    ]),
     html.Div([
    dcc.Dropdown(
        id='demo-dropdown2',
        options= Counties,
        value="New York City, New York",
        ),
    ]),
    html.Div([
        html.H1(children='County Covid-19 Cases 7-day Rolling Averages'),
        dcc.Graph(
            id='graph3',
            figure=fig3
        ),  
    ]),
    html.Div([
        dcc.Graph(
            id='graph4',
            figure=fig4
        ),  
    ]),
    html.Div([
    dcc.Dropdown(
        id='demo-dropdown3',
        options= Counties,
        value="Los Angeles County, California",
        ),
    ]),
     html.Div([
    dcc.Dropdown(
        id='demo-dropdown4',
        options= Counties,
        value="New York City, New York",
        ),
    ]),
    html.Div([
        html.H1(children='County Covid-19 Deaths 7-day Rolling Averages'),
        dcc.Graph(
            id='graph5',
            figure=fig5
        ),  
    ]),
    html.Div([
        dcc.Graph(
            id='graph6',
            figure=fig6
        ),  
    ]),
    
])
@app.callback(
    dash.dependencies.Output('graph3', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    plotdf = pd.DataFrame()
    plotdf[value] = data_dict[value]['svdyc']
    fig3 = px.line(plotdf, x=plotdf.index.tolist(), y=value, title=value)
    return fig3
@app.callback(
    dash.dependencies.Output('graph4', 'figure'),
    [dash.dependencies.Input('demo-dropdown2', 'value')])
def update_output2(value):
    plotdf = pd.DataFrame()
    plotdf[value] = data_dict[value]['svdyc']
    fig4 = px.line(plotdf, x=plotdf.index.tolist(), y=value, title=value)
    return fig4
@app.callback(
    dash.dependencies.Output('graph5', 'figure'),
    [dash.dependencies.Input('demo-dropdown3', 'value')])
def update_output2(value):
    plotdf2 = pd.DataFrame()
    plotdf2[value] = data_dict[value]['svdyd']
    fig5 = px.line(plotdf2, x=plotdf2.index.tolist(), y=value, title=value)
    return fig5
@app.callback(
    dash.dependencies.Output('graph6', 'figure'),
    [dash.dependencies.Input('demo-dropdown4', 'value')])
def update_output2(value):
    plotdf2 = pd.DataFrame()
    plotdf2[value] = data_dict[value]['svdyd']
    fig6 = px.line(plotdf2, x=plotdf2.index.tolist(), y=value, title=value)
    return fig6


if __name__ == '__main__':
    app.run_server(debug=True,port = 2625)
