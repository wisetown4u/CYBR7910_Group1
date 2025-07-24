from dash import dcc, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

traffic = pd.read_csv('datasets/Dataset 4__Network_Traffic_Summary.csv')
incidents = pd.read_csv('datasets/Dataset 5__Security_Incident_Reports.csv')

inbound_activity_chart = px.histogram(traffic, title="Inbound Activity", x="protocol", y="inbound_bytes", color="suspicious_activity", barmode="group")
inbound_activity_chart.update_xaxes(categoryorder="category ascending")

outbound_activity_chart = px.histogram(traffic, title="Outbound Activity", x="protocol", y="outbound_bytes", color="suspicious_activity", barmode="group")
outbound_activity_chart.update_xaxes(categoryorder="category ascending")

suspicious = traffic[traffic["suspicious_activity"] == "Yes"]
suspicious_chart = px.histogram(suspicious, title="Suspicious Activity Summary", x="protocol", y=["inbound_bytes", "outbound_bytes"], barmode="group")
suspicious_chart.update_xaxes(categoryorder="category ascending")

incident_time_chart = px.histogram(incidents, title="Total Response Time by Alert Category", x="response_time_minutes", y="category", orientation="h")
incident_time_chart.update_yaxes(categoryorder="category ascending")

layout = html.Div([
    html.Div([
        dbc.Button("Home", href="/Home", color="link"),
    ]),
    html.Div([
        dcc.Graph(figure=inbound_activity_chart),
    ],style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(figure=outbound_activity_chart),
    ],style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(figure=suspicious_chart),
    ]),
    html.Div([
        dcc.Graph(figure=incident_time_chart),
    ])
], style={'width': '90%', 'margin-left': 'auto', 'margin-right': 'auto'})