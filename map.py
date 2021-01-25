##from data_to_dict import mapdf
##import plotly.express as px
##
##fig = px.choropleth(mapdf, geojson=counties, locations='County', color='Confirmed Cases',
##                           color_continuous_scale="Viridis",
##                           range_color=(0, 1100000),
##                           scope="usa",
##                           labels={'County':'Confirmed Cases'}
##                          )
##fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
##fig.show()
from data_to_dict import mapdf
import plotly.figure_factory as ff

fips = mapdf['fips'].tolist()
values = range(len(fips))

fig = ff.create_choropleth(fips=fips, values=values)
fig.layout.template = None
fig.show()
