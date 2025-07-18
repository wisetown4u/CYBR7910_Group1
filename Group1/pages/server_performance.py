import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback, dash_table
import dash_ag_grid as dag

df1 = pd.read_csv('datasets/Dataset 1__Web_Server_Access.csv')
df2 = pd.read_csv('datasets/Dataset 4__Network_Traffic_Summary.csv')


fig_pie = px.pie(df1, values='http_method', names='status_code', color='status_code', title='Method Status Code'),
barIn = px.bar(df2, x='protocol', y='inbound_bytes', color='suspicious_activity', title= 'Inbound Suspicious Activity by Protocol')
barOut = px.bar(df2, x='protocol', y='outbound_bytes', color='suspicious_activity', title= 'Outbound Suspicious Activity by Protocol')
piechartIn = px.pie(
        data_frame=df2,
        values='inbound_bytes',
        names='suspicious_activity',
        title='Suspicious Inbound Bytes',
)

piechartOut = px.pie(
         data_frame=df2,
         values='outbound_bytes',
         names='suspicious_activity',
         title='Suspicious Outbound Bytes',
)


app = dash.Dash(__name__)


layout = html.Div([
    html.H1("View Server Performance"),
    dbc.Button("Home", href="/Home", color="link"),

        html.Div([

        dcc.Graph(figure=piechartIn, style={'width': '25%', 'display': 'inline-block'}),
        dcc.Graph(figure=barIn, style={'width': '75%', 'display': 'inline-block'}),
        dcc.Graph(figure=piechartOut, style={'width': '25%', 'display': 'inline-block'}),
        dcc.Graph(figure=barOut, style={'width': '75%', 'display': 'inline-block'}),

        ]),

        html.Div([
            dcc.RadioItems(
                id='radioItem',
                options=[{'label':x, 'value':x, 'disabled':False}
                for x in df1['url_accessed'].unique()],
                inline=True,
                value='/admin',
                inputStyle={'margin-right': '5px', 'margin-left': '10px'},
            ),
            dcc.Graph(id='status_hist', figure={})
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
    Output('status_hist', 'figure'),
    [Input('radioItem', 'value'),]
)
def update_graph(url_chosen):

    dff = df1
    if type(url_chosen) != str:
        dff1 = dff[dff['url_accessed'].isin(url_chosen)]
    else:
        dff1 = dff[dff.url_accessed==url_chosen]



    url_fig = px.scatter(dff1, x='status_code', y='response_time_ms', color='url_accessed')
    url_fig.update_layout(title="Status Code of URLs Accessed",
                               yaxis_title='Response Time (ms)',
                               xaxis_title='Status Code')
    return url_fig





