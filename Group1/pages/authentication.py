import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback, dash_table
import dash_ag_grid as dag

df1 = pd.read_csv('datasets/Dataset 2__User_Authentication_Logs.csv')
geo_count_series = df1.groupby('geo_location')['username'].count()
geo_count_df = geo_count_series.reset_index()
geo_count_df.columns = ['geo_location', 'count']
pie_fig = px.pie(
    data_frame=geo_count_df,
    values='count',
    names='geo_location',
    title='Location Distribution of All Users',
)
user_fig = px.histogram(df1, x='username', y='status_num', color='login_status',
                                 title="User's Logins")

app = dash.Dash(__name__)
#
layout = html.Div([
      html.H1("Authentication"),
      dbc.Button("Home", href="/Home", color="link"),

    html.Div([
#
          dcc.Graph(id='myUserLogin', figure=user_fig, style={'width': '50%', 'display': 'inline-block'}),
          dcc.Graph(id='myGeoPie', figure=pie_fig, style={'width': '50%', 'display': 'inline-block'}),

     ]),
    html.Div([
        dcc.Dropdown(id='locationChoice', options=
        [{'label':x, 'value':x}
        for x in df1.username.unique()],
        value='admin', multi=False,
        ),
        dcc.Graph(id='location_hist', figure={}, style={'width': '100%','display': 'inline-block'}),
    ]),

    html.Div([
        html.H1("Authentication Log"),
        dag.AgGrid(id='grid',
                   rowData=df1.to_dict('records'),
                   columnDefs=[{'field':i} for i in df1.columns],
        ),

    ]),
])

@callback(
    Output('location_hist', 'figure'),
    [Input('locationChoice', 'value')],

)

def interactive_graph(dropdown):
    if type(dropdown) != str:
        dff = df1[df1['username'].isin(dropdown)]
    else:
        dff = df1[df1.username==dropdown]

    location_fig = px.histogram(dff, x='geo_location', y='status_num',color='username')
    location_fig.update_layout(title="User's Location",
                              yaxis_title='Total User Login',
                              xaxis_title='Username')
    return location_fig





