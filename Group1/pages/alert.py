####
#   Alerts Page
#   Includes two tables: "Threat Alerts" and "Incident Alerts"
#   Each table has computed executive summaries above it
####
from dash import Dash, dcc, html, Input, Output, dash_table, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash()

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
                html.H3("Alert Count:"),
                html.Br(),
                #html.H3("Mean Response Time:"),
            ], style={'width': '45%', 'display': 'inline-block'}),
            html.Div([
                html.H3(sec_row_count, style={'text-align': 'right'}),
                html.Br(),
                #html.H3(str(mean_response) + " min.", style={'text-align': 'right'}),
            ], style={'width': '45%', 'display': 'inline-block'}),
        ], style={'width': '25%', 'display': 'inline-block', 'vertical-align': 'top'}),
        dcc.Graph(figure=thr_pie_fig,
                  style={
                      'width': '25%',
                      'display': 'inline-block',
                  }),
        dcc.Graph(figure=sev_bar_fig,
                  style={
                      'width': '30%',
                      'display': 'inline-block',
                  }),
        dcc.Graph(figure=rem_pie_fig,
                  style={
                      'width': '20%',
                      'display': 'inline-block',
                  }),
    ],
    style={
        'height':'30vh',
    }),
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
        style_table={
            'overflowY': 'scroll',
            'height': '50vh',
            'cell-align': 'center',
        },
    ),

    html.Div(
        id='alerttable-interactivity-container'
    ),
    html.Div([
        html.Div([
            html.H2("Executive Summary"),
            html.Div([
                html.H3("Incident Total:"),
                html.Br(),
                html.H3("Mean Response Time:"),
            ], style={'width': '45%', 'display': 'inline-block'}),
            html.Div([
                html.H3(rep_row_count, style={'text-align': 'right'}),
                html.Br(),
                html.H3(str(mean_response) + " min.", style={'text-align': 'right'}),
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




# if __name__ == "__main__":
#     app.run(debug=True)
