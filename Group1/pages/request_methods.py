import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback, dash_table
from plotly.graph_objs import Figure
import dash_ag_grid as dag

df1 = pd.read_csv('datasets/Dataset 1__Web_Server_Access.csv')

#fig_hist1 = px.histogram(df1, x='timestamp', y='response_time_ms', color='http_method')
#fig_scat1 = px.scatter(df1, x='timestamp', y='response_time_ms', color='http_method')
#fig_pie = px.pie(df1, values='http_method', names='status_code', color='status_code', title='Method Status Code')
#fig_hist1.show()

app = dash.Dash(__name__)


layout = html.Div([
    html.H1("View Request Methods"),
    dbc.Button("Home", href="/Home", color="link"),

    dcc.Dropdown(id='methodChoice', options=
        [{'label':x, 'value':x}
        for x in df1.http_method.unique()],
            value=df1.http_method.unique(), multi=True,

    ),
    html.Div([
        dcc.Graph(id='myHist', figure={}, style={'display': 'inline-block'}),
        dcc.Graph(id='myScat', figure={}, style={'display': 'inline-block'}),
        html.Div([
        dcc.Graph(id='urlMethod', figure={}),
        ]),

    ]),
    html.Div([
        dag.AgGrid(id='grid',
                   rowData=df1.to_dict('records'),
                   columnDefs=[{'field':i} for i in df1.columns],
        ),
    ]),
])

@callback(
 Output('myHist', 'figure'),
        Output('myScat', 'figure'),
        Output('urlMethod', 'figure'),
        #Output('grid', 'data'),
        Input('methodChoice', 'value'),

)
def interactive_graph(value_method):
    #print(value_method)
    if type(value_method) != str:
       dff = df1[df1['http_method'].isin(value_method)]
    else:
        dff = df1[df1.http_method==value_method],

    fig_hist1 = px.histogram(dff, x='timestamp', y='response_time_ms', color='http_method')
    fig_scat1 = px.scatter(dff, x='timestamp', y='response_time_ms', color='http_method')
    fig_urlscat= px.scatter(dff, x='url_accessed', y='response_time_ms', color='http_method', title='URL Response Time by Method')

    return fig_hist1, fig_scat1, fig_urlscat


