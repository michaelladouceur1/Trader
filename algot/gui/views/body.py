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
    html.H1('Settings'),
    dcc.Slider(
        id='refresh-slider',
        min=5,
        max=60,
        step=None,
        marks={
            5: '5 Seconds',
            10: '10 Seconds',
            15: '15 Seconds',
            20: '20 Seconds',
            30: '30 Seconds',
            60: '60 Seconds'
        },
        value=20
    )
])



