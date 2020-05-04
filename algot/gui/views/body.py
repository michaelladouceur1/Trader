import dash
import dash_html_components as html
import dash_core_components as dcc

from gui.views import graphs

home_graphs = html.Div(id='home-graphs',children=[
    dcc.Graph(id='home-chart')
])

home_layout = html.Div([
    home_graphs
])

securities_layout = html.Div([
    html.H1('Securities')
])

options_layout = html.Div([
    html.H1('Options')
])

algorithms_layout = html.Div([
    html.H1('Algorithms')
])

settings_layout = html.Div([
    html.H1('Settings')
])


