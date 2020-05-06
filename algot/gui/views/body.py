# Third Party Imports
import dash
import dash_html_components as html
import dash_core_components as dcc

# Local Imports
from gui.views import graphs


home_layout = html.Div(id='home', children=[
    html.Div(id='home-chart-container', children=[
        dcc.Graph(id='home-chart'),
        html.Button('1 Day')
    ]),
    html.Div(id='home-indicators', children=[
        html.H3('Sharp Ratio')
    ]),
    html.Div(id='home-table', children=[
        html.H3('Watchlist Table')
    ])
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

settings_layout = html.Div(id='settings', children=[
    html.Div([
        html.P('Set Interval for API Calls (Seconds)', className='settings-label'),
        dcc.Slider(
        id='refresh-slider',
        updatemode='drag',
        min=5,
        max=60,
        step=None,
        marks={
            5: '5',
            10: '10',
            15: '15',
            20: '20',
            30: '30',
            60: '60'
        }
    )
    ], className='settings-pair'),
    html.Div([html.H1('Other settings')])
])



