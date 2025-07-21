import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page

from app import app
from app import server

from pages import request_methods, authentication, server_performance, Home, alerts_threats, statistics, \
    alerts_incidents

app = Dash(external_stylesheets=[dbc.themes.SLATE])

ACCORDION_STYLE = { "position": "fixed",
                   "top":0,
                   "bottom":0,
                   "left":0,
                   "right":0,
                   "width": "19rem",
                   "padding": "2rem 1rem",
                   "background-color": "#f8f9fa",}
CONTENT_STYLE = { "margin-left": "18rem",
                 "margin-right": "2rem",
                 "padding": "2rem 1rem",}
accordion = html.Div(

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
            dbc.Button("Threat Alerts", href='/alerts_threats', color="link"),
            dbc.Button("Incident Alerts", href="/alerts_incidents", color="link"),
            ],
            title="Alerts",

#        pills=True,
        ),
    ]
    ),
#     style=ACCORDION_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([
 #    dcc.Location(id="url"), accordion, content]),
#    html.Div([
 #        dcc.Link(page['name']+ " | ", href=page['path'])
 #    for page in dash.page_registry.values()]
#    ),
    dash.page_container,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/" or pathname == "/Home":
        return Home.layout
    elif pathname == "/authentication":
        return authentication.layout
    elif pathname == "/request_methods":
        return request_methods.layout
    elif pathname == "/server_performance":
        return server_performance.layout
    elif pathname == '/alerts_threats':
        return alerts_threats.layout
    elif pathname == '/alerts_incidents':
        return alerts_incidents.layout
    elif pathname == '/statistics':
        return statistics.layout
    return html.Div(
        [html.H1("404: Not Found", className='text-danger'),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."),
         ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == "__main__":
    app.run(debug=True)
