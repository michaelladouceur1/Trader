# Third Party Imports
import dash
import dash_html_components as html
import dash_core_components as dcc
from datetime import date
import csv

# Local Imports
from gui.views import graphs

def get_tickers():
    symbols = []
    CSV_PATH = '/home/michael/Documents/Coding/Finance/Trader/algot/gui/assets/'
    files = ['nasdaq-symbols.csv', 'nyse-symbols.csv']
    for f in files:
        with open(f'{CSV_PATH}{f}') as file:
            data = csv.reader(file)
            for row in data:
                symbols.append({'label': f'({row[0]}) {row[1]}', 'value': row[0]})
    return symbols

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

securities_layout = html.Div(id='securities', children=[
    html.Div([
        html.Div([html.P('none', id='none')]),
        html.Button('Save to Database', id='local-security-button', n_clicks=0),
        dcc.Slider(
            id='local-security-slider',
            updatemode='drag',
            min=1,
            max=20,
            value=20,
            step=None,
            marks={
                1: '1',
                2: '2',
                3: '3',
                5: '5',
                10: '10',
                15: '15',
                20: '20'
            },
            persistence=True,
            persistence_type='local'
        ),
        dcc.Dropdown(
            id='local-security-dropdown',
            className='dropdown',
            options=get_tickers(),
            multi=True,
            placeholder='Select a company...',
            persistence=True,
            persistence_type='local'
        )
    ]),
    html.Div([

    ])
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
    ], className='settings-pair')
])

