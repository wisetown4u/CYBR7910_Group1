import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback, dash_table
from plotly.graph_objs import Figure
import dash_ag_grid as dag

df = pd.read_csv('datasets/Dataset 2__User_Authentication_Logs.csv')


#lineIn = px.scatter(df2, x='sample_time', y='inbound_bytes', color='suspicious_activity')
#fig_pie = px.pie(df1, values='http_method', names='status_code', color='status_code', title='Method Status Code'),
#activity = df2.suspicious_activity.unique().tolist()
#lineIn.show()

app = dash.Dash(__name__)


layout = html.Div([
    html.H1("View Server Performance"),
    dbc.Button("Home", href="/Home", color="link"),



        html.Div([
            dcc.Dropdown(id='dropChoice', options=
            [{'label': x, 'value': x}
             for x in df.geo_location.unique()],
                value=df.geo_location.unique(), multi=False,
            ),
            dcc.Graph(id='pieUserLocation', figure={}, style={'display': 'inline-block'}),
            #dcc.Graph(id='pieOut', figure={}, style={'display': 'inline-block'}),
            dcc.Graph(id='myScatUsers', figure={}, style={'display': 'inline-block'}),
        # dcc.Graph(id='myScatOut', figure={}, style={'display': 'inline-block'}),
        # dcc.Graph(id='myLineIn', figure={}, style={'display': 'inline-block'}),
        ]),


    html.Div([
        html.H1("Authentication Log"),
        dag.AgGrid(id='grid',
                   rowData=df.to_dict('records'),
                   columnDefs=[{'field':i} for i in df.columns],
        ),


    ]),
]),

@callback(
# #  Output('myHist', 'figure'),
         Output('pieUserLocation', 'figure'),
#                 #Output('pieOut', 'figure'),
#         Output('myScatUsers', 'data'),
#          #Output('myScatOut', 'data'),
# #         Input('methodChoice', 'value'),
          Input('dropChoice', 'value')
)

def update_graph(value_chosen):
# #     #print(value_method)
    #dff = df[df['geo_location'].isin(value_chosen)]
    pieCounts = df.groupby('geo_location')['username'].value_counts()
    df1 = pd.DataFrame({'geo_location': pieCounts.index, 'username': pieCounts.values})
    fig = px.pie(df1, names='geo_location', values='username', color='username')
#

#
#     if type(value_chosen) != str:
#         dff = df[df['geo_location'].isin(value_chosen)]
#     else:
#          dff = df[df.geo_location==value_chosen],
#
#     # piechartIn = px.pie(
#     #     data_frame=dff,
#     #     values='login_timestamp',
#     #     names='geo_location',
#     #     title='Geo Location of Users',
#     # )
#     # piechartOut = px.pie(
#     #      data_frame=dff2,
#     #      values='outbound_bytes',
#     #      names='suspicious_activity',
#     #      title='Suspicious Outbound Bytes',
#     # )
#
#
# #
# #     fig_hist1 = px.histogram(dff, x='timestamp', y='response_time_ms', color='http_method')
#     fig_scat1 = px.scatter(dff, x='username', y='login_timestamp', color='geo_location')
# #     fig_urlscat= px.scatter(dff, x='url_accessed', y='response_time_ms', color='http_method', title='URL Response Time by Method')
#
    #return fig_scat1


