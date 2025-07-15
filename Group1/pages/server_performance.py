import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback, dash_table
from plotly.graph_objs import Figure
import dash_ag_grid as dag

df1 = pd.read_csv('datasets/Dataset 1__Web_Server_Access.csv')
df2 = pd.read_csv('datasets/Dataset 4__Network_Traffic_Summary.csv')

#lineIn = px.scatter(df2, x='sample_time', y='inbound_bytes', color='suspicious_activity')
fig_pie = px.pie(df1, values='http_method', names='status_code', color='status_code', title='Method Status Code'),
#activity = df2.suspicious_activity.unique().tolist()
#lineIn.show()

app = dash.Dash(__name__)


layout = html.Div([
    html.H1("View Server Performance"),
    dbc.Button("Home", href="/Home", color="link"),

    # dcc.Dropdown(id='methodChoice', options=
    #     [{'label':x, 'value':x}
    #     for x in df1.http_method.unique()],
    #         value=df1.http_method.unique(), multi=True,

        html.Div([
            dcc.Checklist(
                id='checklist',
                options=[{'label':x, 'value':x, 'disabled':False}
                         for x in df2['suspicious_activity'].unique()
                         ],
                value=['No','Yes'],
                inline=True,
            ),
        dcc.Graph(id='mypieIn', figure={}, style={'display': 'inline-block'}),
        dcc.Graph(id='mypieOut', figure={}, style={'display': 'inline-block'}),
        dcc.Graph(id='myScatIn', figure={}, style={'display': 'inline-block'}),
        dcc.Graph(id='myScatOut', figure={}, style={'display': 'inline-block'}),
        dcc.Graph(id='myLineIn', figure={}, style={'display': 'inline-block'}),
        ]),


    html.Div([
        html.H1("Web Server Access Log"),
        dag.AgGrid(id='grid',
                   rowData=df1.to_dict('records'),
                   columnDefs=[{'field':i} for i in df1.columns],
        ),
        html.H1('Network Traffic Log'),
        dag.AgGrid(id='grid2',
                   rowData=df2.to_dict('records'),
                   columnDefs=[{'field': i} for i in df2.columns],
        ),
    ]),
]),

@callback(
#  Output('myHist', 'figure'),
         Output('mypieIn', 'figure'),
         Output('mypieOut', 'figure'),
         Output('myScatIn', 'data'),
         Output('myScatOut', 'data'),
#         Input('methodChoice', 'value'),
          Input('checklist', 'value'),
#
)
def update_graph(value_chosen):
#     #print(value_method)
    dff2 = df2[df2['suspicious_activity'].isin(value_chosen)]


    # if type(value_chosen) != str:
    #     dff = df2[df2['suspicious_activity'].isin(value_chosen)]
    # else:
    #     dff = df2[df2.http_method == value_chosen],

    piechartIn = px.pie(
        data_frame=dff2,
        values='inbound_bytes',
        names='suspicious_activity',
        title='Suspicious Inbound Bytes',
    )
    piechartOut = px.pie(
         data_frame=dff2,
         values='outbound_bytes',
         names='suspicious_activity',
         title='Suspicious Outbound Bytes',
    )
    scatIn = px.scatter(df2, x='sample_time', y='inbound_bytes', color='suspicious_activity', title= 'IN')
    scatOut = px.scatter(df2, x='sample_time', y='outbound_bytes', color='suspicious_activity')

#
#     fig_hist1 = px.histogram(dff, x='timestamp', y='response_time_ms', color='http_method')
#     fig_scat1 = px.scatter(dff, x='timestamp', y='response_time_ms', color='http_method')
#     fig_urlscat= px.scatter(dff, x='url_accessed', y='response_time_ms', color='http_method', title='URL Response Time by Method')
#
    return piechartIn, piechartOut, scatIn, scatOut


