import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page


app = Dash(__name__,external_stylesheets=[dbc.themes.LUMEN])

image_path = 'assets/Pic1.jpg'

ACCORDION_STYLE = { "position": "fixed",
                    "top":0,
                    "bottom":0,
                    "left":0,
                    "right":0,
                    "width": "95rem",
                    "padding": "2rem 1rem",
                    #"background-color": "#f8f9fa",
                    }
CONTENT_STYLE = { "margin-left": "18rem",
                  "margin-right": "2rem",
                  "padding": "2rem 1rem",}
#app.layout = dbc.Container([
#    dbc.Row([dbc.Col(html.Div("Welcome!", style={'fontSize': 50, 'textAlign': 'right'}))]),
#])
layout= html.Div(

    dbc.Accordion([

        html.H2("Everything Organic", className="display-5"),
        html.Hr(),
        html.P("Group 1", className="lead"),

        dbc.AccordionItem(
            [dbc.Button ("Authentication", href="/authentication", external_link=True, color="link"),
                    dbc.Button("Request Methods", href="/request_methods", color="link"),
                    dbc.Button("Server Performance", href="/server_performance", color="link"),
                    #dbc.Button("Home", href="/Home", color="link"),
                    ],
                title="Events",
        ),
        dbc.AccordionItem(
            [
            dbc.Button("Coming Soon!", href='/statistics', color="link"),
            ],
            title="Statistics",
        ),
        dbc.AccordionItem(
    [
            dbc.Button("View Alerts", href='/alert', color="link"),
            ],
            title="Alerts",

#        pills=True,
        ),

        dbc.Container(fluid=True),
        html.Img(src=image_path, style={"height": "550px", "width": "1488px","float": "left", "imgClassName": ""}),

    ],
    flush=True,
    ),

    style=ACCORDION_STYLE,

)

content = html.Div(id="page-content", style=CONTENT_STYLE)




