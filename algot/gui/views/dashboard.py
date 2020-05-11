# Third Party Imports
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Local Imports
from gui.serve import Serve
from gui.views.dashboard_header import Data
from gui.app import app

server = Serve()

# account

account = html.Div([
    html.H3('Account Details', className='dashboard-header'),
    html.Span([
        html.Div([html.P('Cash-on-hand', className='dashboard-label'), html.H5(f'${server.cash}', className='dashboard-value')], className='dashboard-pair'),
        html.Div([html.P('Investment Value', className='dashboard-label'), html.H5(f'${server.investment_value}', className='dashboard-value')], className='dashboard-pair'),
        html.Div([html.P('Total Return', className='dashboard-label'), html.H5(f'{server.total_return}%', className='dashboard-value')], className='dashboard-pair'),
        html.Div([html.P('Total Liquid Value', className='dashboard-label'), html.H5(f'${server.total_liquid_value}', className='dashboard-value')], className='dashboard-pair')
    ], className='dashboard-body')
], className='dashboard-module')


# watchlist

data = Data()

watchlist = html.Div([
    html.H3('Watchlist', className='dashboard-header'),
    html.Span([
        html.P('Symbol', className='dashboard-table-label'),
        html.P('Open', className='dashboard-table-label'),
        html.P('Close', className='dashboard-table-label'),
        html.P('High', className='dashboard-table-label'),
        html.P('Low', className='dashboard-table-label')
    ], className='dashboard-table-header'),
    html.Div(id='watchlist-content')
], className='dashboard-module')

@app.callback(Output('watchlist-content', 'children'),
            [Input('app-interval', 'n_intervals')])
def update_watchlist_content(n):
    watchlist_content = []
    dashboard_data = data.update_data()
    for i in dashboard_data:
        watchlist_content.append(html.Span([
            html.P(i['Symbol'], className='dashboard-table-value'),
            html.P(i['Open'], className='dashboard-table-value'),
            html.P(i['Close'], className='dashboard-table-value'),
            html.P(i['High'], className='dashboard-table-value'),
            html.P(i['Low'], className='dashboard-table-value')
        ], className='dashboard-table-content'),)
    return watchlist_content


# movers

movers = html.Div([
    html.H3('Movers', className='dashboard-header'),
    html.Span([
        html.P('Symbol', className='dashboard-label'),
        html.P('Open', className='dashboard-label'),
        html.P('Close', className='dashboard-label'),
        html.P('High', className='dashboard-label'),
        html.P('Low', className='dashboard-label')
    ], className='dashboard-table-header'),
    
], className='dashboard-module')


# navigation

navigation = html.Div([
    dcc.Tabs(
        id='nav-bar',
        value='home',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(className='custom-tab', selected_className='custom-tab-selected', label='Home', value='home'),
            dcc.Tab(className='custom-tab', selected_className='custom-tab-selected', label='Securities', value='securities'),
            dcc.Tab(className='custom-tab', selected_className='custom-tab-selected', label='Options', value='options'),
            dcc.Tab(className='custom-tab', selected_className='custom-tab-selected', label='Algorithms', value='algorithms'),
            dcc.Tab(className='custom-tab', selected_className='custom-tab-selected', label='Settings', value='settings')
        ]
    )
])


# dashboard

dashboard = html.Div([
    watchlist,
    account,
    movers
], id='dashboard')