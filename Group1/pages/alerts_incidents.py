from dash import Dash, dcc, html, Input, Output, dash_table, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash()

rep_df = pd.read_csv('datasets/Dataset 5__Security_Incident_Reports.csv')
rep_df.columns = rep_df.columns.str.replace('_', ' ').str.replace('minutes', '(minutes)').str.title()

# Calculate values for executive summary
mean_response = rep_df['Response Time (Minutes)'].mean()
rep_row_count = rep_df['Category'].count()

cat_pie_df = rep_df["Category"].value_counts()
cat_pie_fig = px.pie(values=cat_pie_df.values, names=cat_pie_df.index, title="Incident Categories", hole=.3)

res_pie_df = rep_df["Resolution Status"].value_counts()
res_pie_fig = px.pie(values=res_pie_df.values, names=res_pie_df.index, title="Incident Statuses", hole=.3)

det_pie_df = rep_df["Detected By"].value_counts()
det_pie_fig = px.pie(values=det_pie_df.values, names=det_pie_df.index, title="Incident Detectors", hole=.3)


layout = html.Div([
    dbc.Button("Home", href="/Home", color="link"),
    html.Div([
        html.Div([
            html.H2("Executive Summary"),
            html.Div([
                html.H4("Incident Total:"),
                html.Br(),
                html.H4("Mean Response Time:"),
            ], style={'width': '45%', 'display': 'inline-block'}),
            html.Div([
                html.H4(rep_row_count, style={'text-align': 'right'}),
                html.Br(),
                html.H4(str(mean_response) + " min.", style={'text-align': 'right'}),
            ], style={'width': '45%', 'display': 'inline-block'}),
        ], style={'width': '25%', 'display': 'inline-block', 'vertical-align': 'top'}),
        dcc.Graph(figure=cat_pie_fig,
                  style={
                      'width': '30%',
                      'display': 'inline-block',
                  }),
        dcc.Graph(figure=res_pie_fig,
                  style={
                      'width': '20%',
                      'display': 'inline-block',
                  }),
        dcc.Graph(figure=det_pie_fig,
                  style={
                      'width': '25%',
                      'display': 'inline-block',
                  }),
    ],
    style={
        'height':'30vh',
    }),
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False} for i in rep_df.columns
        ],
        data=rep_df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_selectable="multi",
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 50,
        style_table={
            'overflowY': 'scroll',
            'height': '50vh',
            'cell-align': 'center',
        },
    ),

    html.Div(
        id='datatable-interactivity-container'
    )
],
    style={
        'width': '80vw',
        'margin-left': 'auto',
        'margin-right': 'auto'
    }
)

