import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output 

from gui.app import app 
from gui.views import dashboard, body


# Layout

app.layout = html.Div([
    dashboard.dashboard,
    dashboard.navigation,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Router

@app.callback(Output('page-content', 'children'),
              [Input('nav-bar', 'value')])
def display_page(pathname):
    if pathname == 'home':
        return body.home_layout
    elif pathname == 'securities':
        return body.securities_layout
    elif pathname == 'options':
        return body.options_layout
    elif pathname == 'algorithms':
        return body.algorithms_layout
    elif pathname == 'settings':
        return body.settings_layout
    else:
        return body.home_layout
    # You could also return a 404 "URL not found" page here

app.run_server(debug=True)