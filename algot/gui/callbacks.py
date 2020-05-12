# Third Party Imports
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Local Imports
from gui.app import app

# Set app interval

@app.callback(Output('app-interval', 'interval'),
                [Input('settings-local-store', 'data')])
def get_app_interval(data):
    if data is None:
        raise PreventUpdate
    return data['refresh_slide']*1000


# Data Input

@app.callback(Output('settings-local-store', 'data'),
                [Input('refresh-slider', 'value')])
def update_app_interval(value):
    if value is None:
        raise PreventUpdate
    return {'refresh_slide': value}

@app.callback(Output('securities-local-store', 'data'),
                [Input('security-period-slider', 'value')])
def update_security_period(value):
    if value is None:
        raise PreventUpdate
    return {'security_period_slider': value}


# Data Loading

@app.callback(Output('refresh-slider', 'value'),
                [Input('nav-bar', 'value')],
                [State('settings-local-store', 'data')])
def load_settings_data(value, data):
    # print(data)
    if value == 'settings':
        return data['refresh_slide']

@app.callback(Output('security-period-slider', 'value'),
                [Input('nav-bar', 'value')],
                [State('securities-local-store', 'data')])
def load_security_period(value, data):
    # print(data)
    if value == 'securities':
        return data['security_period_slider']