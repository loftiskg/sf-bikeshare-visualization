import plotly.express as px

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


from preprocessing import preprocess_data
import sys
import os

DATA = './data/kevin_final.csv'

px.set_mapbox_access_token(open(".mapbox_token").read())


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Visualizing Rush Hour through Bikeshare Data"),
        dcc.Dropdown(id='input',options=[
            {'label':'Workweek','value':'workweek'},
            {'label':'Weekend','value':'weekend'}
            ],
            value='workweek'
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output('graph','figure'),[Input('input','value')])
def render_visual(input):
    workweek,weekend = preprocess_data(DATA)

    if input == 'workweek':
        data = workweek
    else:
        data = weekend
    fig = px.scatter_mapbox(data,lat='lat',lon='long',
                        color='Proportion Of Bikes Available',animation_frame='Hour',
                        hover_name='name',color_continuous_scale=px.colors.sequential.Blues,
                        zoom=12)

    fig.update_traces(marker=dict(size=15),
                      selector=dict(mode='markers'))
    return fig

app.run_server(host='0.0.0.0',port=5000)
