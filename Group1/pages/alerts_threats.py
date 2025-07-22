from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

sec_df = pd.read_csv('datasets/Dataset 3__Malware_Threat_Alerts.csv')
sec_df.columns = sec_df.columns.str.replace('_', ' ').str.title()

sec_row_count = sec_df['Severity'].count()

thr_pie_df = sec_df["Threat Type"].value_counts()
thr_pie_fig = px.pie(values=thr_pie_df.values, names=thr_pie_df.index, title="Threat Types", hole=.3)

rem_pie_df = sec_df["Remediation Status"].value_counts()
rem_pie_fig = px.pie(values=rem_pie_df.values, names=rem_pie_df.index, title="Threat Statuses", hole=.3)

sev_bar_df = sec_df["Severity"].value_counts(sort=False)
sev_bar_fig = px.bar(sev_bar_df, title="Severity Counts")
sev_bar_fig.update_layout(showlegend=False)


layout = html.Div([
    dbc.Button("Home", href="/Home", color="link"),
    html.H1("Threat Alerts"),
    html.Br(),
    html.Div([
        html.Div([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([
                html.H4("Alert Count:"),
            ], style={'width': '45%', 'display': 'inline-block'}),
            html.Div([
                html.H4(sec_row_count, style={'text-align': 'right'}),
            ], style={'width': '45%', 'display': 'inline-block'}),
        ], style={'width': '25%', 'display': 'inline-block', 'vertical-align': 'top'}),
        dcc.Graph(figure=thr_pie_fig,
                  style={'width': '25%', 'display': 'inline-block'}),
        dcc.Graph(figure=sev_bar_fig,
                  style={'width': '30%', 'display': 'inline-block'}),
        dcc.Graph(figure=rem_pie_fig,
                  style={'width': '20%', 'display': 'inline-block',}),
    ], style={'height':'30vh'}
    ),
    dash_table.DataTable(
        id='alerttable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False} for i in sec_df.columns
        ],
        data=sec_df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_selectable="multi",
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 50,
        style_table={'overflowY': 'scroll', 'height': '50vh', 'cell-align': 'center'},
    ),
    html.Div(id='alerttable-interactivity-container'),
], style={'width': '80vw', 'margin-left': 'auto', 'margin-right': 'auto'}
)

