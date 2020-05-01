import dash
import dash_html_components as html
import dash_core_components as dcc
from gui.serve import Serve

app = dash.Dash(__name__)

server = Serve()

account = html.Div([
    html.H3('Account Details'),
    html.Span([
        html.H4('Cash-on-hand: '),
        server.get_cash()
    ])
])

dashboard = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'
    ),
    html.Div(id='dd-output-container')
])

app.layout = html.Div([
    dashboard,
    account
])

# if __name__ == '__main__':
#     app.run_server(debug=True)